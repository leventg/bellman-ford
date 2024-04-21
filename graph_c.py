import collections

class Graph_C:

    def __init__(self):
        self.graph = collections.defaultdict(dict)

    def add_edge(self, u, v, weight):
        self.graph[u][v] = float('inf') if weight is None else weight

    def bellman_ford(self, source):
        d, p = {}, {}
        for node in self.graph:
            d[node] = float('inf')
            p[node] = None
        d[source] = 0

        for _ in range(len(self.graph) - 1):
            relaxation_occurred = False
            for node in self.graph:
                for neighbour in self.graph[node]:
                    if d[neighbour] > d[node] + self.graph[node][neighbour]:
                        d[neighbour] = d[node] + self.graph[node][neighbour]
                        p[neighbour] = node
                        relaxation_occurred = True
            if not relaxation_occurred:
                break

        for u in self.graph:
            for v in self.graph[u]:
                if d[v] < d[u] + self.graph[u][v]:
                    return self.__retrace_negative_loop(p, source)
        return None

    def __retrace_negative_loop(self, p, start):
        arbitrage_loop = [start]
        next_node = start
        while next_node is not None:
            next_node = p.get(next_node)
            if next_node is not None and next_node not in arbitrage_loop:
                arbitrage_loop.append(next_node)
            elif next_node is not None:
                arbitrage_loop.append(next_node)
                arbitrage_loop = arbitrage_loop[arbitrage_loop.index(next_node):]
                return arbitrage_loop
        return None

    def get_nodes(self):
        return self.graph.keys()

    def print_graph(self):
        print("Graph:")
        for u in self.graph:
            print(u, ":", self.graph[u])
        print("end graph")
