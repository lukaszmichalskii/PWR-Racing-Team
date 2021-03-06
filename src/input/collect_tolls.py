from typing import Dict, List

from src.settings import path_types_number


def collect_tolls() -> Dict[str, float]:
    """
    Function read the cost of each path in RGB (red -> green -> blue) order separated by a space
    :return: Dictionary of all charges for each road.
             The key is the type of road and the value is the cost
    """
    paths_types = ['Red', 'Green', 'Blue']

    raw_tolls = input().split()

    while not is_tolls_length_ok(raw_tolls):
        print("Incorrect input! Try again: ", end=' ')
        raw_tolls = input().split()
    else:
        tolls: Dict[str, float] = {paths_types[0]: float(raw_tolls[0]),
                                   paths_types[1]: float(raw_tolls[1]),
                                   paths_types[2]: float(raw_tolls[2])}

    return tolls


def is_tolls_length_ok(tolls: List[str]) -> bool:
    """
    Function check if number of toll is correct
    :param tolls: entered tolls
    """
    if len(tolls) != path_types_number:
        return False

    return True
