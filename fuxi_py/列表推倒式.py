# coding=utf-8
i = 1
b = []
while i<98:
    a = [x for x in range(i,i+3)]
    i +=3
    b.append(a)

print(b)