from Data_Structures.graph.graph import Graph

def business_trip(graph, cities):
    all_verticies = graph.get_nodes()
    vertex_map = {}
    cost = 0
    for vertex in all_verticies:
        vertex_map[vertex.value] = vertex

    for i in range(len(cities) - 1):
        city_1 = cities[i]
        city_2 = cities[i + 1]
        vetrex_1 = vertex_map[city_1]
        vetrex_2 = vertex_map[city_2]

        city_1_neighbors = graph.get_neighbors(vetrex_1)

        is_path = False

        for edge in city_1_neighbors:
            if edge.vertex == vetrex_2:
                cost += edge.weight
                is_path = True
        if not is_path:
            return False,cost

    return True,cost




if __name__ == "__main__":
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
