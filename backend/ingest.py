from pathlib import Path
from dotenv import load_dotenv
import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient

# load env
load_dotenv()

QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")

PDF_PATH = Path("ICICI Pru iProtect Smart.pdf")

# 1️⃣ Load PDF
loader = PyPDFLoader(str(PDF_PATH))
docs = loader.load()
print("Loaded pages:", len(docs))

# 2️⃣ Chunk
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
chunks = splitter.split_documents(docs)
print("Chunks created:", len(chunks))

# 3️⃣ Embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# 4️⃣ Cloud Qdrant client
client = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY
)

# 5️⃣ Store vectors
vectorstore = QdrantVectorStore.from_documents(
    chunks,
    embeddings,
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY,
    collection_name="icici_policy"
)

print("✅ Ingestion completed")