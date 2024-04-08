class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Create the nodes
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)



def height_of_binary_tree(node):
    # Base case: if node is null, return -1
    if node is None:
        return -1
    
    # Recursively calculate the height of the left and right subtrees
    left_height = height_of_binary_tree(node.left)
    right_height = height_of_binary_tree(node.right)
    
    # Return the maximum height of the left and right subtrees, plus 1 for the current node
    return max(left_height, right_height) + 1

# Test the algorithm
print("Height of the binary tree:", height_of_binary_tree(root))
