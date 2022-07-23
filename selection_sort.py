def selection_sort(arr):
    """Selection sort is a simple sorting algorithm
        This sorting algorithm is an in-place comparison-based algorithm
            in which the list is divided into two parts,
                the sorted part at the left end and the unsorted part at the right end

        Args:
            arr(list): The list to be sorted
    """
    for i in range(len(arr)):
        c_run = i
        for j in range(c_run+1, len(arr)):
            if arr[c_run] > arr[j]:
                arr[c_run], arr[j] = arr[j], arr[c_run]
                c_run-1
        print(arr)
    return arr


arr = [3, 0, 1, 8, 7, 2, 5, 4, 9, 6]
selection_sort(arr)
