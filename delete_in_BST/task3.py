'''
NO, PLS, NOT DELETION!
Ok, after reading explanation on
https://www.geeksforgeeks.org/deletion-in-binary-search-tree/
website, it seems easier.
Still, I am pretty sure there is a better solution.
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        '''
        DELETE NODE
        '''
        # The edgecase
        if not root:
            return None

        # Recursive call of the function with corresponding subtree
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)

        # When we found the node to delete
        else:
            # Case1: one or no child
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            # Case2: two children
            node = root.right # the successor
            while node.left:
                node = node.left
            root.val = node.val
            # Delete successor from the right subtree
            root.right = self.deleteNode(root.right, node.val)
        return root
