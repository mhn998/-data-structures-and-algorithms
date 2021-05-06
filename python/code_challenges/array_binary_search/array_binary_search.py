import math
def BinarySearch(arr,value):
    if not(isinstance(value, int) or isinstance(value, float)):
        return ("it seems you are trying wrong input types , please insert any number")
    if type(arr) != list:
            return 'Invalid type , please insert an array'
    for x in arr:
        if not(isinstance(x, int) or isinstance(x, float)):
            return "Are you trying to fool me? please insert an array of numbers!"
    test=arr[0]
    mid=  math.floor((len(arr)/2))
    x=mid
    while test != value:
        test=arr[mid]
        if test == value:
            return x
        elif test > value:
            arr=arr[:mid]
            mid=  math.floor((len(arr)/2))
            if mid != len(arr)/2:
                x=x - (mid+1)
            else:
                x=x - mid
        elif test < value:
            arr=arr[mid:]
            mid=  math.floor((len(arr)/2))
            x=x+mid

        if mid == 0:
            return -1
