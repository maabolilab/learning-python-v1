# def greet_hello(name):
#     print(f"Hello {name}")

# greet_hello("Harmeet")
# greet_hello("Harkirat")
# greet_hello("Amitoz")

# def print_user_biography(name, age, pet_name):
#     print(f"I am {name}")
#     print(f"I am {age} year old")
#     print(f"I have a pet {pet_name}")

# print_user_biography("Harmeet", 45, "Dog")
# print_user_biography("Harkirat", 44, "Tiger")
# print_user_biography("Amitoz", 43, "Cat")

# print_user_biography("Mouse", 43, "User_name")

# default value

# def prepare_meal(burger, fries_size = "S", drink = "Fanta"):
#     print(f"Prepare Meal with {burger} burger, Fries size: {fries_size}, Drink: {drink}")

# prepare_meal("Veggie Tikki")
# prepare_meal("Paneer Tikki")
# prepare_meal("Chicken Tikki", "L")
# prepare_meal("Falafel Tikki", "XL", "COKE")

# def kids_registration(name, days, dob_place = "Moga"):
#     print(f"Baby {name}, registerd with details Days: {days}, Place: {dob_place}")


# kids_registration("Johanas", 34)
# kids_registration("Bikkar", 2)
# kids_registration("Balkar", 58)
# kids_registration("Nanny", 1)

# def copy_documents(documents):
#     for doc in documents:
#         print(f"Copy {doc} successfully...")

# def copy_documents_2(documents):
#     for counter in range(0, len(documents)):
#         documents[counter] = "virus_" +  documents[counter]
#         print(f"Copy 2 Copmputer {documents[counter]} successfully...")

# documents = ["passport", "adhar", "pan", "marksheet", "dob", "dl"]

# copy_documents_2(documents[:])
# print("Orignal Documents...")
# print(documents)

# arbitrary arguments

# def food_court(dish, *extras): 
#     # samosas, [cholle, chutney, piyaaz, salad] ()
#     if len(extras) > 0:
#         print(f"Prepare {dish} with following items:") 
#         for item in extras:
#             print(item)
#     else:
#         print(f"Prepare {dish}")


# food_court("samosas", "cholle", "chutney", "piyaaz", "salad")
# food_court("samosas")

def print_details(**students_details):
    for key, value in students_details.items():
        print(f"{key} : {value}")

print_details(
    name = "Aman",
    age = "23",
    gender = "male"
)

print_details(
    name = "ashu",
    gender = "female"
)

print_details()