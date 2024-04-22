'''
Points giveaway)
'''

class Node:
    '''
    Node.
    '''
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

# Pre-order traversal
def pre_order(node):
    '''
    The simplest task :)
    '''
    if node is None:
        return []
    return [node.data] + pre_order(node.left) + pre_order(node.right)

# In-order traversal
def in_order(node):
    '''
    Another candidate on position of the simplest task.
    '''
    if node is None:
        return []
    return in_order(node.left) + [node.data] + in_order(node.right)

# Post-order traversal
def post_order(node):
    '''
    One more candidate on position of the simplest task.
    '''
    if node is None:
        return []
    return post_order(node.left) + post_order(node.right) + [node.data]

if __name__ == '__main__':
    a = Node(5)
    b = Node(10)
    c = Node(2)
    d = Node("leaf")
    a.left = b
    a.right = c
    c.left = d
    print(pre_order(a))
