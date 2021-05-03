import math
def insertShiftArray(arr,value):
    newArr = []
    for x in arr:
        newArr.append(x)
    if len(arr) % 2 == 0:
        i = len(arr)//2
        newArr.insert(i,value)
        return newArr
    else:
        i = len(arr)//2 + 1
        newArr.insert(i,value)
        return newArr

def insertShiftArray_1(arr,value):
    x = math.ceil(len(arr)/2)
    return arr[:x] + [value] + arr[x:]

