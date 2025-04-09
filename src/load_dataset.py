import json

def load_dataset(dataset):
    with open(dataset, 'r') as file:
        return json.load(file)
