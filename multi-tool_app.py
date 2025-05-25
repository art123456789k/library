def calc():
    D = input("enter mathematical example: ")
    for i in D:
        if i == "-":
            print(float(D.split("-")[0])-float(D.split("-")[1]))
        if i == "+":
            print(float(D.split("+")[0])+float(D.split("+")[1]))
        if i == "*":
            print(float(D.split("*")[0])*float(D.split("*")[1]))
        if i == "/":
            print(float(D.split("/")[0])-float(D.split("/")[1]))
        

while True:
    calc()