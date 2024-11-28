from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def generate_embeddings(text_list):
    return model.encode(text_list, convert_to_tensor=True)

def find_best_match(scene_text, transcript_segments):
    scene_embedding = model.encode(scene_text, convert_to_tensor=True)
    transcript_texts = [t["text"] for t in transcript_segments]
    transcript_embeddings = model.encode(transcript_texts, convert_to_tensor=True)
    scores = util.pytorch_cos_sim(scene_embedding, transcript_embeddings)[0]
    best_idx = scores.argmax().item()
    return transcript_segments[best_idx], scores[best_idx].item()
