s = "1234 4567" # индексы как в списках
print("12"+"23") # 1223
print("12"*3) #121212
a = 12
print(f"значение выражения равнятся: {a} .")
print(s.find("23"))
if "12" in s:
    print(True)
b = s.split() # b = ["1234", "4567"]
c = ".".join(b)
print(c)
# строки - неизменяемый тип данных
s = s.replace("2", "0", 1)
s = s.replace("4", "10")
print(c.count("4"))
f = " 34536 "
f = f.strip()
g = "qwebdskbksd jdlgjsbkdf;nld;ldnskjkds"
print(g.count("sk"))