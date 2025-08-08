# Key Takeaways:
# - Use resp.json() to parse JSON response bodies into native Python dicts/lists.
# - The json= parameter in requests auto-sets Content-Type: application/json for request payloads.
# - Using data= sends form-encoded data (application/x-www-form-urlencoded) instead.
# - Include Accept: application/json to explicitly request JSON if an API supports multiple formats; requests lib defaults to Accept: */*.
# - Inspect resp.request.headers and resp.request.body to debug outgoing requests.
# - Use json.dumps()/json.loads() to mirror JavaScript’s JSON.stringify()/JSON.parse().

import requests

API_KEY = "reqres-free-v1"
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    # 'Accept': 'application/json'    # (client) request header; tells the server to return JSON (requests lib defaults to Accept: */*)
    # If an API really does support multiple formats (JSON, XML, HTML, etc.), then you’d use Accept: application/json (or application/xml) to pick one. But for JSON-only APIs, it’s effectively a no-op—JSON is the default.
    # 'Content-Type': 'application/json'  # (client) request header; indicates the request body format (requests sets this automatically when using json=...)
}
BASE_URL = "https://reqres.in/api/users"

# .json() parses the stringified JSON response body into a Python dictionary
# similar idea in JS
# fetch(url)
#   .then(res => res.json())   // parses JSON text into a JS object/array
#   .then(data => console.log(data));

# CREATE
new_user = {"name": "murat", "job": "tester"}
resp = requests.post(BASE_URL, json=new_user, headers=HEADERS)
print("POST →", resp.status_code, resp.json())

# READ (single)
resp = requests.get(f"{BASE_URL}/2", headers=HEADERS)
print("GET 2 →", resp.status_code, resp.json())

# READ (list/page) (public endpoint)
resp = requests.get(BASE_URL, params={"page": 2})
print("GET page 2 →", resp.status_code, resp.json())

# UPDATE (full replace)
update_user = {"name": "murat ozcan", "job": "senior tester"}
resp = requests.put(f"{BASE_URL}/2", json=update_user, headers=HEADERS)
print("PUT 2 →", resp.status_code, resp.json())

# UPDATE (partial)
patch_user = {"job": "lead tester"}
resp = requests.patch(f"{BASE_URL}/2", json=patch_user, headers=HEADERS)
print("PATCH 2 →", resp.status_code, resp.json())

# DELETE
resp = requests.delete(f"{BASE_URL}/2", headers=HEADERS)
print("DELETE 2 →", resp.status_code)  # should be 204 No Content


######
# In modern REST-style APIs you’ll almost always want to use JSON, but you can also send raw data
# Using data= will send application/x-www-form-urlencoded by default name=murat&job=tester&foo=bar%20baz
# Pairs are joined with &, and each key is separated from its value by =.
# Keys and values are percent-escaped (so spaces become %20, & and = get escaped, etc.)
# On the receiving end, a web framework (or requests when you use data=…) parses that back into a dictionary/object or map of strings.
resp = requests.post(BASE_URL, data=new_user, headers=HEADERS)
# Let’s inspect what actually went out
print("Request headers →", resp.request.headers)  # application/x-www-form-urlencoded
print("Request body    →", resp.request.body)  # name=murat&job=tester
print("Response status →", resp.status_code)  # 201
print("Response content type →", resp.headers["Content-Type"])  # application/json
print("Response accept →", resp.headers["accept"])  # application/json
print(
    "Response body   →", resp.text
)  # {"name":"murat","job":"tester","id":"608","createdAt":"2025-07-14T13:47:56.914Z"} gives it as JSON string
print(
    "Response body   →", resp.json()
)  # {'name': 'murat', 'job': 'tester', 'id': '608', 'createdAt': '2025-07-14T13:47:56.914Z'} gives it as Python dict/object


#####

import json

py_obj = {"name": "murat", "age": 35}

# JS equivalent: JSON.stringify(obj) → str
json_str = json.dumps(py_obj)
print(json_str)  # '{"name": "murat", "age": 35}'

# JS equivalent: JSON.parse(str) → obj
parsed = json.loads(json_str)
print(parsed)  # {'name': 'murat', 'age': 35}
print(type(parsed))  # <class 'dict'>
