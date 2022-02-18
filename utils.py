import csv
import json
import os
from typing import List

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'datasets')
FIXTURE_DIR = os.path.join(BASE_DIR, 'fixtures')


def get_cvs_dict(cvs_data_path: str) -> List[str]:
    with open(cvs_data_path, 'r', encoding='UTF-8') as csvfile:
        field_names = csvfile.readline().strip().split(',')
        return [r for r in csv.DictReader(csvfile, field_names)]


def get_py_dict(cvslist: List[str], name: str):
    print(cvslist)
    exit()
    res = []
    for key, item in enumerate(cvslist):
        res.append({
            "pk": key,
            "model": f"ads.{name}",
            "fields": item
                })
    return res


def create_fixtures(data_dir: str, fixture_dir: str, name: str):
    cvs_data_path = os.path.join(data_dir, f'{name}.csv')
    cvs_dict = get_cvs_dict(cvs_data_path)
    data = get_py_dict(cvs_dict, name)
    json_data_path = os.path.join(fixture_dir, f'{name}.json')

    with open(json_data_path, 'w', encoding='UTF-8') as jsonfile:
        json.dump(data, jsonfile, sort_keys=False, indent=4, separators=(',', ': '), ensure_ascii=False)

    jsonfile.close()


NAMES = ('ads', 'categories')
for name in NAMES:
    create_fixtures(DATA_DIR, FIXTURE_DIR, name)
