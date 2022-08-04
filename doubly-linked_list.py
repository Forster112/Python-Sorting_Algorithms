class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.prev, current.data, current.next, end=' # ')
            current = current.next

    def insert(self, head, data):
        node = Node(data)
        if head is None:
            head = node
        else:
            n = head
            while n.next is not None:
                n = n.next
                n.prev = n
            n.next = node
            node.prev = node
        return head


mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)
mylist.display(head)
