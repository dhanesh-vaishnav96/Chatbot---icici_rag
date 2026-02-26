import requests

url = "http://127.0.0.1:8000/chat"
data = {"message": "What is accidental death benefit?"}

response = requests.post(url, data=data)
print(f"Status Code: {response.status_code}")

if response.status_code == 200:
    html = response.text
    # Extract the answer which should be in the HTML
    # We'll just look for a rough indication or print the whole HTML
    print("Response received, length:", len(html))
    if "What is accidental death benefit?" in html:
        print("Message echoed back in HTML.")
    
    # We can use BeautifulSoup or just simple string find to extract the text.
    try:
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html, "html.parser")
        # Find where the answer might be. It depends on `chat.html`.
        # Let's print the visible text or just output it.
        print(soup.get_text()[:500])
    except ImportError:
        pass
    
    print("\nFull HTML Snippet:\n", html[:1000].encode('cp1252', 'replace').decode('cp1252'))

else:
    print(response.text)


