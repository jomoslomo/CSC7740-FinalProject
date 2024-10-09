import json
import os

# Function to extract unique device IDs from a local JSON file
def extract_and_save_unique_device_ids(file_path):
    try:
        # Open and load the JSON file
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Initialize a set to store unique device IDs
        unique_device_ids = set()

        # Access the 'feeds' array from the JSON structure
        feeds = data.get('feeds', [])
        
        if not feeds:
            print("No 'feeds' key found or it's empty.")
            return
        
        # Loop through the 'feeds' data and extract 'device_id'
        for record in feeds:
            if isinstance(record, dict):
                device_id = record.get('device_id')
                if device_id:
                    unique_device_ids.add(device_id)
        
        # Convert the set to a list for JSON serialization
        unique_device_ids_list = list(unique_device_ids)

        # Create the 'data' directory if it doesn't exist
        output_dir = "data"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Define the output file path
        output_file_name = os.path.join(output_dir, "unique_device_ids.json")
        
        # Save the unique device IDs to the 'data' directory
        with open(output_file_name, 'w', encoding='utf-8') as json_file:
            json.dump(unique_device_ids_list, json_file, indent=4)

        # Print additional information
        print(f"Unique device IDs saved to {output_file_name}")
        print(f"Total records in 'feeds': {len(feeds)}")
        print(f"Number of unique device IDs: {len(unique_device_ids_list)}")
        print(f"Top-level keys: {list(data.keys())}")

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except json.JSONDecodeError:
        print(f"Error decoding JSON from file '{file_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'airbox_latest_data.json' with the path to your JSON file
file_path = 'data/airbox_latest_data.json'

# Extract and save unique device IDs
extract_and_save_unique_device_ids(file_path)
