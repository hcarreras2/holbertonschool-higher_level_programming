#!/usr/bin/python3

import csv

import json

"""A function that takes CSV filename
as parameter and writes the JSON data
to data.json"""


def convert_csv_to_json(csv_filename):
    try:
        data = []
        with open(csv_filename, 'r') as csvf:
            csv_reader = csv.DictReader(csvf)
            for row in csv_reader:
                data.append(dict(row))
        with open('data.json', 'w') as jsonf:
            json.dump(data, jsonf, indent=4)
        return True
    except FileNotFoundError:
        return False
    except Exception as e:
        return False
