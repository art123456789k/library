def pokupki():
    lst = []
    while True:
        d = input("vvedite pokupki: ")
        if d == "stop":
            return lst
        else:
            lst.append(d)

print(pokupki())