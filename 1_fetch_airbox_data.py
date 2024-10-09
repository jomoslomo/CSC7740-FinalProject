import requests
import os

# Define the URL and output file path
url = 'https://pm25.lass-net.org/API-1.0.0/project/airbox/latest/'
output_dir = 'data'
output_file = os.path.join(output_dir, 'airbox_latest_data.json')

try:
    # Ensure the 'data' directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Send a GET request to the API
    response = requests.get(url, headers={'accept': 'application/json'})

    # Check if the request was successful
    if response.status_code == 200:
        # Save the response content to the file in the 'data' directory
        with open(output_file, 'w') as file:
            file.write(response.text)
        print(f"Data successfully saved to {output_file}")
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

except Exception as e:
    print(f"An error occurred: {e}")
