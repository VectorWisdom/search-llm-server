import os
import typesense
from dotenv import load_dotenv


def create_collection(client,schema):
  print("* creating collection")
  client.collections.create(schema)
  return

def create_documents(client,documents):
  print(f"* upserting {len(documents)} documents:")
  #print(client.collections['books'].documents.create(hunger_games_book))
  for document in documents:
    client.collections['books'].documents.upsert(document)
  return

def get_client():
    host = os.getenv('HOST')
    port = os.getenv('TYPESENSE_PORT')
    protocol = 'https' if (os.getenv('USE_HTTPS')=='true') else 'http'
    api_key = os.getenv('TYPESENSE_API_KEY')
    if(api_key is None):
        print("API key not found, provide TYPESENSE_API_KEY variable in .env")
        exit(0)

    print(f"connecting typesense client to {protocol}://{host}:{port}")

    client = typesense.Client({
    'api_key': api_key,
    'nodes': [{
        'host': host,
        'port': port,
        'protocol': protocol
    }],
    'connection_timeout_seconds': 2
    })
    return client

load_dotenv()
