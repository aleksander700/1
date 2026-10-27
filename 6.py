a = [-2, -1, 4, 3, 5, 6, 2]
chetmax = a[0]
minchet = a[0] # -2
for el in a: # el = 2
    if el  > 0 and el % 2 ==0:
        if el > chetmax:
            chetmax = el
        if el < minchet or (minchet < 0 or minchet % 2 != 0): # 2 < -2 or -2 < 0
            minchet = el # 4
if chetmax == a[0]:
    print(-1, -1)
else:
    print(chetmax, minchet)
