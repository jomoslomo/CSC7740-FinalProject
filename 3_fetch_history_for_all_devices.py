import json
from fetch_device_history import fetch_device_history
import os
import concurrent.futures

# Path to the unique device IDs JSON file
device_ids_file = os.path.join('data', 'unique_device_ids.json')

# Function to fetch history for a device, this will be called concurrently
def fetch_device_history_concurrent(device_id):
    print(f"Fetching history for device ID: {device_id}")
    fetch_device_history(device_id)

# Function to read unique device IDs and fetch history for each using multithreading
def fetch_history_for_all_devices_concurrently():
    try:
        # Open and load the unique device IDs JSON file
        with open(device_ids_file, 'r', encoding='utf-8') as file:
            device_ids = json.load(file)

        # Check if the list is not empty
        if not device_ids:
            print("No device IDs found in the file.")
            return

        # Using ThreadPoolExecutor to run fetch_device_history_concurrent in parallel
        with concurrent.futures.ThreadPoolExecutor() as executor:
            # Map device_ids to the fetch_device_history_concurrent function
            executor.map(fetch_device_history_concurrent, device_ids)

    except FileNotFoundError:
        print(f"File '{device_ids_file}' not found.")
    except json.JSONDecodeError:
        print(f"Error decoding JSON from file '{device_ids_file}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
if __name__ == "__main__":
    fetch_history_for_all_devices_concurrently()
