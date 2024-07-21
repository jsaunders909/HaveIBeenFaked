from requests import get, post

filename = "pineapple.jpeg"

url = "http://127.0.0.1:8000/image/" + filename

response = get(url)

response.raise_for_status()

print(response.content)
with open(f"images/output.jpg", "wb") as f:
    f.write(response.content)
