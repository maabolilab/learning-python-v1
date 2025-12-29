full_name = input("Enter your name: ")
grade = int(input("Enter your percentage: "))

if grade >= 95:
    print(f"Wow!, {full_name}, you are selected for A grade college")
elif grade >= 85 and grade < 95:
    print(f"Congratulations, {full_name}, you are selected for B grade college")
elif grade >= 70 and grade < 85:
    print(f"{full_name}, you are selected for C grade college")
else:
    print(f"Sorry!!, {full_name}, you are selected for D grade college")