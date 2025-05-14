# Define a dictionary
my_dict = {
    "name": "Kyriakos",
    "age": 36,
    "city": "Montreal"
}

# Extract keys into a set
key_set = set(my_dict.keys())

# Check if a specific key exists
key_to_check = "age"

if key_to_check in key_set:
    print(f"'{key_to_check}' exists in the dictionary keys.")
else:
    print(f"'{key_to_check}' does NOT exist in the dictionary keys.")