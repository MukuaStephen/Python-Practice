import random

random_numbers = [random.randint (1,10) for _ in range(10)]
unique_numbers = set(random_numbers)
print ("random numbers", random_numbers)
print ("unique numbers", unique_numbers)