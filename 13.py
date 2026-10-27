file = input()
y = input()
tochka = file.rfind('.')
if tochka == -1:
    file = file + '.' + y
else:
    file = file[:tochka] + '.' + y
print(file)


# f = file.split(".")
# if len(f) > 1:
#     file = file + y
# else:
#     f[-1] = y
#     file = ".".join(f)