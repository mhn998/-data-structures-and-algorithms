# Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.

class Node():
    def __init__(self,data, next=None):
        self.data = data  # Assign data
        self.next = next  # Initialize next as null

# Within your LinkedList class, include a head property. Upon instantiation, an empty Linked List should be created.
class Linked_list():
    def __init__(self):
        self.head = None  # Initialize head as None

    # Define a method called insert which takes any value as an argument and adds a new node with that value to the head of the list
    def insert(self,data):
        new_node = Node(data) # Create a new Node

        if self.head:
            current = self.head
            while(current.next):
                current = current.next
            current.next = new_node
        else:
            self.head = new_node
    # Define a method called includes which takes any value as an argument and returns a boolean result depending on whether that value exists as a Node’s value somewhere within the list.
    def includes(self,look_data):
        current = self.head
        while current != None:
            if current.data == look_data:
                return True # data found
            current = current.next
        return False # Data Not found

    #Define a method called toString (or __str__ in Python) which takes in no arguments and returns a string representing all the values in the Linked List, formatted as:
# "{ a } -> { b } -> { c } -> NULL"2
    def __str__(self):
        output = ""
        current = self.head
        while current:
            output+=f" {{{current.data}}} -> "
            current = current.next
        output+= "Null"
        return output


# # Write program here
# if __name__ == "__main__":
# #   item = Node("Mugh")
# #   linked = Linked_list()
# # #   print(linked)
# #   linked.head = item
# #   print(item.data)
# # #   print(linked.head)
# #   print(linked.insert("john"))
# # #   print(new_)
# #   linked.insert("doe")
# # #   linked.insert("Muhannad")
# # #   print(linked.__str__())
# # #   print(linked.includes("jack"))
# # #   print(linked.includes("Muhannad"))
