import json

my_details = {
    'name': 'John Doe',
    'age': 29
}

with open('personal.json', 'w') as json_file:
    json.dump(my_details, json_file)