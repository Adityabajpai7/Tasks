import requests

# Make a GET request with basic authentication
r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))

# Print the status code of the response
print(r.status_code)  # Output: 200

# Print the content type from the response headers
print(r.headers['content-type'])  # Output: 'application/json; charset=utf8'

# Print the encoding used for the response
print(r.encoding)  # Output: 'utf-8'

# Print the response text
print(r.text)  # Output: '{"authenticated": true, ...'

# Print the response JSON
print(r.json())  # Output: {'authenticated': True, ...}
