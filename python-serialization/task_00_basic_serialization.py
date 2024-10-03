import json

def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a JSON file.

    Args:
        data (dict): The Python dictionary to be serialized.
        filename (str): The name of the file to save the serialized data to.

    Returns:
        None
    """
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def load_and_deserialize(filename):
    """
    Load and deserialize data from a JSON file.

    Args:
        filename (str): The name of the file to load the serialized data from.

    Returns:
        dict: The deserialized Python dictionary.
    """
    with open(filename, 'r') as f:
        data = json.load(f)
    return data
