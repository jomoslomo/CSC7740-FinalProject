import json

# Function to load and print the structure of a JSON file
def inspect_json(file_path):
    try:
        # Open and load the JSON file
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        # Pretty print the JSON structure with indentation
        print("JSON structure:")
        print(json.dumps(data, indent=4, ensure_ascii=False))

        # Provide additional useful information
        print("\n--- Additional Info ---")
        
        # Check if the top-level object is a list or dictionary
        if isinstance(data, list):
            print(f"Number of objects (items in list): {len(data)}")
        elif isinstance(data, dict):
            print(f"Top-level keys: {list(data.keys())}")
        
        # Count nested dictionaries and lists
        total_objects, total_lists = count_objects_and_lists(data)
        print(f"Total dictionaries (objects): {total_objects}")
        print(f"Total lists (arrays): {total_lists}")

        # Find unique device IDs
        unique_device_ids = find_unique_device_ids(data)
        print(f"Number of unique 'device_id': {len(unique_device_ids)}")

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except json.JSONDecodeError:
        print(f"Error decoding JSON in file '{file_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Helper function to count dictionaries and lists recursively
def count_objects_and_lists(data):
    object_count = 0
    list_count = 0
    
    if isinstance(data, dict):
        object_count += 1
        for key, value in data.items():
            sub_objects, sub_lists = count_objects_and_lists(value)
            object_count += sub_objects
            list_count += sub_lists
    elif isinstance(data, list):
        list_count += 1
        for item in data:
            sub_objects, sub_lists = count_objects_and_lists(item)
            object_count += sub_objects
            list_count += sub_lists
    
    return object_count, list_count

# Helper function to find unique device IDs
def find_unique_device_ids(data):
    device_ids = set()  # Using a set to store unique device IDs

    def extract_device_ids(item):
        if isinstance(item, dict):
            # If 'device_id' exists, add it to the set
            if 'device_id' in item:
                device_ids.add(item['device_id'])
            # Recurse through dictionary
            for key, value in item.items():
                extract_device_ids(value)
        elif isinstance(item, list):
            # Recurse through list
            for sub_item in item:
                extract_device_ids(sub_item)

    # Start the extraction process
    extract_device_ids(data)

    return device_ids

# Replace 'your_json_file.json' with the path to your JSON file
file_path = 'airbox_latest_data.json'

# Inspect the structure of the given JSON file
inspect_json(file_path)
