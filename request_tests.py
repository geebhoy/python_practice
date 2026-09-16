import requests

url = "https://jsonplaceholder.typicode.com/users"

name = input("Enter your name: ")
email = input("Enter your email: ")
data = {
    "name": name,
    "email": email
}

response = requests.post(url, json=data)

print(response.status_code)
print(response.json())