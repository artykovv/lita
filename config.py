from dotenv import load_dotenv
import os


load_dotenv()

DB_HOST = os.environ.get("POSTGRESQL_HOST")
DB_PORT = os.environ.get("POSTGRESQL_PORT")
DB_NAME = os.environ.get("POSTGRESQL_DBNAME")
DB_USER = os.environ.get("POSTGRESQL_USER")
DB_PASS = os.environ.get("POSTGRESQL_PASSWORD")

PrivateKey = "certs/private.pem"
PublicKey = "certs/public.pem"
algorithm: str = "RS256"


API_KEYS = {
    os.getenv("API_KEY_1"): "Key1",
    os.getenv("API_KEY_2"): "Key2",
    os.getenv("api_key_for_jinja"): "Key3",
}

api_key = os.getenv("api_key_for_jinja")