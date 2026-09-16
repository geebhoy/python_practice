import requests

response = requests.get('https://example.com')

print("status: ", response.status_code)
print("content type: ", response.headers["content-type"])