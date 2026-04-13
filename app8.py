import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
print(response.status_code)  # 200
print(response.json()) # {'userId': 1, 'id': 1, 'title': '...', 'body': '...'}

data = response.json()
print(data["userId"])

postData = {
    "userId": 90,
    "title": "yash",
    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
  },


respose = requests.post('https://jsonplaceholder.typicode.com/posts', json=postData)

print(respose.status_code)  # 201


responseJoke = requests.get("https://official-joke-api.appspot.com/random_joke")
print(responseJoke.status_code)  # 200
print(responseJoke.json())
print(responseJoke.json()["setup"])
print(responseJoke.json()["punchline"])