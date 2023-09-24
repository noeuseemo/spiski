import random

lst = []

for i in range(10):
        lst.append(random.randint(0, 10))

print(max(lst))