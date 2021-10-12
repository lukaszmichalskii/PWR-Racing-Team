from src.input.collect_number_of_hangars import get_number_of_hangars_to_visit
from src.input.collect_path import collect_path
from src.input.collect_tolls import collect_tolls

if __name__ == '__main__':
    tolls = collect_tolls()
    hangars_number_to_visit = get_number_of_hangars_to_visit()
    path = collect_path(hangars_number_to_visit)
