import sys


class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def levelOrder(self, root):
        if root is None:
            return []
        queue = [root]
        next_queue = []
        level = []
        result = []
        final_result = []
        while queue != []:
            for i in queue:
                level.append(i.data)
                if i.left is not None:
                    next_queue.append(i.left)
                if i.right is not None:
                    next_queue.append(i.right)
            result.append(level)
            level = []
            queue = next_queue
            next_queue = []
        for i in result:
            for j in i:
                final_result.append(str(j))
        final_result = ' '.join(final_result)
        print(final_result)


T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)
myTree.levelOrder(root)
