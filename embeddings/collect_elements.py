from utils import load_json, save_json, duration_text
import time

def get_headings(content):
    elements = []
    for heading in content["headings"]:
        elements.append({
            "doc_sid":content["sid"],
            "doc_path":content["path"],
            "heading":heading["slug"],
            "type":"heading",
            "text":heading["label"]
        })
    return elements

def get_tables(content):
    elements = []
    for table in content["tables"]:
        elements.append({
            "doc_sid":content["sid"],
            "doc_path":content["path"],
            "heading":table["heading"],
            "type":"table",
            "text":table["text"],
            "sid": table["sid"]
        })
    return elements

def get_images(content):
    elements = []
    for image in content["images"]:
        if(len(image["text_list"]) > 0):
            text = ' '.join(image["text_list"])
            meta = "url="+image["url"] + " "
            if(image["title"] is not None):
                meta += "title="+image["title"] + " "
            if(image["alt"] is not None):
                meta += "alt="+image["alt"] + " "
            elements.append({
                "doc_sid":content["sid"],
                "doc_path":content["path"],
                "heading":image["heading"],
                "type":"diagram",
                "text":text,
                "meta":meta,
                "sid": image["sid"]
            })
    return elements

def get_codes(content):
    elements = []
    for code in content["code"]:
        meta = "language="+code["language"]
        elements.append({
            "doc_sid":content["sid"],
            "doc_path":content["path"],
            "heading":code["heading"],
            "type":"code",
            "text":code["text"],
            "meta":meta,
            "sid": code["sid"]
        })
    return elements

def get_paragraphs(content):
    elements = []
    for paragraph in content["paragraphs"]:
        elements.append({
            "doc_sid":content["sid"],
            "doc_path":content["path"],
            "heading":paragraph["heading"],
            "type":"paragraph",
            "text":paragraph["text"]
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

    # filter out empty entries
    pages_elements = [el for el in pages_elements if((len(el["text"])>0))]
    duration = time.time() - start
    print(f"collected pages elements in {duration_text(duration)}")
    return pages_elements

def main():
    pages_elements = get_pages_elements()
    save_json(pages_elements,"../.data/document_elements.json")

main()
