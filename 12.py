import itertools

a = 'ABC'
k = 3
c = 0

words = itertools.product(a, repeat=k)

for el in words:
    word = "".join(el)
    c+=1
    
    
print(c)


print(list(itertools.permutations(a, 2)))