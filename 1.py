# a = [x for x in range(2,101) if all(x % i !=0 for i in range(2, x) )]
# print(a)
a=[]
'''for x in range(2,101):
    for i in range(2,x):
        if x % i ==0:
            break
    else:
        a.append(x)
print(*a)'''
#оптимизировать
a=[]
for x in range(2,101):
    for i in range(2, int(x**0.5)+1):
        if x % i ==0:
            break
    else:
        a.append(x)
print(*a)
