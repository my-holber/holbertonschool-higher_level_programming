import csv
import json


def convert_csv_to_json(file_name):
    try:
        _list = []
        with open(file_name, 'r') as f:
            data = csv.DictReader(f, delimiter=',')
            for row in data:
                _list.append(row)



        with open('data.json', 'w') as f:
            json.dump(_list, f)

    except Exception:
         return False
    return True

