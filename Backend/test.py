from requests import get, post

sample_image = "../sample_images/Biden.jpg"

with open(sample_image, "rb") as f:
    bytes = f.read()

username = "John"

results = []
