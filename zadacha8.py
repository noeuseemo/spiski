n = int(input('введите ваше число- '))
lst = []
lst2 = []

for i in range(n):
        
        chislo = int(input('число '))
        
        lst.append(chislo)

for i in range(len(lst)):
        
        if i % 2 != 0:
            
            lst2.append(i)
        


for i in lst2:
        
        lst.pop(i)

print(lst)