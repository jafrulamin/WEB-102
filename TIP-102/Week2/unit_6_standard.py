# # Problem 1: Wild Goose Chase
# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# def is_circular(clues):
#     # If the list is empty, it's not circular.
#     if clues is None:
#         return False

#     current = clues  # Start at the head
#     # Traverse the list until we reach the end or find a pointer back to head
#     while current.next is not None and current.next != clues:
#         current = current.next

#     # If the last node's next points back to the head, it's circular.
#     return current.next == clues

# # Example Usage:
# clue1 = Node("The stolen goods are at an abandoned warehouse")
# clue2 = Node("The mayor is accepting bribes")
# clue3 = Node("They dumped their disguise in the lake")
# clue1.next = clue2
# clue2.next = clue3
# clue3.next = clue1  # Making it circular

# print(is_circular(clue1))  # Expected output: True






# Problem 2: Breaking the Cycle


# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# def collect_false_evidence(evidence):
#     if evidence is None:
#         return []
    
#     # Step 1: Detect a cycle using slow and fast pointers.
#     slow, fast = evidence, evidence
#     cycle_found = False
#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next
#         if slow == fast:
#             cycle_found = True
#             break
    
#     # If no cycle is detected, return an empty list.
#     if not cycle_found:
#         return []
    
#     # Step 2: Find the entry point of the cycle.
#     entry = evidence
#     while entry != slow:
#         entry = entry.next
#         slow = slow.next
    
#     # Step 3: Traverse the cycle and collect the values.
#     values = []
#     current = entry
#     while True:
#         values.append(current.value)
#         current = current.next
#         if current == entry:
#             break
    
#     return values

# # Example Usage:
# clue1 = Node("Unmarked sedan seen near the crime scene")
# clue2 = Node("The stolen goods are at an abandoned warehouse")
# clue3 = Node("The mayor is accepting bribes")
# clue4 = Node("They dumped their disguise in the lake")
# clue1.next = clue2
# clue2.next = clue3
# clue3.next = clue4
# clue4.next = clue2  # Cycle starts at clue2

# # A list with no cycle:
# clue5 = Node("A masked figure was seen fleeing the scene")
# clue6 = Node("Footprints lead to the nearby woods")
# clue7 = Node("A broken window was found at the back")
# clue5.next = clue6
# clue6.next = clue7

# print(collect_false_evidence(clue1))
# # Expected output (order may vary): 
# # ['The stolen goods are at an abandoned warehouse', 'The mayor is accepting bribes', 'They dumped their disguise in the lake']

# print(collect_false_evidence(clue5))
# # Expected output: []



# Problem 3: Prioritizing Suspects


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def partition(suspect_ratings, threshold):
    greater_list = None
    smaller_list = None



    current = suspect_ratings

    
    while current != None:




def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

# Example Usage:
suspect_ratings = Node(1, Node(4, Node(3, Node(2, Node(5, Node(2))))))
print_linked_list(partition(suspect_ratings, 3))
# Possible acceptable outputs:
# 4 -> 5 -> 1 -> 3 -> 2 -> 2
# (Nodes with values >3 come first, order among groups can vary)
