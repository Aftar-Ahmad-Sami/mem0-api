import requests

# Define the API endpoint URL
url = "http://127.0.0.1:8000/api/search"  # Replace with your API endpoint

# Define the payload data to be sent in the POST request
payload = {
    "query": "What is my name?",  # Replace with the query text
    "user_id": "aftar_ahmad"  # Ensure user_id is included in the request body
}

# Optionally, define headers if required (e.g., for authentication)
headers = {
    "Content-Type": "application/json",  # Ensure the Content-Type is correct
}

# Send the POST request with the payload data
response = requests.post(url, json=payload, headers=headers)

# Print the response status code
print(f"Status Code: {response.status_code}")

# Print the response JSON content
try:
    response_data = response.json()
    print("Response JSON:", response_data)
except ValueError:
    print("Response is not in JSON format:", response.text)

# import os
# os.environ['OPENAI_API'] = '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'
