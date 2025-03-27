import json

# Sample data (like an order)
data = {"item": "Coffee", "timestamp": "2025-03-27 10:30:00"}

# Save to JSON
with open("example.json", "w") as file:
    json.dump(data, file, indent=4)

# Load from JSON
with open("example.json", "r") as file:
    loaded_data = json.load(file)

print(loaded_data)  # Output: {'item': 'Coffee', 'timestamp': '2025-03-27 10:30:00'}
