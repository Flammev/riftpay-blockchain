import json
from datetime import datetime, timezone
from typing import Optional
from urllib.error import URLError
from urllib.request import Request as UrlRequest, urlopen

from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, Field

from blockchain_proofs import BlockchainProof, SessionLocal
from config import (
    backend_api_key,
    backend_api_key_header,
    django_webhook_timeout,
    django_webhook_token,
    django_webhook_url,
    horizom_url,
    stellar_secret,
)
from proofs import generate_proof
from stellar_client import StellarClient

app = FastAPI(title="Stellar Proof Backend", version="1.0.0")
stellar = StellarClient(horizom_url=horizom_url, stellar_secret=stellar_secret)


class TransferIn(BaseModel):
    local_transaction_id: int = Field(..., ge=1)
    reference_id: str = Field(..., min_length=1, max_length=255)
    sender_user_id: int
    receiver_user_id: int
    amount: str
    currency: str = Field(default="FCFA", min_length=1, max_length=10)
    timestamp: Optional[str] = None


class TransferOut(BaseModel):
    reference_id: str
    stellar_transaction_hash: str
    proof_hash: str
    amount: str
    currency: str
    status: str


def _send_webhook(payload: dict):
    if not django_webhook_url:
        return

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    if django_webhook_token:
        headers["X-Webhook-Token"] = django_webhook_token

    request = UrlRequest(
        url=django_webhook_url,
        data=json.dumps(payload).encode("utf-8"),
        headers=headers,
        method="POST",
    )

    try:
        with urlopen(request, timeout=django_webhook_timeout):
            return
    except URLError:
        return


def _check_api_key(provided_key: Optional[str]):
    expected = backend_api_key.strip()
    if expected and provided_key != expected:
        raise HTTPException(status_code=401, detail="Invalid API key")


@app.get("/health")
def health():
    return {"status": "ok", "service": "back_sec"}


@app.post("/api/transfers", response_model=TransferOut)
def create_transfer(
    body: TransferIn,
    request: Request,
):
    provided_key = request.headers.get(backend_api_key_header, "")
    _check_api_key(provided_key)

    hash_payload = {
        "local_transaction_id": body.local_transaction_id,
        "reference_id": body.reference_id,
        "sender_user_id": body.sender_user_id,
        "receiver_user_id": body.receiver_user_id,
        "amount": body.amount,
        "currency": body.currency,
        "timestamp": body.timestamp or datetime.now(timezone.utc).isoformat(),
    }

    proof_hash = generate_proof(hash_payload)

    try:
        stellar_tx_hash = stellar.write_proof(proof_hash)
    except Exception as exc:
        _send_webhook(
            {
                "reference_id": body.reference_id,
                "local_transaction_id": body.local_transaction_id,
                "status": "FAILED",
                "error_detail": f"Stellar submit failed: {str(exc)}",
                "amount": body.amount,
                "currency": body.currency,
            }
        )
        raise HTTPException(status_code=502, detail=f"Stellar submit failed: {str(exc)}")

    db = SessionLocal()
    try:
        record = BlockchainProof(
            transaction_id=str(body.local_transaction_id),
            proof_hash=proof_hash,
            stellar_tx_hash=stellar_tx_hash,
        )
        db.add(record)
        db.commit()
    except Exception as exc:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database save failed: {str(exc)}")
    finally:
        db.close()

    response = {
        "reference_id": body.reference_id,
        "stellar_transaction_hash": stellar_tx_hash,
        "proof_hash": proof_hash,
        "amount": body.amount,
        "currency": body.currency,
        "status": "CONFIRMED",
    }

    _send_webhook(
        {
            "reference_id": body.reference_id,
            "local_transaction_id": body.local_transaction_id,
            "stellar_transaction_hash": stellar_tx_hash,
            "proof_hash": proof_hash,
            "amount": body.amount,
            "currency": body.currency,
            "status": "CONFIRMED",
        }
    )

    return response
