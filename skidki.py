def skidki():
    cena = float(input("enter summ: "))
    sale = float(input("enter sale(bez znaka %): "))
    if sale > 0 and cena > 0 :
        percent = cena / 100

        print(cena-percent*sale)
    else:
        print("ti tupoy?")
while True:
    skidki()