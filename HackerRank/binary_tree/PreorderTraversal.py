from data_structures import binary_tree

# Easy
# Complete the function in the editor below, which has 1 parameter: a pointer to the root of a binary tree. It must print the values in the tree's preorder traversal as a single line of space-separated values.

def preOrder(root):
    values = []
    traversal(root, values)
    print(" ".join(str(x) for x in values))

def traversal(root, data):
    if root is not None:
        data.append(root.info)
        traversal(root.left, data)
        traversal(root.right, data)

# TRICK: The trick is the visit order: preorder means Root → Left → Right. At each node, record its value first, then recursively traverse the left subtree, followed by the right subtree. The root is not None check is the base case that stops recursion at empty branches.

root = binary_tree.Node(1)
root.right = binary_tree.Node(2)
root.right.right = binary_tree.Node(5)
root.right.right.right = binary_tree.Node(3)
root.right.right.left = binary_tree.Node(6)
root.right.right.right.right = binary_tree.Node(4)

preOrder(root)
