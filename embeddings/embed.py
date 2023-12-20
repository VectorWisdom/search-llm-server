import utils as utl
import tiktoken
from copy import deepcopy

def main():
    elements = utl.load_json("../.data/elements.json")
    encoding = tiktoken.encoding_for_model("text-embedding-ada-002")
    elements_embeddings = []
    for el in elements:
        #headings are irrelevant for semantic search and question answering
        if (el["type"] not in ["paragraph", "diagram", "code", "table"]):
            elements_embeddings.append(el)
            continue
        results = utl.split_chunk_text(el["text"],1000,200)
        for index,result in enumerate(results,1):
            el_part = deepcopy(el)
            el_part["text_len"] = len(result["text"])
            el_part["chunk_len"] = len(result["chunk"])
            el_part["text"] = result["text"]
            payload = ""
            if(el["heading"] is not None):
                payload += "heading="+el["heading"]+"\n"
            if("meta" in el):
                payload += el["meta"]+"\n"
            payload += result["chunk"]
            el_part["payload"] = payload
            el_part["hash"] = utl.short_md5(payload)
            el_part["tokens"] = len(encoding.encode(payload))
            if(len(results)>1):
                el_part["part"] = index
            elements_embeddings.append(el_part)
    utl.save_json("../.data/elements_embeddings.json",elements_embeddings)
    return

main()
