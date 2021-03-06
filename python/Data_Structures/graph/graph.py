from collections import deque
from Data_Structures.stacks_and_queues.stacks_and_queues import Stack

class Vertex:
    def __init__(self,value):
        self.value = value


class Edge:
    def __init__(self,vertex,weight):
        self.vertex = vertex
        self.weight = weight

class Queue():
    def __init__(self):
        self.dq = deque()

    def enqueue(self,value):
        self.dq.appendleft(value)

    def dequeue(self):
        return self.dq.pop()

    def __len__(self):
        return len(self.dq)

# class Stack():
#     def __init__(self):
#         pass

class Graph:
    def __init__(self):
        self._adjacency_list = {} # how do we want to represent the graph? in a dictionary!

    def add_node(self,value):
        """Adds value to a node and adds the node to a graph"""
        v = Vertex(value)
        # Add to the adjacency_list
        self._adjacency_list[v] = [] # lets choose a list
        return v

    def __str__(self) -> str:
        return self._adjacency_list

    def add_edge(self,start_vertex,end_vertex,weight=0):
        """Adds on an edge to the graph"""
        # We want to prevent this function from  continuing if the start and end doesn't exist in the graph
        if start_vertex not in self._adjacency_list:
            raise KeyError('Start Vertex not found in graph')
        if end_vertex not in self._adjacency_list:
            raise KeyError('End Vertex not found in graph')

        self._adjacency_list[start_vertex].append(Edge(end_vertex, weight=0))
        return self._adjacency_list[start_vertex][0]

    def size(self):
        """Returns the size of our graph(dictionary)"""
        return len(self._adjacency_list)

    def get_nodes(self):
        """Gets all of the nodes in the graph"""

        if len(self._adjacency_list) == 0 :
            return None
        return self._adjacency_list.keys()

    def get_neighbors(self,vertex):
        """Gets all of the neighbors of a vertex"""
        return self._adjacency_list.get(vertex,[])

    def breadth_first_search(self,start_vertex,action=(lambda x:None)):
        queue = Queue()
        visited = set()
        lst = []

        queue.enqueue(start_vertex)
        visited.add(start_vertex)

        while len(queue):
            current_vertex = queue.dequeue()
            lst.append(current_vertex.value)
            neighbors = self.get_neighbors(current_vertex)

            for edge in neighbors:
                neighbor_vertex = edge.vertex

                if neighbor_vertex in visited:
                    continue
                else:
                    visited.add(neighbor_vertex)
                queue.enqueue(neighbor_vertex)

        if start_vertex not in self._adjacency_list:
            return "Start node does not exist"

        if len(lst) == 0:
            return "Empty Graph"
        return lst


    def depth_first_search(self, start_vertex):
        verticies = []
        visited = set()
        stack = Stack()

        stack.push(start_vertex)
        visited.add(start_vertex.value)

        while not stack.isEmpty():
            current_vertex = stack.pop()
            verticies.append(current_vertex.value)
            neighbors = self.get_neighbors(current_vertex)

            for neighbor in neighbors:
                if not neighbor in visited :
                    stack.push(neighbor.vertex)
                    visited.add(neighbor.vertex.value)


        if start_vertex not in self._adjacency_list:
                return "Start node does not exist"

        return visited


if __name__ == '__main__':
    g = Graph()
    node1 = g.add_node('node1')
    node2 = g.add_node('node2')
    g.add_edge(node1,node2)
    print(g.breadth_first_search(node1))
    g2 = Graph()
    node_a= g2.add_node('A')
    node_b= g2.add_node('B')
    node_c= g2.add_node('C')
    node_d= g2.add_node('D')
    node_e= g2.add_node('E')
    node_f= g2.add_node('F')
    node_g= g2.add_node('G')
    node_h= g2.add_node('H')
    g2.add_edge(node_a,node_b)
    g2.add_edge(node_a,node_d)
    g2.add_edge(node_b,node_d)
    g2.add_edge(node_b,node_c)
    g2.add_edge(node_c,node_g)
    g2.add_edge(node_d,node_f)
    g2.add_edge(node_d,node_h)
    g2.add_edge(node_f,node_h)
    g2.add_edge(node_d,node_e)
    print(g2.depth_first_search(node_a))
