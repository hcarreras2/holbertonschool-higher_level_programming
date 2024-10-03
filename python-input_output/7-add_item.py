#!/usr/bin/python3

"""Write a script that adds all arguments to a Python list,
and then save them to a file"""

import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if os.path.exists("add_item.json"):
        items = load_from_json_file("add_item.json")
else:
    items = []
    items.extend(sys.argv[1:])
    save_to_json_file(items, "add_item.json")  # save to file
