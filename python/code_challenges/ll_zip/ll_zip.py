from Data_Structures.linked_list.linked_list import Linked_list

def zipLists(ll1,ll2):
    i , j = 0, 0
    current1 = ll1.head
    current2 = ll2.head

    while current1:
        i += 1
        current1 = current1.next
        if current1 == None:
            break
    while current2:
        j += 1
        current2 = current2.next
        if current2 == None:
            break
    if i < j:
        head = ll2.head.value
        current1 = ll2.head
        current2 = ll1.head

    elif j <= i:
        current1 = ll1.head
        current2 = ll2.head

    while current1 != None or current2 != None:

        if current2 != None:
            new_next1 = current1.next
            new_next2 = current2.next
            current1.next = current2
            current1 = current1.next
            if new_next1 != None:
                current1.next = new_next1
                current1 = current1.next
            current2 = new_next2


        if current1.next == None and current2 == None:
            current1 = current1.next

        if current1 == None:
            if i < j:
                ll1.insert(head)
            return ll1
