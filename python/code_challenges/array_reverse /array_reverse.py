def reverse_array(arr):
    return arr[::-1]

def reverse_array_2(arr):
    arr2 = []
    for i in range(len(arr)-1,-1,-1):
        arr2.append(arr[i])
    return arr2

def reverse_array_3(arr):
    arr3 =[]
    for i in arr:
        arr3.insert(0,i)
    return arr3

def reverse_array_4(arr):
    arr4 =[]
    x= len(arr)-1
    while(x>-1):
        arr4.append(arr[x])
        x-=1
    return arr4
