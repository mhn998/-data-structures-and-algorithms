from Data_Structures.graph.graph import Graph
from code_challenges.graph_business_trip.graph_business_trip import business_trip

import pytest

def test_is_reachable():
    pass



@pytest.fixture
def test_graph_path():
    g = Graph()
    node1 = g.add_node('Pandora')
    node2 = g.add_node('Arendelle')
    node3 = g.add_node('Metroville')
    node4 = g.add_node('Monstropolis')
    node5 = g.add_node('Narnia')
    node6 = g.add_node('Naboo')
    g.add_edge(node1, node2, 150)
    g.add_edge(node2, node3, 99)
    g.add_edge(node1, node3, 82)
    g.add_edge(node2, node4, 42)
    g.add_edge(node3, node4, 105)
    g.add_edge(node3, node5, 37)
    g.add_edge(node3, node6, 26)
    g.add_edge(node4, node6, 73)
    g.add_edge(node5, node6, 250)
    business_trip(g,['Metroville','Pandora'])
    business_trip(g,['Arendelle','Monstropolis','Naboo'])
    business_trip(g,['Naboo','Pandora'])
    business_trip(g,['Narnia','Arendelle','Naboo'])
