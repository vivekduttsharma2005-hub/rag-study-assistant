from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.llms import OpenAI
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Load document
loader = TextLoader("notes.txt")
documents = loader.load()

# Split into chunks
text_splitter = CharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
docs = text_splitter.split_documents(documents)

# Create embeddings
embeddings = HuggingFaceEmbeddings()

# Store in FAISS
db = FAISS.from_documents(docs, embeddings)

print("✅ Document processed successfully!")

# Ask questions loop
while True:
    query = input("\nAsk a question (or type 'exit'): ")

    if query.lower() == "exit":
        break

    # Retrieve relevant chunks
    retrieved_docs = db.similarity_search(query)

    context = retrieved_docs[0].page_content

    # Generate response
    llm = OpenAI(api_key=OPENAI_API_KEY)
    response = llm.predict(context + "\nQuestion: " + query)

    print("\n📌 Answer:\n", response)
