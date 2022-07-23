def insertion_sort(lists):
    """Insertion sort is a simple sorting algorithm
        that builds the final sorted array one item at a time

        Args:
            lists(list): The list to be sorted
        """
    for i in range(0, len(lists)):
        current_index = i
        prev_index = current_index - 1
        while (prev_index >= 0 and lists[prev_index] > lists[current_index]):
            if lists[prev_index] > lists[current_index]:
                lists[prev_index], lists[current_index] = lists[current_index], lists[prev_index]
                current_index-=1
                prev_index-=1
            print(lists)
    return lists

lists = [19, 48, 99, 71, 13, 52, 96, 73, 86, 7]
insertion_sort(lists)
