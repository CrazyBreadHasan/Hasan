import requests

url = "https://www.mentimeter.com/blog/stand-out-get-ahead/trivia-questions"

response = requests.get(url)
print(response.text)