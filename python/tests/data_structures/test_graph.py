# Node can be successfully added to the graph
# An edge can be successfully added to the graph
# A collection of all nodes can be properly retrieved from the graph
# All appropriate neighbors can be retrieved from the graph
# Neighbors are returned with the weight between nodes included
# The proper size is returned, representing the number of nodes in the graph
# A graph with only one node and edge can be properly returned
# An empty graph properly returns null

import pytest
from Data_Structures.graph.graph import Graph , Vertex

def test_add_node(test_graph1):
    assert test_graph1.add_node('1').value == '1'

def test_size_empty(test_graph1):
    assert test_graph1.size() == 0


def test_add_edge():
    graph = Graph()
    node1 = graph.add_node('a')
    node2 = graph.add_node('b')
    test1 = graph.add_edge(node1,node1)
    expected = ['a',0]
    actual = [test1.vertex.value,test1.weight]
    assert actual == expected

def  test_get_nodes(test_graph2):
    nodes = test_graph2.get_nodes()
    actual = [node.value for node in nodes]
    expected = ['a', 'b', 'c', 'd']
    assert actual == expected


def test_get_neighbors(test_graph2):
    expected = ['b',['c', 0]]
    nodes = test_graph2.get_nodes()
    for node in nodes:
        if node.value == 'b':
            node3 = node
    neighbors = test_graph2.get_neighbors(node3)
    actual = [node3.value]
    for edge in neighbors:
        actual += [[edge.vertex.value,edge.weight]]
    assert actual == expected


def test_empty_graph():
    graph = Graph()
    actual = graph.get_nodes()
    assert not actual


@pytest.fixture
def test_graph1():
    g1 = Graph()
    return g1


@pytest.fixture
def test_graph2():
    g2 = Graph()
    node1 = g2.add_node('a')
    node2 = g2.add_node('b')
    node3 = g2.add_node('c')
    node4 = g2.add_node('d')

    g2.add_edge(node1,node3)
    g2.add_edge(node1,node4)
    g2.add_edge(node2,node3)

    return g2
