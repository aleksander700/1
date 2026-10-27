a = 'aabbccAABBCC'
kolzam = a.count('a') + a.count('b') + a.count('A') + a.count('B')
a = a.replace('a', '1')
a = a.replace('b', 'a')
a = a.replace('1', 'b')
a = a.replace('A', '2')
a = a.replace('B', 'A')
a = a.replace('2', 'B')
print(a, kolzam)
