full_name = input("Enter your name: ")
age = input("Enter your age: ")

new_age = int(age)

if new_age > 18:
    print(f"{full_name} your are eligble for voting")       
else:
    print(f"Sorry, {full_name} you are just a kid")