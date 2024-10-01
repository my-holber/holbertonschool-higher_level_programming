#!/usr/bin/python3
"""7. Load, add, save"""


import sys
import os


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"
'''Загружаем существующие элементы или создаем пустой список'''
if os.path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []
arguments = sys.argv[1:]
items.extend(arguments)
save_to_json_file(items, filename)
