from Data_Structures.hashtable.hashtable import Hashtable

def left_join(h_t1,h_t2):
    lst = []
    # loop over hashmap1
    for i in h_t1:
        if i is not None:
            current = i.head
            while current:
                lst += [[current.key, current.value],] # append key value pair as sub array
                current = current.next
    # print(lst)

    for i in lst: # loop over the array of hashmap1 with its keys and values
        if h_t2.contains(i[0]) == True: # check if the key exists in h2 , if yes
            i.append(h_t2.get(i[0])) # --> Append the value of of the key to the second element in the inner array
        else:
            i.append(None) # append None if there is no key existed in hasmap2

    return lst


# if __name__ == '__main__':

#     test1 = Hashtable()
#     test1.add('fond', 'enamored')
#     test1.add('wrath', 'anger')
#     test1.add('diligent', 'employed')
#     test1.add('outift', 'garb')
#     test1.add('guide', 'usher')


#     test2 = Hashtable()
#     test2.add('fond', 'averse')
#     test2.add('wrath', 'delight')
#     test2.add('diligent', 'idle')
#     test2.add('guide', 'follow')
#     test2.add('flow', 'jam')

#     test3 = Hashtable()
#     test3.add('wrath', 'delight')
#     test3.add('diligent', 'idle')


#     print(left_join(test,test3))
