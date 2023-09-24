import random

n = int(input('введите ваше число- '))

lst = [random.randint(0, 25) for _ in range(10)]

print(lst)

if n in lst:
        print(lst.index(n))
else:
        print('-1')