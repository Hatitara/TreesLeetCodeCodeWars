'''
I AM SURE IT IS BFS!!! 100%
'''
from collections import deque

class Node:
    '''
    Class for nodes.
    '''
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

def tree_by_levels(node: 'Node') -> list:
    '''
    Return tree as level-sorted arr.
    '''
    if not node:
        return []
    visited = [node]
    queue = deque(visited)
    while queue:
        current_node = queue.popleft()
        if current_node.left and current_node.left not in visited:
            visited.append(current_node.left)
            queue.append(current_node.left)
        if current_node.right and current_node.right not in visited:
            visited.append(current_node.right)
            queue.append(current_node.right)
    return [k.value for k in visited]

if __name__ == '__main__':
    bad = None
    sample_tree = Node(Node(None, Node(None, None, 4), 2), Node(Node(None, None, 5), Node(None, None, 6), 3), 1)
    print(tree_by_levels(bad))
    print(tree_by_levels(sample_tree))
