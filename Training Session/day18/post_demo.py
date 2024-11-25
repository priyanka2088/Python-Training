import requests

url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "userId": 1,
    "title": "Anlin's Data",
    "body": "Hi"
}

response = requests.post(url, data)

if response.status_code == 201:
    print("Created")
else:
    print("Error", response.status_code)
