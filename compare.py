value = input("Enter a value:")
try:
    value = int(value)
except ValueError:
    try:
        value = float(value)
    except ValueError:
        pass

match value:
    case int():
        print("You have entered an integer:", value)
    case str():
        print("You have entered a string:", value)
    case float():
        print("You have entered a float:", value)
    case _:
        print("Invalid data typ entered.")