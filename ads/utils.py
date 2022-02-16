import csv
import os
from typing import List, Dict

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = BASE_DIR.replace('ads', 'datasets')
ADS_PATH = os.path.join(DATA_DIR, 'ads.csv')
CATEGORIES_PATH = os.path.join(DATA_DIR, 'categories.csv')


def cvs_to_dict(file_path: str) -> List[Dict[str, str]]:
    csvfile = open(file_path, 'r', encoding='UTF-8')
    field_names = csvfile.readline().strip().split(',')
    reader = csv.DictReader(csvfile, field_names)
    return [r for r in reader]


categories_cvs_data = cvs_to_dict(CATEGORIES_PATH)
ads_cvs_data = cvs_to_dict(ADS_PATH)
