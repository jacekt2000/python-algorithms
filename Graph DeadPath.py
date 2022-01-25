from typing import Any, Optional, List, Dict


class Vertex:
    def __init__(self, data, index):
        self.data = data
        self.index = index


class Edge:
    source: Vertex
    destination: Vertex

    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


class Digraph:
    connection: Dict[Vertex, List[Edge]]

    def __init__(self) -> None:
        self.connection = {}

    def create_vertex(self, data: Any) -> Vertex:
        temp: Vertex = Vertex(data, len(self.connection))
        self.connection[temp] = []
        return temp

    def add_directed_edge(self, source, destination):
        new_edge = Edge(source, destination)
        self.connection[source].append(new_edge)


def dead_path(graph: Digraph, start: Vertex, path: List[Vertex], visited: List[Vertex]) -> Optional[List[Vertex]]:
    visited.append(start)
    for edge in graph.connection[start]:
        if edge.destination in visited:
            path.append(edge.destination)
        elif edge.destination not in visited:
            path.append(edge.destination)
            return dead_path(graph, edge.destination, path, visited)


def dfs_path(graph: Digraph, start: Vertex) -> Optional[List[Vertex]]:
    visited = []
    path = []
    path.append(start)
    return dead_path(graph, start, path, visited), path, start


def print_graph(graph: dfs_path) -> List[Vertex]:
    for node in graph[1]:
        print(node.data, end=" -> ")


def is_directed(graph: dfs_path) -> bool:
    start = graph[2]
    counter = graph[1].count(start)
    if counter == 2:
        print_graph(graph)
        return True
    print(None)


if __name__ == "__main__":
    graph = Digraph()

    a = graph.create_vertex("A")
    b = graph.create_vertex("B")
    c = graph.create_vertex("C")

    d = graph.create_vertex("D")
    e = graph.create_vertex("E")
    f = graph.create_vertex("F")

    graph.add_directed_edge(a, b)
    graph.add_directed_edge(b, c)
    graph.add_directed_edge(c, d)
    graph.add_directed_edge(d, e)
    graph.add_directed_edge(e, f)
    graph.add_directed_edge(f, a)


    graph1 = Digraph()

    a1 = graph1.create_vertex("A")
    b1 = graph1.create_vertex("B")
    c1 = graph1.create_vertex("C")
    d1 = graph1.create_vertex("D")
    e1 = graph1.create_vertex("E")

    graph1.add_directed_edge(a1, b1)
    graph1.add_directed_edge(b1, c1)
    graph1.add_directed_edge(c1, d1)
    graph1.add_directed_edge(d1, e1)
    graph1.add_directed_edge(e1, c1)

    dfs_path1 = dfs_path(graph1, c1)

    graph2 = Digraph()

    a2 = graph2.create_vertex("A")
    b2 = graph2.create_vertex("B")
    c2 = graph2.create_vertex("C")
    d2 = graph2.create_vertex("D")
    e2 = graph2.create_vertex("E")

    graph2.add_directed_edge(a2, b2)
    graph2.add_directed_edge(b2, c2)
    graph2.add_directed_edge(c2, d2)
    graph2.add_directed_edge(d2, e2)
    graph2.add_directed_edge(e2, c2)

    dfs_path2 = dfs_path(graph2, a2)
    is_directed(dfs_path2) # -> None
    print('\n')
    dfs_path1 = dfs_path(graph1, c1)
    is_directed(dfs_path1) # -> C-C
    print('\n')
    dfs_path = dfs_path(graph, a)
    is_directed(dfs_path) # -> A-A
