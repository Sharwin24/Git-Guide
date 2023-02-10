import random

# Generate a random number between 0 and 100 and print it
random_number = random.randint(0, 100)
# print(random_number)

# Generate another random number between 0 and 6
# and multiply it by our previous number
print(random_number * random.randint(0, 6))