import requests
import json
import os

# Function to fetch device history based on device ID and save to a JSON file
def fetch_device_history(device_id):
    # Define the base URL for the API
    base_url = f'https://pm25.lass-net.org/API-1.0.0/device/{device_id}/history/'
    
    # Define the output directory and ensure it exists
    output_dir = os.path.join('data', 'device_history')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    try:
        # Send a GET request to the API with the provided device ID
        response = requests.get(base_url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Get the JSON response from the API
            data = response.json()
            print(f"History for device ID {device_id}:")
            print(data)
            
            # Save the JSON data to a file in the 'data/device_history' folder
            file_name = os.path.join(output_dir, f"device_{device_id}_history.json")
            with open(file_name, 'w', encoding='utf-8') as json_file:
                json.dump(data, json_file, indent=4, ensure_ascii=False)
            print(f"History data saved to {file_name}")
            
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# The following block ensures that this part of the code only runs if this script is executed directly
if __name__ == "__main__":
    # Prompt the user for the device ID
    device_id = input("Enter the device ID to fetch history: ")

    # Fetch the history for the provided device ID and save it to a JSON file
    fetch_device_history(device_id)
