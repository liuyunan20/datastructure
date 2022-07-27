"""
class DirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""

class Solution:
    """
    @param graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort_tle(self, graph):
        # write your code here
        result = []
        node_pos = {}
        while graph:
            current = graph.pop(0)
            print(current.label)
            if current in node_pos:
                n = node_pos[current]
                print("n", n, current.label)
                result[n] = None
            result.append(current)
            node_pos[current] = len(result) - 1
            graph.extend(current.neighbors)
        return [x for x in result if x is not None]
