from typing import List


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:

        node_location = {0}

        for i in range(n):
            if leftChild[i] > -1 or rightChild[i] > -1:
                if i not in node_location:
                    return False
                if (leftChild[i] in node_location) or (rightChild[i] in node_location):
                    return False

                if leftChild[i] > -1:
                    node_location.add(leftChild[i])
                if rightChild[i] > -1:
                    node_location.add(rightChild[i])

        return True


sol = Solution()
print(sol.validateBinaryTreeNodes(6, [1, -1, -1, 4, -1, -1], [2, -1, -1, 5, -1, -1]))
