import collections


class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

    def deserialize(self, data):
        # None or ""
        if not data:
            return None
        values = {}
        for star in data.split('#'):
            bfs_order = [
                int(val) if val != '#' else None
                for val in star.split(',')
            ]
            if bfs_order[0] not in values:
                values[bfs_order[0]] = DirectedGraphNode(bfs_order[0])
        for star in data.split('#'):
            bfs_order = [
                int(val) if val != '#' else None
                for val in star.split(',')
            ]
            for nei in bfs_order[1:]:
                values[bfs_order[0]].neighbors.append(values[nei])

        return values.values()

node176 = DirectedGraphNode(1).deserialize("1,2,4#2,3,4#4,5 #3#5")

