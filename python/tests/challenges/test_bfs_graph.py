from Data_Structures.graph.graph import Graph, Vertex

def test_breadth_fisrt_graph():
    g = Graph()
    node1 = g.add_node('node1')
    node2 = g.add_node('node2')
    g.add_edge(node1,node2)
    assert g.breadth_first_search(node1) == ['node1','node2']

def test_breadth_first_graph():
    g = Graph()
    node1 = g.add_node('a')
    node2 = Vertex('s')
    assert g.breadth_first_search(node2) == "Start node does not exist"
