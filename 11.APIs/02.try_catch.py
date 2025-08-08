# in Python, the errors are not built-in like in JS, we need to import them from requests.exceptions
# we have to enable HTTPErrors with .raise_for_status()
import requests
from requests.exceptions import ConnectionError, HTTPError

url = "http://wronghost:3000/albums"
try:
    r = requests.get(url)
    r.raise_for_status()  # Enable raising errors for all error status_codes
    print(r.status_code)
except ConnectionError as conn_err:
    print(f"Connection Error! {conn_err}.")
except HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
