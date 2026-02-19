import os


stellar_secret = os.getenv("STELLAR_SECRET", "SCNFSIG3ZKKURPHT7X4HHJIDYDOA3YUEIRQ4MUTQXUMVZGLJBOWANAFB")
horizom_url = os.getenv("HORIZON_URL", "https://horizon-testnet.stellar.org")
database_url = os.getenv("DATABASE_URL", "postgresql://postgres:Postgre218@localhost:5432/postgres")

backend_api_key = os.getenv("BACKEND_API_KEY", "dev-back-sec-key")
backend_api_key_header = os.getenv("BACKEND_API_KEY_HEADER", "X-API-Key")

django_webhook_url = os.getenv("DJANGO_WEBHOOK_URL", "http://127.0.0.1:8000/webhooks/blockchain/")
django_webhook_token = os.getenv("DJANGO_WEBHOOK_TOKEN", "dev-webhook-token")
django_webhook_timeout = int(os.getenv("DJANGO_WEBHOOK_TIMEOUT", "10"))