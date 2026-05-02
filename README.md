# rag-study-assistant
# 📘 AI-Powered Study Assistant (RAG Project)

## 👨‍💻 Author
Vivek Dutt Sharma

---

## 🚀 Overview
This project implements a **Retrieval-Augmented Generation (RAG)** system that answers user queries based on custom documents instead of general AI knowledge.

---

## 🎯 Features
- 📄 Document-based Q&A
- ⚡ Fast retrieval using FAISS
- 🤖 AI-generated answers using OpenAI
- 🔍 Semantic search with embeddings

---

## 🧠 How It Works

1. Load document (notes.txt)
2. Split text into chunks
3. Convert chunks into embeddings
4. Store in FAISS vector DB
5. User asks a question
6. Retrieve relevant chunk
7. Generate answer using LLM

---

## 🛠️ Tech Stack

- Python
- LangChain
- FAISS
- OpenAI API
- HuggingFace Embeddings

---

## 📥 Installation

```bash
git clone https://github.com/yourusername/rag-study-assistant.git
cd rag-study-assistant
pip install -r requirements.txt
