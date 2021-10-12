from typing import Dict, Tuple, List

import networkx as nx

from src.input.collect_number_of_hangars import get_number_of_hangars_to_visit
from src.input.collect_path import collect_path
from src.input.collect_tolls import collect_tolls

if __name__ == '__main__':
    tolls = collect_tolls()
    hangars_number_to_visit = get_number_of_hangars_to_visit()
    path = collect_path(hangars_number_to_visit)

    G = nx.Graph()

    edges: List[Tuple[str, str, Dict[str]]] = [('E', 'F', tolls['Red']), ('H', 'I', tolls['Red']),
                                               ('F', 'C', tolls['Red']), ('N', 'O', tolls['Red']),
                                               ('O', 'D', tolls['Red']), ('D', 'L', tolls['Red']),
                                               ('N', 'J', tolls['Red']),
                                               ('G', 'H', tolls['Green']), ('A', 'H', tolls['Green']),
                                               ('I', 'L', tolls['Green']), ('J', 'K', tolls['Green']),
                                               ('J', 'M', tolls['Green']), ('C', 'M', tolls['Green']),
                                               ('G', 'J', tolls['Green']),
                                               ('A', 'E', tolls['Blue']), ('F', 'G', tolls['Blue']),
                                               ('H', 'J', tolls['Blue']), ('B', 'I', tolls['Blue']),
                                               ('I', 'K', tolls['Blue']), ('M', 'N', tolls['Blue']),
                                               ('K', 'O', tolls['Blue'])]

    G.add_weighted_edges_from(edges)
    total_cost: float = 0

    for i in range(len(path) - 1):
        source = path[i]
        destination = path[i + 1]
        cost: float = round(nx.dijkstra_path_length(G, source, destination), 1)
        # print("Toll of travel from {} to {}: {}".format(src, dest, cost))

        total_cost += cost

    # print("Total cost of travel path: {} is {}".format(path_to_string(path), round(total_cost, 1)))
    print(total_cost)
