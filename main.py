import json

# {"month": "00", "day": "00", "year": "00", "lunDay": "00", "moonPhase": "0"} 
# moonPhase: 1-firstQuarter, 2-fullMoon, 3-lastQuarter, 4-newMoon
for y in (2023):    
    for m in range(1, 13):
        for d in range(1, 32):
            pass
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
