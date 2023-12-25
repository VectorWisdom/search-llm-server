import utils as utl

print("embed_openai start")
elements_embeddings = utl.load_json("../.data/embedding_chunks.json")
cache_file="../.data/vectors.pkl"
model="text-embedding-ada-002"

vectors = utl.get_embeddings(elements_embeddings,cache_file,model)

print(f" get_embeddings() returned {len(vectors)} vectors")
