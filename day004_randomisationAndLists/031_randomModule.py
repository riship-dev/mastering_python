'''
- Python creates pseudo random numbers using Mersenne Twister method.
'''

'''
import random
import myModule # Import another py file in same directory

print(random.randint(1, 10)) # Random whole numbers, both inclusive
print(myModule.number)

print(random.random()) # 0.0 to 1.0
print(random.random() * 10) # 0.0 to 10.0
print(random.uniform(1, 10)) # random float
'''

import random

if random.randint(0, 1):
    print("head")
else:
    print("tail")