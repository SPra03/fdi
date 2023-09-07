import requests

# Define the URL for your FastAPI endpoint
url = "http://localhost:8000/process_and_download"

# Define the dataset_name as a query parameter
params = {
    "dataset_name": "odc-sci_851"
}

# Send the POST request with query parameters
response = requests.post(url, params=params)

# Check the response status code
if response.status_code == 200:
    print("Request was successful.")
    # You can also print the response content if needed
    # print(response.text)
else:
    print(f"Request failed with status code {response.status_code}:")
    print(response.text)
