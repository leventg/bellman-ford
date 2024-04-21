import pytest
from graph_c import Graph_C  

def test_add_edge():
    graph = Graph_C()

    graph.add_edge('A', 'B', 6)
    graph.add_edge('B', 'A', 10)  # Bidirectional edge
    assert graph.graph == {'A': {'B': 6}, 'B': {'A': 10}} 

def test_bellman_ford_simple():
    graph = Graph_C()

    graph.add_edge('A', 'B', 6)
    graph.add_edge('B', 'A', 10)  # Bidirectional
    graph.add_edge('A', 'C', 2)
    graph.add_edge('C', 'A', 5)  # Bidirectional
    result = graph.bellman_ford('A')
    assert result is None  # No negative cycles

def test_bellman_ford_negative_cycle():
    graph = Graph_C()

    graph.add_edge('A', 'B', 6)
    graph.add_edge('B', 'A', 10)
    graph.add_edge('A', 'C', 2)
    graph.add_edge('C', 'A', 5)
    graph.add_edge('C', 'B', -7)  # Creates a negative cycle
    graph.add_edge('B', 'C', 3)  # Bidirectional
    result = graph.bellman_ford('B')
    assert result == ['B', 'C', 'B'] 
