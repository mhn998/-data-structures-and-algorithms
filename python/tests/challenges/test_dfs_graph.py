from Data_Structures.graph.graph import Graph , Vertex

def test_depth_first_1():
    g= Graph()
    node1 = g.add_node('node1')
    node2 = g.add_node('node2')
    node3 = g.add_node('node3')
    node4 = g.add_node('node4')
    g.add_edge(node1,node2)
    g.add_edge(node1,node3)
    g.add_edge(node2,node4)
    actual = g.depth_first_search(node1)
    expected = {'node1', 'node2', 'node3', 'node4'}
    assert actual == expected

def test_depth_first_2():
    g = Graph()
    node1 = g.add_node('1')
    node2 = Vertex('2')
    assert g.depth_first_search(node2) == "Start node does not exist"
