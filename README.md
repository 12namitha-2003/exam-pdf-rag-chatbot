# exam-pdf-rag-chatbot

 Features

 Upload study PDFs

 Context-aware question answering

 Retrieval-Augmented Generation (RAG) architecture

 Structured 14-mark style exam answers

 Conversational chat interface (Streamlit)

 Lightweight and CPU-compatible setup


Core Technologies Used

Frontend: Streamlit

Embedding Model: sentence-transformers/all-MiniLM-L6-v2

Vector Database: FAISS (IndexFlatL2)

LLM (Answer Generation Model): google/flan-t5-base

PDF Processing: PyPDF

Frameworks: Hugging Face Transformers

Acceleration Support: Accelerate, BitsAndBytes


Architecture Overview

PDF is uploaded

Text is extracted and chunked

Chunks are converted into embeddings

FAISS builds a vector index

Relevant context is retrieved based on user question

FLAN-T5 generates a structured exam-style answer



Target Output Format (Under Improvement)

The goal of this project is to generate detailed, structured university exam answers in the following format:

Title

Introduction

Detailed Explanation

Key Points

Advantages / Disadvantages

Applications

Conclusion
