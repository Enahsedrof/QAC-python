import math
from random import randint
from math import remainder as rem

def multiply_pi():
    return randint(1,10) * math.pi

for i in range(5):
    print(multiply_pi())

print("--------------------")
print(rem(8,4))