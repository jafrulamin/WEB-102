#problem 2



'''
given a sorted(cabins)
find preferred_deck
if the preferred deck exists on the list return its index
if it does not exist return the expected index 

'''

# def find_cabin_index(cabins, preferred_deck):
#     # low, high = 0, len(cabins) - 1
#     if not cabins:
#         return None
#     mid = len(cabins) // 2

#     # if low > high:
#     #     return high
    

#     if cabins[mid] == preferred_deck:
#         return mid
    
#     if cabins[mid] > preferred_deck:
#         return find_cabin_index(cabins[:mid], preferred_deck)
#     elif cabins[mid] < preferred_deck:
#         return find_cabin_index(cabins[mid+1:], preferred_deck)
#     else:
# #        index_in_right = find_cabin_index(cabins[mid+1:], preferred_deck)
#         result = mid + 1 + index_in_right
#         return result

# def find_cabin_index(cabins, preferred_deck):
#     def helper(sub, offset):
#         if not sub:
#             return offset

#         mid = len(sub) // 2

#         if sub[mid] == preferred_deck:
#             return offset + mid
#         elif sub[mid] > preferred_deck:
#             return helper(sub[:mid], offset)
#         else:
#             return helper(sub[mid+1:], offset + mid + 1)

#     return helper(cabins, 0)



# print(find_cabin_index([1, 3, 5, 6], 5))
# print(find_cabin_index([1, 3, 5, 6], 2))
# print(find_cabin_index([1, 3, 5, 6], 7))



def count_checked_in_passengers(rooms):
    
# Example Usage:

rooms1 = [0, 0, 0, 1, 1, 1, 1]
rooms2 = [0, 0, 0, 0, 0, 1]
rooms3 = [0, 0, 0, 0, 0, 0]

print(count_checked_in_passengers(rooms1)) 
print(count_checked_in_passengers(rooms2))
print(count_checked_in_passengers(rooms3))
# Example Output:

# 4
# 1
# 0