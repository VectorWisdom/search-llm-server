import openai_utils as outl
import utils as utl
import time

def fetch_chunk(chunk):
    if(not chunk["hash"] in vectors):
        start = time.time()
        embedding = outl.get_embedding(chunk["payload"],model=model)
        print(f"fetched embedding in {utl.duration_text(time.time()-start)}")
        vectors[chunk["hash"]] = embedding
    else:
        print(f" hash '{chunk['hash']}' already available")

def fetch_chunk_list(chunk_list):
    filtered_chunks = []
    for chunk in chunk_list:
        if(not chunk["hash"] in vectors):
            filtered_chunks.append(chunk)
    chunk_payloads = [chunk["payload"] for chunk in filtered_chunks]
    start = time.time()
    chunk_embeddings = outl.get_embedding_list(chunk_payloads,model=model)
    print(f"fetched {len(chunk_embeddings)} embedding in {utl.duration_text(time.time()-start)}")
    for index, embedding in enumerate(chunk_embeddings):
        hash = filtered_chunks[index]["hash"]
        vectors[hash] = embedding
    return

def fetch_big_chunk_list(big_chunk_list,list_size):
    list_of_lists =[]
    for i in range(0, len(big_chunk_list), list_size):
        chunk_list = big_chunk_list[i:i+list_size]
        list_of_lists.append(chunk_list)
    for chunk_list in list_of_lists:
        fetch_chunk_list(chunk_list)
    return

print("embed_openai start")
elements_embeddings = utl.load_json("../.data/embedding_chunks.json")
cache_file = "../.data/vectors.pkl"
model = "text-embedding-ada-002"
embeddings = utl.get_vectors_cache(cache_file, model)
vectors = embeddings[model]

fetch_big_chunk_list(elements_embeddings,200)

embeddings[model] = vectors
utl.save_pickle(embeddings,"../.data/vectors.pkl")
