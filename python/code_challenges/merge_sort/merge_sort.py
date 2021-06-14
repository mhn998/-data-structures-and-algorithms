def merge_sort(arr:list):
    n = len(arr)

    if n > 1:
        mid = n//2
        left = arr[:mid]
        right = arr[mid:n]

        merge_sort(left)
        merge_sort(right)
        merge(left , right , arr)

    return arr

def merge(left,right,arr):
    i,j,k = 0, 0, 0

    while i< len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i+=1

        else:
            arr[k] = right[j]
            j+=1

        k+=1


    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

