import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")

print(response.status_code)

users = response.json()

print("Total users:", len(users))

for user in users:
    print("User:", user["name"])
print("First user's city:", users[0]["address"]["city"])

