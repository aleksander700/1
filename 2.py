import random
A, B, N, K =map(int, input().split())
a = [random.randint(A, B) for i in range(N)]
k = 0
for x in a:
    summ = 0
    n = abs(x)
    while n > 0:
        summ += n % 10
        n //= 10
    if x == 0:
        summ = 0
    if summ == K:
        k += 1
print(*a)
print(k)
