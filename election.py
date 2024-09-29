def has_id():
    response = input("Do you have a valid ID? (yes/no): ").strip().lower()
    return response == "yes"
age = input("Pleae enter your age?:")
age = int(age)
if age >=18:
    if has_id():
        print("You are eligible to vote!")
    else:
        print("You need a valid ID to vote. You are not eligible to vote!")
else:
        print("You are not eligible to vote!")