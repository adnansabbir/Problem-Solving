# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode, min_depth=0) -> int:
        if not root:
            return 0

        queue = []
        queue.append(root)

        while queue:
            min_depth += 1
            count = len(queue)

            while count:
                temp = queue.pop()

                if temp.right:
                    queue.insert(0, temp.right)
                if temp.left:
                    queue.insert(0, temp.left)

                if not (temp.right or temp.left):
                    queue.clear()
                    count = 1
                count -= 1

        return min_depth


t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(2)
t1.left = t2
t1.right = t3

t4 = TreeNode(3)
t5 = TreeNode(3)
t2.left = t4
t2.right = t5

t6 = TreeNode(3)
t7 = TreeNode(3)
t3.left = t6
t3.right = t7

t8 = TreeNode(4)
t9 = TreeNode(4)
t10 = TreeNode(4)
t11 = TreeNode(4)
t12 = TreeNode(4)
t13 = TreeNode(4)

t4.left = t8
t4.right = t9

t5.left = t10
t5.right = t11

t6.left = t12
t6.right = t13

t14 = TreeNode(5)
t15 = TreeNode(5)
t16 = TreeNode(5)

t7.left = t14
t14.right = t15
t15.right = t16

# t6.right = None

sol = Solution()
print(sol.minDepth(t1))
