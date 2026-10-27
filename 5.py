a = [3, 5, 4, 7, 1]
tecmax = a[0]
tecmin = a[0]
for el in a:
    if tecmax < el:
        tecmax = el
    if tecmin > el:
        tecmin = el
print(tecmax, tecmin)
print(max(a), min(a))