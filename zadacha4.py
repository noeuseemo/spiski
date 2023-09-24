import random
lst = []

for i in range(10):
        lst.append(random.randint(0, 100))

summa = 0
proizvedenie = 1

for i in lst:
        summa += i
        proizvedenie *= i

print(summa, '\n', proizvedenie)