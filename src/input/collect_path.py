from typing import List

from src.settings import graph_nodes


def collect_path(size: int) -> List[str]:
    """
    Function returns the desired path based on entered stops/hangars
    :param size: The number of stops / hangars to visit
    :return: A complete path, graph vertices are represented by capital letters
    """
    path = input("Enter hangars: ").split()
    while not (is_path_length_ok(path, size) and is_path_nodes_ok(path)):
        print("Error! Wrong input")
        path = input("Enter hangars: ").split()

    return path


def is_path_length_ok(path: List[str], size) -> bool:
    """
    Function check if entered path length is correct
    :param path: entered path
    :param size: desired size of path
    """
    if len(path) != size:
        return False

    return True


def is_path_nodes_ok(path: List[str]) -> bool:
    """
    Function check if entered path nodes are correct
    :param path: entered path
    """
    A_code = ord(graph_nodes[0])
    O_code = ord(graph_nodes[-1])
    for node in path:
        if not A_code <= ord(node) <= O_code:
            return False

    return True
