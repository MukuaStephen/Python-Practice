def greet( name = "This is KCB Mobile Banking."):
    """prints a greeting message"""
    print(f"Hello, {name}")

greet()
name = input("Enter your name?")
greet(name)