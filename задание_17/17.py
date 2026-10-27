a = 0
with open('task1.txt', 'r') as file:
    for line in file:
        number = int(line.strip())
        n = number
        summ = 0
        while n:
            summ += n % 10
            n //= 10
        if number % 5 == 0 and summ % 3 == 0 and 10000 < number < 56000:
            if number > a:
                a = number
print(a)
