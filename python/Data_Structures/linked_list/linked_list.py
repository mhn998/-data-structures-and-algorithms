# Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.

class Node():
    def __init__(self,value, next=None):
        self.value = value  # Assign data
        self.next = next  # Initialize next as null

# Within your LinkedList class, include a head property. Upon instantiation, an empty Linked List should be created.

class Linked_list():
    def __init__(self):
        self.head = None  # Initialize head as None

    # Define a method called insert which takes any value as an argument and adds a new node with that value to the head of the list

    def insert(self,value):
        new_node = Node(value) # Create a new Node

        if self.head:
            current = self.head
            while(current.next):
                current = current.next
            current.next = new_node
        else:
            self.head = new_node
    # .append(value) which adds a new node with the given value to the end of the list

    def append(self,value):
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
        else:
            current = self.head

            while current.next:
                current = current.next

            current.next = new_node

        # .insertBefore(value, newVal) which add a new node with the given newValue immediately before the first value node

    def insertBefore(self,value, newVal):
        new_node = Node(newVal)
        current = self.head
        if current.value == value:
            new_node.next = current
            self.head = new_node
        else:
            while current.next:
                if current.next.value == value:
                    new_node.next = current.next
                    current.next = new_node
                    break
                current = current.next

                if current.next == None:
                    raise Exception("No value found")

        # .insertAfter(value, newVal) which add a new node with the given newValue immediately after the first value node

    def insertAfter(self,value, newVal):
        new_node = Node(newVal)
        current = self.head
        while current:
            if current.value == value:
                new_node.next = current.next
                current.next = new_node
                break
            current = current.next
            if current == None:
                raise Exception("No value found")

    # Define a method called includes which takes any value as an argument and returns a boolean result depending on whether that value exists as a Node’s value somewhere within the list.

    def includes(self,look_data):
        current = self.head
        while current != None:
            if current.value == look_data:
                return True # data found
            current = current.next
        return False # Data Not found

    #Define a method called toString (or __str__ in Python) which takes in no arguments and returns a string representing all the values in the Linked List, formatted as:
# "{ a } -> { b } -> { c } -> NULL"2

    def kthFromEnd(self,k):
        try:
            if k < 0:
                raise Exception
        except Exception:
            return ("Invalid input with a negative value")
        result=[]
        current = self.head
        if current == None:
            return ("Linked list is empty")
        while current:
            result += [current.value]
            current = current.next
            if current == None:
                break
        try:
            return result[::-1][k]
        except IndexError:
            return ("Out Of Range")

    def __str__(self):
        output = ""
        current = self.head
        while current:
            output+=f" {{{current.value}}} -> "
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
