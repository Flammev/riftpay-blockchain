# stellar_client.py
from stellar_sdk import Server, Keypair, TransactionBuilder, Network
from config import stellar_secret, horizom_url

class StellarClient:
    def __init__(self, horizom_url, stellar_secret):
        self.server = Server(horizom_url)
        self.keypair = Keypair.from_secret(stellar_secret)
        self.public_key = self.keypair.public_key

    def write_proof(self, proof_hash: str) -> str:
        account = self.server.load_account(self.public_key)

        tx = (
            TransactionBuilder(
                source_account=account,
                network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
                base_fee=100
            )
            .append_manage_data_op(
                data_name="proof",
                data_value=proof_hash[:64])
            .set_timeout(30)
            .build()
        )

        tx.sign(self.keypair)
        response = self.server.submit_transaction(tx)
        return response["hash"]
