from random import randint
c=0
for i in range(1000):
    a=[False for i in range(100)]
    a[randint(0,99)]=True

    b=[]
    b.append(a[0])
    for i in range(1,99):
        if a[i]:
            b.append(True)

    if len(b) > 1:
        if b[1]:
            c+=1

print(c,"\b/1000")