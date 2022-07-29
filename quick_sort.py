def quick_sort(arr):
    """Quicksort is a sorting algorithm based on the divide and conquer approach where
        An array is divided into subarrays by selecting a pivot element
        (element selected from the array).
        
        Best time complexity: O(log n)
        Average time complexity: O(nlogn)
        Worst time complexity: O(n^2)
    """
    if len(arr) <= 1:
        """return the list if the length is less than and equal to 1"""
        return arr
    else:
        """take the element at the last index as our pivot"""
        pivot = arr.pop()
    greater = []
    lesser = []
    for i in arr:
        if i > pivot:
            greater.append(i)
        else:
            lesser.append(i)
    print(arr)
    """recusively perform the sort in both lists"""
    return quick_sort(lesser) + [pivot] + quick_sort(greater)

arr = [19, 48, 99, 71, 13, 52, 96, 73, 86, 7]
print(quick_sort(arr))