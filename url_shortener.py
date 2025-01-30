import hashlib
import string
import random

def generate_short_url(long_url):
    hash_object = hashlib.md5(long_url.encode())
    hash_hex = hash_object.hexdigest()

    short_url = hash_hex[:6]

    return short_url

def store_url_mapping(long_url, short_url, url_db):
    url_db[short_url] = long_url

def retrieve_long_url(short_url, url_db):
    return url_db.get(short_url, "URL not found!")

def main():
    url_db = {} 

    print("Welcome to the URL Shortener!")

    while True:
        long_url = input("Enter a long URL to shorten (or type 'exit' to quit): ")
        
        if long_url.lower() == 'exit':
            print("Exiting the URL shortener. Goodbye!")
            break

        short_url = generate_short_url(long_url)

        store_url_mapping(long_url, short_url, url_db)

        print(f"Shortened URL: http://short.ly/{short_url}")

        retrieve = input(f"Would you like to retrieve the long URL for {short_url}? (y/n): ")

        if retrieve.lower() == 'y':
            print(f"Long URL: {retrieve_long_url(short_url, url_db)}")

if __name__ == "__main__":
    main()
