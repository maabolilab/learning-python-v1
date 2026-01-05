fast_food = ["burger", "pizza", "champ", "pakore", "patties", "sandwich"]


# for item in fast_food:
#     print(item.title())

# for number in list(range(1, 11)):
#     print(number * 2)

# binary_list = []
# for value in range(0, 11):
#     binary_list.append(2 ** value)

# print(binary_list)

# for value in range(0, 50, 10):
#     print(value)

# binary_list = [2 ** value for value in range(0, 11)]
# print("New List ... ")
# print(binary_list)

import random
random_numbers = [random.randint(0, 11) for _ in range(1, 4)]
print(random_numbers)