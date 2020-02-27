# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Recursion implementation
# class Solution:
#     def levelOrderDepthDict(self, root: TreeNode, data: dict = None, depth=0):
#         if not data:
#             data = {
#                 depth: [],
#                 "max_depth": 0
#             }
#
#         if root:
#             if depth in data:
#                 data[depth].append(root.val)
#             else:
#                 data[depth] = [root.val]
#
#             if root.left:
#                 self.levelOrderDepthDict(root.left, data, depth + 1)
#             if root.right:
#                 self.levelOrderDepthDict(root.right, data, depth + 1)
#
#         data['max_depth'] = max(data['max_depth'], depth)
#         return data
#
#     def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
#         data = self.levelOrderDepthDict(root)
#         data_array = []
#         for i in range((data['max_depth']), -1, -1):
#             if len(data[i]):
#                 data_array.append(data[i])
#         return data_array


# Iteration Implementation
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        queue = []
        data = []

        if root:
            queue.append(root)

        while queue:
            count = len(queue)
            depth = len(data)
            while count:
                temp = queue.pop()
                data[depth].append(temp.val) if depth+1 == len(data) else data.insert(depth, [temp.val])
                if temp.left:
                    queue.insert(0, temp.left)
                if temp.right:
                    queue.insert(0, temp.right)
                count -= 1

        return data[::-1]


t1 = TreeNode(1)

t2 = TreeNode(2)
t3 = TreeNode(2)
t1.left = t2
t1.right = t3

t4 = TreeNode(3)
t5 = TreeNode(3)
t3.left = t4
t3.right = t5

t6 = TreeNode(4)
t7 = TreeNode(4)
t4.left = t6
t4.right = t7

t6.right = None

sol = Solution()
print(sol.levelOrderBottom(t1))

# arr = [1,2,3,4,5]
# print(arr[::-1])
