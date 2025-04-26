
# Problem 1: Merging Cookie Orders


'''
UPI
Understand:
2 trees given to us
merge them into one tree
2 nodes with same value will be added together
if no similar nodes found we will save it as it is

Plan:
Base cases:
If first tree is empty, return the second tree
if the second tree is empty, return the first tree

Merging the nodes of two trees into one

use recursion to traverse through the left side of both trees
use recursion to traverse through the right side of both trees

return the final answer

'''


from collections import deque 
class TreeNode():
     def __init__(self, quantity, left=None, right=None):
        self.val = quantity
        self.left = left
        self.right = right


# Tree Node class
class TreeNode:
  def __init__(self, value, key=None, left=None, right=None):
      self.key = key
      self.val = value
      self.left = left
      self.right = right

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

def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)


# def merge_orders(order1, order2):
   
#     if not order1:
#         return order2
#     if not order2:
#         return order1
#     if not order1 or not order2:
#         return None
    
    

#     mergedTree = TreeNode(order1.val + order2.val)


#     mergedTree.left = merge_orders(order1.left, order2.left)
#     mergedTree.right = merge_orders(order1.right, order2.right)

#     return mergedTree


"""
     1             2         
    /  \         /   \       
   3    2       1     3   
 /               \      \   
5                 4      7   
"""
# Using build_tree() function included at top of page
# cookies1 = [1, 3, 2, 5]
# cookies2 = [2, 1, 3, None, 4, None, 7]
# order1 = build_tree(cookies1)
# order2 = build_tree(cookies2)

# # Using print_tree() function included at top of page
# print_tree(merge_orders(order1, order2))

'''
[3, 4, 5, 5, 4, None, 7]
Explanation:
Merged Tree:
     3
    /  \      
  4     5  
 / \      \
5   4      7
'''

# If the tree is empty:
#     return an empty list

# Create an empty queue
# Create an empty list to store visited nodes

# Add the root into the queue

# While the queue is not empty:
#     Pop the next node off the queue 
#     Add the popped node to the list of visited nodes

#     Add the popped node's left child to the queue
#     Add the popped node's right child to the queue


'''
UPI

Understand: 

Plan: edge cases : empty tree return empty list

Implementation
'''

class Puff():
     def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right

def print_design(design):
    if not design:
        return []

    visited = []
    queue = deque([design])    

    while queue:
        node = queue.popleft()
        visited.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return visited


# Example Usage:

# """
#             Vanilla
#            /       \
#       Chocolate   Strawberry
#       /     \
#   Vanilla   Matcha  
# """
croquembouche = Puff("Vanilla", 
                    Puff("Chocolate", Puff("Vanilla"), Puff("Matcha")), 
                    Puff("Strawberry"))

print_design(croquembouche)