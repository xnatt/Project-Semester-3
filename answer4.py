age = int(input("Please enter your age: "))
if age <= 19:
    print("You qualify for student discounts.")
elif 20 <= age <= 54:
    print("You don't qualify for age-related discounts.")
else:
    print("You can receive senior discounts.")
    