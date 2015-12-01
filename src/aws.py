import json

def read(filename):

    with open(filename, 'rb') as json_file:
        parsed = json.load(json_file)
        return parsed

