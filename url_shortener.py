import requests

def shorten_url(api_url, long_url):
    response = requests.get(api_url + long_url)
    if response.status_code == 200:
        return response.text.strip()
    return "Error: Unable to shorten URL"

long_url = input("Enter a long URL: ")
short_url = shorten_url("https://tinyurl.com/api-create.php?url=", long_url)
print("Shortened URL:", short_url)
