from helpers.NODE import TreeNode
import unittest


def array_to_bst(arr, i=None, n=None):
    if not i:
        i = 0
    if not n:
        n = len(arr)

    if i >= n:
        return None
    node = TreeNode(arr[i])
    node.left = array_to_bst(arr, ((2 * i) + 1), n)
    node.right = array_to_bst(arr, ((2 * i) + 2), n)

    return node


def bst_to_array(node: TreeNode):
    queue = []
    array = []
    if node:
        queue.append(node)

    while queue:
        size = len(queue)

        while size:
            size -= 1
            temp_node = queue.pop(0)
            array.append(temp_node.val)

            if temp_node.left:
                queue.append(temp_node.left)

            if temp_node.right:
                queue.append(temp_node.right)

    return array


class TestBST(unittest.TestCase):

    def test_array_to_bst(self):
        test_array = [1, 3, 2, 4, 5]
        test_node = array_to_bst(test_array)
        self.assertListEqual(bst_to_array(test_node), test_array)

        print('Array to BST working fine')

    def test_bst_to_array(self):
        test_array = [1, 3, 2, 4, 5]
        test_node = array_to_bst(test_array)
        self.assertListEqual(test_array, bst_to_array(test_node))

        print('BST to Array working fine')


if __name__ == '__main__':
    unittest.main()
