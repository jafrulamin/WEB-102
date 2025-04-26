# # Standard Problem Set Version 1

# # Problem 1: Mutual Friends
# class Villager:
#     def __init__(self, name, species, catchphrase):
#         self.name = name
#         self.species = species
#         self.catchphrase = catchphrase
#         self.friends = []

#     def get_mutuals(self, new_contact):
#         mutuals = []
#         for friend in self.friends:
#             if friend in new_contact.friends:
#                 mutuals.append(friend.name)
#         return mutuals


# bob = Villager("Bob", "Cat", "pthhhpth")
# marshal = Villager("Marshal", "Squirrel", "sulky")
# ankha = Villager("Ankha", "Cat", "me meow")
# fauna = Villager("Fauna", "Deer", "dearie")
# raymond = Villager("Raymond", "Cat", "crisp")
# stitches = Villager("Stitches", "Cub", "stuffin")

# bob.friends = [stitches, raymond, fauna]
# marshal.friends = [raymond, ankha, fauna]
# print(bob.get_mutuals(marshal))

# ankha.friends = [marshal]
# print(bob.get_mutuals(ankha))


# Problem 2: Linked Up

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next

# kk_slider = Node("K.K. Slider")
# harriet = Node("Harriet")
# saharah = Node("Saharah")
# isabelle = Node("Isabelle")

# kk_slider.next = harriet
# harriet.next = saharah
# saharah.next = isabelle

# print_linked_list(kk_slider)



# Problem 3: Daily Tasks



# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next

# def add_first(head, task):
#     newnode = Node(task)
#     newnode.next = head
#     return newnode

# task_1 = Node("shake tree")
# task_2 = Node("dig fossils")
# task_3 = Node("catch bugs")
# task_1.next = task_2
# task_2.next = task_3

# # Linked List: shake tree -> dig fossils -> catch bugs
# print_linked_list(add_first(task_1, "check turnip prices"))


# # Problem 4: Halve List
# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next

# def halve_list(head):
#     curr = head
#     while curr:
#         curr.value /= 2
#         curr = curr.next
#     return head

# node_one = Node(5)
# node_two = Node(6)
# node_three = Node(7)
# node_one.next = node_two
# node_two.next = node_three

# # Input List: 5 -> 6 -> 7
# print_linked_list(halve_list(node_one))



# # Problem 5: Remove Last
# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next

# def delete_tail(head):
#     if not head or not head.next:
#         return None
    
#     curr = head
#     while curr.next and curr.next.next:
#         curr = curr.next

#     curr.next = None
#     return head

# butterfly = Node("Common Butterfly")
# ladybug = Node("Ladybug")
# beetle = Node("Scarab Beetle")
# butterfly.next = ladybug
# ladybug.next = beetle

# # Input List: butterfly -> ladybug -> beetle
# print_linked_list(delete_tail(butterfly))


#Problem 6: Find Minimum in Linked List


# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next

# def find_min(head):
#     if not head:
#         return None
    
#     min = head.value
#     curr = head.next
#     while curr:
#         if curr.value < min:
#             min = curr.value
#         curr = curr.next
    
#     return min

# head1 = Node(5, Node(6, Node(7, Node(8))))
# head2 = Node(8, Node(5, Node(6, Node(7))))

# # Linked List: 5 -> 6 -> 7 -> 8
# print(find_min(head1))

# # Linked List: 8 -> 5 -> 6 -> 7
# print(find_min(head2))


# Problem 7: Remove From Inventory
# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next

# def delete_item(head, item):
#     if not head:
#         return None
    
#     if head.value == item:
#         return head.next
    
#     curr = head
#     while curr.next:
#         if curr.next.value == item:
#             curr.next = curr.next.next
#             return head
#         curr = curr.next
    
#     return head

# slingshot = Node("Slingshot")
# peaches = Node("Peaches")
# beetle = Node("Scarab Beetle")
# slingshot.next = peaches
# peaches.next = beetle

# # Linked List: slingshot -> peaches -> beetle
# print_linked_list(delete_item(slingshot, "Peaches"))

# # Linked List: slingshot -> beetle
# print_linked_list(delete_item(slingshot, "Triceratops Torso"))



# Problem 8: Move Tail to Front of Linked List

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next

# def tail_to_head(head):
#     curr = head
#     while curr.next:
#         curr = curr.next
    
#     tail = curr #tail is now the lsat element in the linked list
#     curr = head #now we set the curr element to be the head

#     while curr.next != tail: #traverse the linked list until we reach the last element
#         curr = curr.next

#     curr.next = None #remove the remainder and set the next of tail to be head, so we have 4 -> 1 -> 2 -> 3
#     tail.next = head

#     return tail

# daisy = Node("Daisy")
# mario = Node("Mario")
# toad = Node("Toad") 
# peach = Node("Peach")
# daisy.next = mario
# mario.next = toad
# toad.next = peach

# # Linked List: Daisy -> Mario -> Toad -> Peach
# print_linked_list(tail_to_head(daisy))


# Problem 9: Create Double Links

# class Node:
#     def __init__(self, value, next=None, prev=None):
#         self.value = value
#         self.next = next
#         self.prev = prev

# head = Node("Isabelle")
# tail = Node("K.K. Slider")
# #
# head.next = tail
# tail.prev = head

# print(head.value, "<->", head.next.value)
# print(tail.prev.value, "<->", tail.value)

# # <-- (Isabelle) --> (KK slideer) -->
# #                <--

#Problem 10: Print Backwards
# class Node:
#     def __init__(self, value, next=None, prev=None):
#         self.value = value
#         self.next = next
#         self.prev = prev

# def print_reverse(tail):
#     curr = tail
#     while curr:
#         print(curr.value, end = " " if curr.prev else "\n")
#         curr = curr.prev
    
# isabelle = Node("Isabelle")
# kk_slider = Node("K.K. Slider")
# saharah = Node("Saharah")
# isabelle.next = kk_slider
# kk_slider.next = saharah
# saharah.prev = kk_slider
# kk_slider.prev = isabelle

# # Linked List: Isabelle <-> K.K. Slider <-> Saharah
# print_reverse(saharah)

# # 1 (start) ->(.next) 2 -> 3 -> 4

# # 1 ->      2   ->      3       ->      4       -> Null
# #    <-         <-             <-(.prev)      