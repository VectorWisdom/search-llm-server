from sentence_transformers import SentenceTransformer

def get_embedding_list(text_list,model_name="all-MiniLM-L6-v2"):
    check_client(model_name)
    results = model.encode(text_list, normalize_embeddings=True)
    sentence_embeddings = [entry.tolist() for entry in results]
    return sentence_embeddings

def create_model(model_name):
    model = SentenceTransformer(model_name)
    return model

def check_client(model_name):
    global model
    global g_model_name
    if((model == None) or (g_model_name != model_name)):
        model = create_model(model_name)
        g_model_name = model_name
    return

model = None
g_model_name = ""
