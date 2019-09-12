from typing import Set, Tuple, List


class Graf:
    def __init__(self):
        self.nodes: Set[str] = set()
        self.edges: Set[Tuple[str, str]] = set()

    def add_vertex(self, new_vertex):
        self.nodes.add(new_vertex)

    def add_edge(self, new_edge):
        for i in new_edge:
            if (len(self.nodes.intersection(i))) == 0:
                return
        self.edges.add(new_edge)

    def find_neighbours(self, node: str) -> Set[str]:
        neighbours = set()
        for edge in self.edges:
            if edge[0] == node:
                neighbours.add(edge[1])
            if edge[1] == node:
                neighbours.add(edge[0])
        return neighbours

    def breadth_first_walk(self, start_node: str) -> List[str]:
        visited = set()
        queue_to_visit = set(start_node)

        while queue_to_visit:
            visiting = queue_to_visit.pop()
            neighbours = self.find_neighbours(visiting)
            visited.add(visiting)
            for node in neighbours:
                if node not in visited:
                    queue_to_visit.add(node)
        return visited

    def depth_first_walk(self, start_node: str, visited=set()) -> Set[str]:
        visited.add(start_node)
        for neighbour in self.find_neighbours(start_node):
            if neighbour not in visited:
                self.depth_first_walk(neighbour,visited)
        return visited


    pass


graf = Graf()

graf.add_vertex("1")
graf.add_vertex("2")
graf.add_vertex("1")
graf.add_vertex("3")
graf.add_vertex("4")
graf.add_vertex("5")
graf.add_vertex("6")
graf.add_edge(("1", "2"))
graf.add_edge(("2", "3"))
graf.add_edge(("1", "4"))
graf.add_edge(("3", "5"))
graf.add_edge(("5", "6"))

print(graf.nodes)
print(graf.edges)
print(graf.find_neighbours("2"))
print("s")

print(graf.depth_first_walk("2"))
