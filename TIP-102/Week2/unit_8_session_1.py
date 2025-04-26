# # Problem 1


# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# root = TreeNode("Trunk")

# root.left = TreeNode("Mcintosh")
# root.left.left = TreeNode("Fuji")
# root.left.right = TreeNode("Opal")


# root.right = TreeNode("Granny Smith")
# root.right.left = TreeNode("Crab")
# root.right.right = TreeNode("Gala")



# def print_tree(node):
#     if node is None:
#         return
    
#     print(node.val)  # Print the current node's value
    
#     print_tree(node.left)  # Recursively print the left asubtree
#     print_tree(node.right)  # Recursively print the right subtree


# print(print_tree(root))











# Problem 2: Calculating Yield







# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def calculate_yield(root):
#   left_val = root.left.val
#   right_val= root.right.val


#   operation = root.val


#   if operation == "+":
#      return left_val+right_val
#   elif operation == "-":
#      return left_val-right_val
#   elif operation == "*":
#      return left_val*right_val
#   else:
#      return left_val/right_val
  


# apple_tree = TreeNode("+", TreeNode(7), TreeNode(5))

# print(calculate_yield(apple_tree))




# Problem 3: Ivy Cutting
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def right_vine(root):
  path = []
  current = root
  while current:
    path.append(current.val)
    if current.right:
        current = current.right
    else: 
        break
  return path

ivy1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))
ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

print(right_vine(ivy1))
print(right_vine(ivy2))


# Example Output:

# ['Root', 'Node2', 'Leaf3']
# ['Root']