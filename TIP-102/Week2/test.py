# # def count_suits_iterative(suits):
# #     unique_suits = set()

# #     for suit in suits:
# #         unique_suits.add(suit)
# #     return len(unique_suits)


# def count_suits_recursive(suits):
#     # unique_suits = set()

#     if not suits:
#         return 0
    
#     first_suit = suits[0]
    
#     unique_suits = first_suit
    



# # print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
# print(count_suits_recursive(["Mark I", "Mark I", "Mark III"]))





def strongest_avenger(strengths):
    if len(strengths) == 1:
        return strengths[0]
    

    max_in_remaining = strongest_avenger(strengths[1:])

    if strengths[0] > max_in_remaining:
        return  strengths[0]
    else:
        return max_in_remaining
    

print(strongest_avenger([88, 92, 95, 99, 97, 100, 94]))
print(strongest_avenger([50, 75, 85, 60, 90]))