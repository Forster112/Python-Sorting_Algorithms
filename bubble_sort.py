def bubblesort(arr):
    """bubble sort is a simple sorting algorithm
          that repeatedly steps through the list,
          compares adjacent elements and swaps them if they are in the wrong order.
          The pass through the list is repeated until the list is sorted
        Arg:
            arr(list): the list to be sorted"""
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print(arr)
    return arr
 
       
arr = [19, 48, 99, 71, 13, 52, 96, 73, 86, 7]
bubblesort(arr)
