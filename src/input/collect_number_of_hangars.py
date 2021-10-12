def get_number_of_hangars_to_visit() -> int:
    """
    Function loads the number of stops/hangars to visit
    """
    nr_of_hangars_to_visit = input().rstrip()

    while not is_number_of_stops_ok(nr_of_hangars_to_visit):
        print('Incorrect value!')
        nr_of_hangars_to_visit = input().rstrip()

    return int(nr_of_hangars_to_visit)


def is_number_of_stops_ok(number_of_stops: str) -> bool:
    """
    The function checks whether the user has entered correct data (e.g. if float type then return False)
    :param number_of_stops: entered value
    """
    if not number_of_stops.isnumeric():
        return False
    return True
