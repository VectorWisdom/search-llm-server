import os
import typesense
from typesense_utils import get_client, create_collection, create_documents
from utils import load_json, save_json

def main():
    client = get_client()
    try:
        docs = client.collections['documents'].retrieve()
        print("collection 'documents' exist deleting old collection")
        client.collections['documents'].delete()
    except typesense.exceptions.ObjectNotFound as e:
        print(e)
        print("collection 'docs' does not exist")

    print("* creating new 'docs' collection")
    schema = load_json("schema.json")
    create_collection(client,schema)

    print("listing all collections:")
    collections = client.collections.retrieve()
    for collection in collections:
        print(f" - {collection['name']}")

    if os.path.exists("documents.json"):
        documents = load_json("documents.json")
    else:
        #TODO get documents from content-structure
        documents = []
        #save_json("books.json",books)
    #create_documents(client,documents)


main()
