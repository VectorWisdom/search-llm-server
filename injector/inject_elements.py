import typesense_utils as tyutl
from utils import load_json

def main():
    if(tyutl.collection_exists("pages_elements")):
        tyutl.collection_delete("pages_elements")

    print("* creating new 'paegs' collection")
    schema_fields = load_json("schema_fields.json")
    schema = {
        "name": "pages_elements",
        "fields": schema_fields
    }
    tyutl.create_collection(schema)
    tyutl.collections_list()

    pages_elements = load_json("../.data/pages_elements.json")
    tyutl.create_documents("pages_elements",pages_elements)

main()
