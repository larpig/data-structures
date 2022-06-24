class Graph:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges
        self.adj_list = self.edges_2_adjacency_list(nodes, edges)

    @staticmethod
    def edges_2_adjacency_list(nodes, edges):

        adj_list = {}
        for node in nodes:
            adj_list[node] = []

        for start_node, end_node in edges:
            adj_list[start_node].append(end_node)

        return adj_list

    def add_node(self, node):
        self.nodes.append(node)
        self.adj_list = self.edges_2_adjacency_list(self.nodes, self.edges)
        return True

    def add_edge(self, start, end):
        self.edges.append((start, end))
        self.adj_list = self.edges_2_adjacency_list(self.nodes, self.edges)
        return True

    def get_paths(self, start, end, path=[]):

        path = path + [start]

        if start == end:
            return [path]

        if start not in self.adj_list:
            return []

        paths = []
        for node in self.adj_list[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)

        return paths


if __name__ == '__main__':
    cities = ["Mumbai", "Paris", "Dubai", "New York", "Toronto", ]

    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("Dubai", "Toronto"),
        ("New York", "Toronto"),
    ]

    print(f"Adjacency list representation:", Graph.edges_2_adjacency_list(cities, routes))

    route_graph = Graph(nodes=cities, edges=routes)

    route_graph.add_node('São Paulo')
    print(f"All nodes after add São Paulo:", route_graph.nodes)

    route_graph.add_edge('São Paulo', "New York")
    print(f"All edges after add (São Paulo, New York):", route_graph.edges)

    start = "Mumbai"
    end = "Dubai"
    print(f"All paths between {start} and {end}: ", route_graph.get_paths(start, end))
    # print(f"Shortest path between {start} and {end}: ", route_graph.get_shortest_path(start, end))