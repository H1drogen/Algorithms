from data_structures import binary_tree

def preOrder(root):
    values = []
    traversal(root, values)
    print(" ".join(str(x) for x in values))

def traversal(root, data):
    if root is not None:
        data.append(root.info)
        traversal(root.left, data)
        traversal(root.right, data)



root = binary_tree.Node(1)
root.right = binary_tree.Node(2)
root.right.right = binary_tree.Node(5)
root.right.right.right = binary_tree.Node(3)
root.right.right.left = binary_tree.Node(6)
root.right.right.right.right = binary_tree.Node(4)

preOrder(root)
