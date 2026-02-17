from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# -----------------------------
# Embedding Model
# -----------------------------
embed_model = SentenceTransformer("all-MiniLM-L6-v2")

index = None
chunks = None


# -----------------------------
# Create Vector Store
# -----------------------------
def create_vector_store(text_chunks):
    global index, chunks

    chunks = text_chunks
    embeddings = embed_model.encode(chunks)

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))


# -----------------------------
# Retrieve Context
# -----------------------------
def retrieve_context(question, k=3):
    global index, chunks

    if index is None:
        return ""

    q_embedding = embed_model.encode([question])
    D, I = index.search(np.array(q_embedding), k)

    context = " ".join([chunks[i] for i in I[0]])
    return context


# -----------------------------
# Load Generation Model
# -----------------------------
model_name = "google/flan-t5-base"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)


# -----------------------------
# RAG Chat Function
# -----------------------------
def rag_chat(question):

    context = retrieve_context(question)

    prompt = f"""
You are an academic exam assistant.

Generate a detailed 14-mark university exam answer.

Format:
1. Title
2. Introduction
3. Explanation
4. Key Points
5. Advantages / Disadvantages (if applicable)
6. Applications
7. Conclusion

Context:
{context}

Question:
{question}

Answer:
"""

    inputs = tokenizer(prompt, return_tensors="pt")

    outputs = model.generate(
        **inputs,
        max_new_tokens=500,
        do_sample=False
    )

    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return answer
