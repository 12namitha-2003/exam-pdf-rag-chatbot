# Exam PDF RAG Chatbot

## Project Overview
- This project is a PDF-based RAG (Retrieval-Augmented Generation) chatbot.
- Users can upload exam-related PDF documents and ask questions from the uploaded content.
- The chatbot retrieves relevant information from the PDF and generates answers using AI models.

---

## Features
- Upload PDF documents
- Extract text from PDFs
- Ask questions from uploaded PDFs
- AI-powered answer generation
- Context-based response generation
- Simple user interface using Streamlit
- Fast document search using vector embeddings

---

## Technologies Used
- Python
- Streamlit
- LangChain
- NLP (Natural Language Processing)
- Vector Database
- Embedding Models
- FAISS / ChromaDB
- OpenAI / Gemini API
- PyPDF

---

## Project Structure

```text
exam-pdf-rag-chatbot/
│
├── app.py
├── requirements.txt
├── README.md
├── data/
├── pdfs/
└── vector_store/
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/12namitha-2003/exam-pdf-rag-chatbot.git
```

---

### Move to Project Folder

```bash
cd exam-pdf-rag-chatbot
```

---

### Create Virtual Environment

```bash
py -3.10 -m venv venv
```

---

### Activate Virtual Environment

```bash
venv\Scripts\activate
```

---

### Install Required Packages

```bash
pip install -r requirements.txt
```

---

## Run the Project

```bash
streamlit run app.py
```

---

## How the System Works
1. User uploads PDF document
2. Text is extracted from PDF
3. Text is split into smaller chunks
4. Embeddings are created
5. Embeddings are stored in vector database
6. User asks question
7. Relevant chunks are retrieved
8. AI model generates contextual answer

---

## NLP Concepts Used
- Text preprocessing
- Tokenization
- Semantic search
- Embeddings
- Context retrieval
- Question answering
- Language generation
- Information retrieval

---

## Advantages
- Faster information retrieval from large PDFs
- Reduces manual searching effort
- Context-aware responses
- Interactive chatbot interface
- Useful for exam preparation and document analysis

---

## Constraints / Limitations
- Slow answer generation for large PDF files
- Accuracy depends on quality of uploaded PDF
- Requires internet connection for API-based models
- Large documents may increase processing time
- Limited understanding of complex diagrams/tables
- High memory usage for large vector databases
- Responses may vary depending on embedding quality

---

## Future Scope
- Add multilingual NLP support
- Improve response generation speed
- Integrate voice-based question answering
- Add OCR support for scanned PDFs
- Improve semantic understanding using advanced NLP models
- Add summarization feature
- Add chatbot memory for conversation history
- Deploy as cloud-based web application
- Integrate advanced LLMs for better contextual answers
- Add support for multiple PDF uploads
- Improve document ranking and retrieval accuracy

---

## Applications
- Exam preparation systems
- Academic document analysis
- Research paper assistance
- Question-answering systems
- Smart educational assistants

---


https://github.com/user-attachments/assets/c3e6008e-3c8e-49df-b5d3-65277fab4310


## Author
Namitha A Suresh
