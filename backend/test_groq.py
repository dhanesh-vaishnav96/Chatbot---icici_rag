from groq import Groq
from app.config import settings

client = Groq(api_key=settings.GROQ_API_KEY)

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[{"role": "user", "content": "hello"}]
)

print(response.choices[0].message.content)