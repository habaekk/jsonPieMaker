import json



# create a list of dictionaries
my_data = [
    {"name": "John", "age": 30},
    {"name": "Jane", "age": 25},
    {"name": "Bob", "age": 40}
]

# sorted_data = sorted(my_data, key=lambda x: x["age"])

# convert the data to JSON
json_data = json.dumps(my_data)

# save the JSON to a file
with open("my_file.json", "w") as f:
    f.write(json_data)
