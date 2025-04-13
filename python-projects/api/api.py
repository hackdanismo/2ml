# Import the package/module needed. This is importing the requests package
import requests

# Define the API endpoint
url = "https://jsonplaceholder.typicode.com/posts"

# Make a GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON data
    data = response.json()
    # Print the first three items
    print(data[:3])
else:
    print(f"Failed to retrieve data: {response.status_code}")