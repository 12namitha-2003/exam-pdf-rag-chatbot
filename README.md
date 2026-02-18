🚀 Features

Upload study PDFs

Context-aware question answering

Retrieval-Augmented Generation (RAG) architecture

Exam-oriented structured answers (14-mark style – in progress)

Conversational chat interface using Streamlit

Lightweight and CPU-compatible setup


🧠 Core Technologies Used

Frontend: Streamlit

Embedding Model: sentence-transformers/all-MiniLM-L6-v2

Vector Database: FAISS (IndexFlatL2)

Answer Generation Model (LLM): google/flan-t5-base

PDF Processing: PyPDF

Framework: Hugging Face Transformers

Acceleration Support: Accelerate, BitsAndBytes


🏗 Architecture Overview

PDF upload and text extraction

Text chunking for semantic indexing

Embedding generation using Sentence Transformers

FAISS-based similarity search

Context retrieval

Answer generation using FLAN-T5


🎯 Target Output Format (Under Improvement)

The goal of this project is to generate detailed, structured university exam answers in the following format:

Title

Introduction

Detailed Explanation

Key Points

Advantages / Disadvantages

Applications

Conclusion


