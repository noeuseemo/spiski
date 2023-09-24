
import random

lst = []

for i in range(10):
        
        lst.append(random.randint(0, 10))

print(lst)

for i in lst:
        
        if lst.count(i) > 1:
            
            
            print(i)