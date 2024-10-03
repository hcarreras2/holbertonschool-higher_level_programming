#!/usr/bin/python3

"""Write a script that adds all arguments to a Python list,
and then save them to a file"""

import sys
import os
from file_manager import save_to_json_file, load_from_json_file


def add_item():
    if os.path.exists("add_item.json"):
        items = load_from_json_file("add_item.json")
    else:
        items = []

    for arg in sys.argv[1:]:
        items.append(arg)

    save_to_json_file("add_item.json", items)


if __name__ == "__main__":
    add_item()
