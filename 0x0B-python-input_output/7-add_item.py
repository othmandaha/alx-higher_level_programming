#!/usr/bin/python3
"""adding all argument to a list saved to a file."""
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


arguments = sys.argv

try:
    json_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    json_list = []
for arg in arguments[1:]:
    json_list.append(arg)

save_to_json_file(json_list, "add_item.json")
