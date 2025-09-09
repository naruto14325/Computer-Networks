# http_requests.py
import requests
import logging

# Configure logging
logging.basicConfig(filename="http_requests.log",
                    level=logging.ERROR,
                    format="%(asctime)s - %(levelname)s - %(message)s")

def send_get_request():
    url = "https://httpbin.org/get"
    params = {"course": "Computer Networks", "topic": "HTTP"}
    try:
        response = requests.get(url, params=params, timeout=5)
        print("=== GET Request ===")
        print("Status Code:", response.status_code)
        print("Headers:", response.headers)
        print("Body:", response.text)
    except requests.exceptions.RequestException as e:
        logging.error("GET request failed: %s", e)
        print("GET request failed! Check http_requests.log")

def send_post_request():
    url = "https://httpbin.org/post"
    data = {"username": "student", "project": "Application Layer Protocols"}
    try:
        response = requests.post(url, data=data, timeout=5)
        print("\n=== POST Request ===")
        print("Status Code:", response.status_code)
        print("Headers:", response.headers)
        print("Body:", response.text)
    except requests.exceptions.RequestException as e:
        logging.error("POST request failed: %s", e)
        print("POST request failed! Check http_requests.log")

if __name__ == "__main__":
    send_get_request()
    send_post_request()
