#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lsd = int(f"{number}"[-1])
if lsd > 5:
    print(f"Last digit of {number:d} is {lsd:d} and is greater than 5")
elif lsd == 0:
    print(f"Last digit of {number:d} is {lsd:d} and is 0")
else:
    print(f"Last digit of {number:d} is {lsd:d} and is less than 6 and not 0")
