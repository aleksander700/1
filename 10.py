a = 'abra cadabra fibra'
b = a.split()
o = 0
maxdl = ''
for i in b:
    if len(i)  > o:
        o = len(i)
        maxdl = i
print(maxdl, o)
        