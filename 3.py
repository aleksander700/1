import random
A, B, N =map(int, input().split())
a = [random.randint(A, B) for i in range(N)]
chet = 0
nechet = 0
for num in a:
    if num %2 ==0:
        chet += 1
    else:
        nechet += 1
print(*a)
print(chet, nechet)
