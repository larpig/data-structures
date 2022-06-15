class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.adj_list = self.edges_2_adjacency_list(edges)

    @staticmethod
    def edges_2_adjacency_list(edges):
        adj_list = {}
        for start_node, end_node in edges:
            if start_node not in adj_list:
                adj_list[start_node] = [end_node]
            else:
                adj_list[start_node].append(end_node)
        return adj_list

    def get_paths(self, start, end, path=[]):

        path = path + [start]
        #path.append(start)

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
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("Dubai", "Toronto"),
        ("New York", "Toronto"),
    ]

    print(f"Adjacency list representation:", Graph.edges_2_adjacency_list(routes))

    route_graph = Graph(routes)

    start = "Mumbai"
    end = "Dubai"
    print(f"All paths between {start} and {end}: ", route_graph.get_paths(start, end))
    #print(f"Shortest path between {start} and {end}: ", route_graph.get_shortest_path(start, end))