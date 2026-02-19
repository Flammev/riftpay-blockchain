# -*- coding: utf-8 -*-
import hashlib
import json

def generate_proof(payload: dict) -> str:
    """
    Generate stable SHA-256 hash from transaction data
    """
    serialized = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(serialized.encode("utf-8")).hexdigest()
