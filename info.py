def user_info (name, age):
    """Prints user information"""
    print (f"Name: {name}")
    if age >= 18:
        print (f"Age: {age}")
    else:
        print (f"Age: {age} (minor)")

name = input("Enter your name?")
age = int(input("Enter your age?"))
user_info(name, age)

