v = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
lst = []

for i in v:
        if i in v and i in c:
            lst.append(i)

print(lst)