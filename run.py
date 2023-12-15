from collections import deque

# graph data structure which represents
# the distinctions
routes_graph = {
    'home': ['bus station', 'train station'],
    'bus station': ['airport', 'underground_target'],
    'train station': ['underground'],
    'airport': [],
    'underground_target': []
}


# search queue integration
search_queue = deque()

search_queue += routes_graph['home']


def is_target(point)->bool:
    return point[-1] == '_target'
