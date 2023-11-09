import requests
import sys

def check_health(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
        print(f"Health check passed for {url}")
    except requests.exceptions.RequestException as e:
        print(f"Health check failed for {url}: {e}")
        sys.exit(1)

if __name__ == "__main__":
    health_check_url = "http://localhost:8000/"
    check_health(health_check_url)



