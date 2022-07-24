def selection_sort(arr):
    """Selection sort is a simple sorting algorithm
        This sorting algorithm is an in-place comparison-based algorithm
            in which the list is divided into two parts,
                the sorted part at the left end and the unsorted part at the right end

        Args:
            arr(list): The list to be sorted
    """
    for i in range(len(arr)-1):
        nex_idx = i+1
        min_idx = i
        for j in range(nex_idx, len(arr)):
            if (arr[j] < arr[min_idx]):
                min_idx = j
        if (arr[min_idx] < arr[i]):
            arr[min_idx], arr[i] = arr[i], arr[min_idx]
        print(arr)
    return(arr)


arr = [19, 48, 99, 71, 13, 52, 96, 73, 86, 7]
selection_sort(arr)


"""Also saw people referring to this as selection sort so i implented it also"""
def selection_sort(arr):
    for i in range(len(arr)-1):
        c_run = i
        for j in range(c_run+1, len(arr)):
            if arr[c_run] > arr[j]:
                arr[c_run], arr[j] = arr[j], arr[c_run]
                c_run-1
        print(arr)
    return arr
