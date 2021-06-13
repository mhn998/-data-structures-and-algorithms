def InsertionSort(arr:list):
  for i in range(1,len(arr)):
    j = i-1
    temp = arr[i]
    while j >= 0 and temp < arr[j]:
      arr[j+1] = arr[j]
      j = j-1
    arr[j+1] = temp
  return arr

if __name__ == '__main__':
    test = [5,10,4,2,8,19,11]
    InsertionSort(test)
