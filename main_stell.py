# main.py
from alchemy_con import SessionLocal
from stellar_client import StellarClient
from blockchain_proofs import BlockchainProof
from proofs import generate_proof
from main_class import *
from config import horizom_url, stellar_secret
from main_class import transfert

db = SessionLocal()
stellar = StellarClient(horizom_url=horizom_url, stellar_secret=stellar_secret)
id_tx = transfert.transaction_id
amount_tx = transfert.amount
sender_tx = transfert.sender
receiver_tx = transfert.receiver

data = {
    "transaction_id": id_tx,
    "amount": amount_tx,
    "sender": sender_tx,
    "receiver": receiver_tx
}

proof_hash = generate_proof(data)
stellar_tx = stellar.write_proof(proof_hash)

record = BlockchainProof(
    transaction_id=data["transaction_id"],
    proof_hash=proof_hash,
    stellar_tx_hash=stellar_tx
)

db.add(record)
db.commit()
