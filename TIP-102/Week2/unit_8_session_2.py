# # Problem 1:


# '''
# UPI method:
# Understand:
# input: the root node of a binary tree
# output: an integer representing the count of nodes that have odd value

# Plan:
# use a recursive approach to traverse the tree
# in each iteration check whether it is odd or even
# get the sum of the nodes that have odd values
# 2,3,5,6
# '''
from collections import deque

# class TreeNode:
#   def __init__(self, value, key=None, left=None, right=None):
#       self.key = key
#       self.val = value
#       self.left = left
#       self.right = right


def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root
         
# def count_odd_splits(root):
#     if root is None:
#         return 0
#     # if root.val%2 == 1:
#     #     left = 1+ count_odd_splits(root.left)
#     #     right = 1+ count_odd_splits(root.right)
#     # if root.left is None or if root.right is None:

#     if root.val % 2 == 1:
#         current_count = 1
#     else:
#         current_count = 0
#     left_tree = count_odd_splits(root.left)
#     right_tree = count_odd_splits(root.right)

#     return current_count+left_tree+right_tree



# # Using build_tree() function included at top of page
# values = [2, 3, 5, 6, 7, None, 12]
# monstera = build_tree(values)

# print(count_odd_splits(monstera))
# print(count_odd_splits(None))

#undeserstand:
#We're given a bst
# inventory=root name-what for looking for
#find name and reutnr true if its in bst else return false
#
class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right
         
def find_flower(inventory, name):
    if inventory is None:
        return False
   

    if inventory.val == name:
        return True
   
    left_tree = find_flower(inventory.left, name)
    right_tree = find_flower(inventory.right, name)

    return left_tree or right_tree



"""
          Rose
         /    \
      Lilac  Tulip
      /  \       \
   Daisy Lily   Violet
"""

# using build_tree() function at top of page
values = ["Rose", "Lilac", "Tulip", "Daisy", "Lily", None, "Violet"]
garden = build_tree(values)

print(find_flower(garden, "Lilac"))  
print(find_flower(garden, "Sunflower")) 


## Problem 3: Flower Finding II

"""
Understand the problem



"""



class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def non_bst_find_flower(root, name):
    if root is None:
        return False
    
    if root.val == name:
        return True

    return non_bst_find_flower(root.left, name) or non_bst_find_flower(root.right, name)

# using build_tree() function at top of page
values = ["Rose", "Lily", "Tulip", "Daisy", "Lilac", None, "Violet"]
garden = build_tree(values)

print(non_bst_find_flower(garden, "Lilac"))  
print(non_bst_find_flower(garden, "Sunflower"))  
