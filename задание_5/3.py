def troy(n):
    a = ''
    while n:
        a = str(n%3) + a
        n = n // 3
    return a
def r(n):
    b = troy(n)
    if n % 3 == 0:
        b = b + b[(len(b)-2):]
    else:
        s = 0
        for i in b:
            s += int(i)
        b = b + troy(s)
    return int(b, 3)
print(min(r(n) for n in range(1,10000) if r(n) >208 and r(n)%2 != 0))
