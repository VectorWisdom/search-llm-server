from utils import load_json, save_json, duration_text
import time

def get_headings(content):
    elements = []
    for heading in content["headings"]:
        elements.append({
            "doc_sid":content["sid"],
            "doc_type":"page",
            "heading":heading["slug"],
            "element_type":"heading",
            "element_value":heading["label"]
        })
    return elements

def get_tables(content):
    elements = []
    for table in content["tables"]:
        for cell in table:
            elements.append({
                "doc_sid":content["sid"],
                "doc_type":"page",
                "heading":table["heading"],
                "element_type":"table",
                "element_value":cell
            })
    return elements

def get_images(content):
    elements = []
    for image in content["images"]:
        for text in image["text"]:
            elements.append({
                "doc_sid":content["sid"],
                "doc_type":"page",
                "heading":image["heading"],
                "element_type":"diagram",
                "element_value":text
            })
    return elements

def get_codes(content):
    elements = []
    for code in content["code"]:
        elements.append({
            "doc_sid":content["sid"],
            "doc_type":"page",
            "heading":code["heading"],
            "element_type":"code",
            "element_value":code["value"]
        })
    return elements

def get_paragraphs(content):
    elements = []
    for paragraph in content["paragraphs"]:
        for text in paragraph["text"]:
            elements.append({
                "doc_sid":content["sid"],
                "doc_type":"page",
                "heading":paragraph["heading"],
                "element_type":"paragraph",
                "element_value":text
            })
    return elements

def get_pages_elements():
    start = time.time()
    pages_elements = []
    docs_list = load_json("../.data/document_list.json")
    for doc in docs_list:
        if(doc["format"].startswith("markdown")):
            content = load_json(f"../.data/documents/{doc['sid']}/content.json")
            pages_elements.extend(get_headings(content))
            pages_elements.extend(get_tables(content))
            pages_elements.extend(get_images(content))
            pages_elements.extend(get_codes(content))
            pages_elements.extend(get_paragraphs(content))
    duration = time.time() - start
    print(f"collected pages elements in {duration_text(duration)}")
    return pages_elements

def main():
    pages_elements = get_pages_elements()
    save_json("../.data/pages_elements.json",pages_elements)

main()
