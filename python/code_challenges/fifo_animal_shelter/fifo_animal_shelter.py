
class AnimalShelter:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self,animal):
        new_node = animal
        if self.front is None:
            self.front= new_node
            self.rear = new_node
        self.rear.next = new_node
        self.rear = self.rear.next

    def dequeue(self,kind=None):
        if kind == None:
            if self.front:
                node = self.front
                self.front = self.front.next
                return node.value
        else:
            current = self.front

            if self.front.kind == kind:
                node = self.front
                self.front = self.front.next
                return node.value
            else:
                while current.next:
                    if current.next.kind == kind:
                        node = current.next
                        current.next = current.next.next
                        return node.value

                    if current.kind != kind:
                        current = current.next
                return 'Null'


    def __str__(self):
        result= ""
        current = self.front
        while current:
            result += f"{{{current.value}}}->"
            current = current.next
            if current is None: result += 'Null'

        return result


class Dog:
    def __init__(self,value):
        self.value = value
        self.kind = 'Dog'
        self.next = None

class Cat:
    def __init__(self,value):
        self.value = value
        self.kind = 'Cat'
        self.next = None




# if __name__ == "__main__":
#     shelter =AnimalShelter()
#     shelter.enqueue(Cat('ok'))
#     shelter.enqueue(Dog('test'))
#     shelter.enqueue(Cat('this'))
#     print(shelter)
#     shelter.enqueue(Dog('max'))
#     print(shelter.dequeue('Dog'))
#     print(shelter.dequeue('Bird'))
#     print(shelter.dequeue())
#     print(shelter.dequeue('Cat'))
#     print(shelter)
