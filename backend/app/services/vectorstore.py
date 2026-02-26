from langchain_huggingface import HuggingFaceEmbeddings
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from app.config import settings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

try:
    client = QdrantClient(
        url=settings.QDRANT_URL,
        api_key=settings.QDRANT_API_KEY
    )

    vectorstore = QdrantVectorStore(
        client=client,
        collection_name="icici_policy",
        embedding=embeddings
    )

    retriever = vectorstore.as_retriever(search_kwargs={"k":3})
except Exception as e:
    print(f"Failed to initialize Qdrant: {e}")
    retriever = None

