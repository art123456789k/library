def t(tr):
    print(tr)
    if tr > 0:
        tr -= 1
        
        t(tr)
    else:
        return 0 
tr = int(input("vvedite chislo: "))
t(tr)