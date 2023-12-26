import utils as utl

chunk_list_file = "../.data/embedding_chunks.json"
cache_file="../.data/vectors.pkl"
# 'text-embedding-ada-002', 'all-MiniLM-L6-v2'
model="all-MiniLM-L6-v2"

print(f"embed {model} start")
chunk_list = utl.load_json(chunk_list_file)
vectors = utl.get_embeddings(chunk_list,cache_file,model,batch_size=200)
print(f" get_embeddings() returned {len(vectors)} vectors")
