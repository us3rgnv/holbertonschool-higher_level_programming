# Python Basic Serialization

This repository contains a simple Python module to serialize Python dictionaries to JSON files and deserialize JSON files back to Python dictionaries.

## Files

- `task_00_basic_serialization.py`: Module implementing serialization and deserialization functions.

## Usage

```python
from task_00_basic_serialization import serialize_and_save_to_file, load_and_deserialize

# Example dictionary
data_to_serialize = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

# Serialize and save to file
serialize_and_save_to_file(data_to_serialize, 'data.json')
print("Data serialized and saved to 'data.json'.")

# Load and deserialize
deserialized_data = load_and_deserialize('data.json')
print("Deserialized Data:")
print(deserialized_data)
