def r(n):
    b = bin(n)[2:]
    if n %2 == 0:
        b = '11' + b + '11'
    else:
        b = '1' + b + '00'
    return int(b, 2)
print(max(r(n) for n in range(1, 10000) if r(n) <= 113))
