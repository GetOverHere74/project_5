from utils.func import loading_file, filtered_list, sort_by_date, date_format, get_card_number, get_summ, load_main
import os
from config import ROOT_DIR

def test_loading_file():
    test_path = os.path.join(ROOT_DIR, 'tests', 'test_operations.json')
    assert loading_file(test_path) == []


