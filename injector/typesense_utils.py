import os
import typesense
from dotenv import load_dotenv
import time
from utils import duration_text

def create_collection(schema):
  print("* creating collection")
  client.collections.create(schema)
  return

def create_documents_on_by_one(collection,documents):
  print(f"* creating {len(documents)} documents:")
  for document in documents:
    client.collections[collection].documents.create(document)
  return

def create_documents(collection,documents):
  start = time.time()
  print(f"* creating {len(documents)} documents:")
  client.collections[collection].documents.import_(documents, {'action': 'create'})
  duration = time.time() - start
  print(f"* created {len(documents)} documents in {duration_text(duration)}")
  return

def collection_exists(collection_name):
  try:
      docs = client.collections[collection_name].retrieve()
      print(f"collection '{collection_name}' exists")
      return True
  except typesense.exceptions.ObjectNotFound as e:
      print(e)
      print(f"collection '{collection_name}' does not exist")
      return False

def collection_delete(collection_name):
  client.collections[collection_name].delete()
  return

def collections_list():
  print("listing all collections:")
  collections = client.collections.retrieve()
  for collection in collections:
      print(f" - {collection['name']}")
  return

def get_client():
   return client

def create_client():
  load_dotenv()
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
  'connection_timeout_seconds': 10
  })
  return client

def search(collection,params):
  search_result = client.collections[collection].documents.search(params)
  return search_result

client = create_client()
