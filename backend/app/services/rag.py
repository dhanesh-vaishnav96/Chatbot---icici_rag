from groq import Groq
from app.config import settings
from app.services.vectorstore import retriever

client = Groq(api_key=settings.GROQ_API_KEY)

def ask_rag(question: str):
    if retriever is None:
        return "Vector DB connection failed."

    docs = retriever.invoke(question)

    context = "\n".join([d.page_content for d in docs])

    prompt = f"""
You are an insurance policy assistant.

Answer ONLY from context.
If answer not found, say "I don't know".

Context:
{context}

Question:
{question}
"""

    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.1-8b-instant"
    )

    return response.choices[0].message.content
