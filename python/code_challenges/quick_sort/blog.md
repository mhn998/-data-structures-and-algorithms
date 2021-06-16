# Quick Sort

Quick Sort is also called partition-exchange sort. This algorithm divides the given array of numbers into three main parts: Elements less than the pivot element. Pivot element , Elements greater than the pivot element

Quick Sort is based on the concept of Divide and Conquer algorithm, which is also the concept used in Merge Sort. The difference is, that in quick sort the most important or significant work is done while partitioning (or dividing) the array into subarrays, while in case of merge sort, all the major work happens during merging the subarrays. For quick sort, the combining step is insignificant.

## Pseudo code

    ALGORITHM QuickSort(arr, left, right)
        if left < right
            // Partition the array by setting the position of the pivot value
            DEFINE position <-- Partition(arr, left, right)
            // Sort the left
            QuickSort(arr, left, position - 1)
            // Sort the right
            QuickSort(arr, position + 1, right)

    ALGORITHM Partition(arr, left, right)
        // set a pivot value as a point of reference
        DEFINE pivot <-- arr[right]
        // create a variable to track the largest index of numbers lower than the defined pivot
        DEFINE low <-- left - 1
        for i <- left to right do
            if arr[i] <= pivot
                low++
                Swap(arr, i, low)

        // place the value of the pivot location in the middle.
        // all numbers smaller than the pivot are on the left, larger on the right.
        Swap(arr, right, low + 1)
        // return the pivot index point
        return low + 1

    ALGORITHM Swap(arr, i, low)
        DEFINE temp;
        temp <-- arr[i]
        arr[i] <-- arr[low]
        arr[low] <-- temp


## Trace
Since it's too long to trace it , this is sample work of tracing in code until more than the half of the process.
'#' means another level of processing
'/' between values mean the same process but at different loops

        def quick_sort(arr:list,left:int,right:int):
            if left < right: #0 < 5(True)
                position = partition(arr, left , right)#(arr , 0 , 5)-> return 2 (arr,0,1) -> return 1
                quick_sort(arr,left,position -1)#(arr,0,1) #(arr,0,0)
                quick_sort(arr,position+1,right) # (arr,2,1)
            return arr

        def partition(arr,left,right):#(arr,0/0,5/1)
            pivot = arr[right] # arr[5] = 15,4
            low = left - 1 # low = -1,-1
            for i in range(left,right): #0,1,2,3,4 / #0
                if arr[i] <= pivot: #8,4,23,42,16  <= 15
                    low+=1 # 0,1
                    swap(arr,i,low) # (arr,0/1,0/1)
            swap(arr, right, low+1)#(arr,5,2) (arr,1,0)
            return low + 1

        def swap(arr,i,low):#(arr,0/1/5,0/1/2) #(arr,1,0)
            temp = arr[i] #8,4,15 #4
            arr[i] = arr[low]#[8,8,.,.,.,23]
            arr[low] = temp#[4,8,15,.,.,23]

        test = [20,18,12,8,5,-2]
        print(quick_sort(test,0,len(test)-1))
        print(test)
