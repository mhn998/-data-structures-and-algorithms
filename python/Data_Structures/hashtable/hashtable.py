class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self,key,value):
        new_node = Node(key,value)

        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def __str__(self):
        output= ''
        current = self.head
        while current:
            output += f'{{{current.key}}}: {{{current.value}}}->'
            current = current.next
            if current == None:
                output += 'NULL'
        return output

class Hashtable:
    def __init__(self,size=1024):
        self.size = size
        self._buckets = [None]*size

    def hash(self,key):
        sum = 0
        for char in key:
            sum += ord(char)
        hash_key = (sum*29)%(self.size)
        return hash_key

    def add(self,key,value):
        index = self.hash(key)
        if self._buckets[index] is None:
            self._buckets[index] = LinkedList()
            self._buckets[index].insert(key,value)
        else:
            self._buckets[index].insert(key,value)


    def get(self,key):
        index = self.hash(key)

        if self._buckets[index] is None:
            return self._buckets[index]
        else:
            current = self._buckets[index].head
            while current:
                if current.key == key:
                    return current.value
                current = current.next

    def contains(self,key):
        index = self.hash(key)
        if self._buckets[index] != None:

            current = self._buckets[index].head
            while current:
                if current.key == key:
                    return True
                current = current.next
        else:
            return False

if __name__ == "__main__":
    hashtable = Hashtable()
    hashtable.add("muhannad", 10)
    hashtable.add("alrightee", False)
    hashtable.add("why", 'so serious')
    print(hashtable.get("muhannad"))
    print(hashtable.get("alrightee"))
    print(hashtable.get("why"))
    print(hashtable.contains("muhannad"))
    print(hashtable.hash('delicious'))

