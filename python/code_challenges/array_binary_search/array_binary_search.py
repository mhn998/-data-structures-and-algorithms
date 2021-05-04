# import math
# def BinarySearch1(arr,value):
#     test=arr[0]
#     mid= math.floor((len(arr)/2))
#     x=mid
#     if type(value) != int:
#         print ('Invalid input to the Array')
#         return 'Invalid input to the Array'
#     if type(arr) != list:
#         print('Invalid type , please insert an array')
#         return 'Invalid type , please insert an array'
#     while test != value:
#         test=arr[mid]
#         if test == value:
#             print ("line 15", x)
#             return x
#         elif test > value:
#             newArrAfter=arr[:mid]
#             mid= int(math.floor((len(newArrAfter)/2)))
#             if mid != int(len(newArrAfter/2)):
#                 x-=mid+1
#                 print  (" line 21" ,x )
#             else:
#                 x-=mid
#                 print (" line 23 ", x)
#         elif test < value:
#             newArrayBefore=arr[mid:]
#             mid= math.floor((len(newArrayBefore)/2))
#             if mid %2==0:
#                 x+=mid
#                 print ("line28", x )
#             else:
#                 x+=mid
#                 print ("line 30", x )
#         if mid <=0:
#             return 'Unsuccessful , invalid input'

def BinarySearch(arr,value):
    if( value not in arr):
        print(-1)
        return -1
    for x in arr:
        if(x == value):
            print (arr.index(x))
            return arr.index(x)

# BinarySearch1([4,8,15,16,23,42], 15)
# BinarySearch([11,22,33,44,55,66,77], 90)
# BinarySearch([1, 2, 3, 5, 6, 7], 4)
# BinarySearch([4,8,15,16,23,42, 15 , 30 ,4554 , 2403], 15)
