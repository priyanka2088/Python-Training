import requests

url="https://jsonplaceholder.typicode.com/posts"
data={
    "title":"Priyanka's session","body":"heloo","userId":1
}

response=requests.post(url,json=data)
print(response.status_code)