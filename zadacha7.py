import random
lst = []
for i in range(10):
        
        lst.append(random.randint(0, 100))

lst2 = lst.copy()

maximum = lst.index(max(lst))

minimum = lst.index(min(lst))

lst2[maximum] = min(lst)


lst2[minimum] = max(lst)

print(lst)
print(lst2)