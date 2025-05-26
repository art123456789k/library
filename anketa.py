
def anketa():
    name = input("name: ")
    if len(name) > 33:
        print("Тебя рил так зовут? \nЗаново напиши")
        name = input("name: ")
        if len(name) > 33:
            print("Ты закалибал!\nЗаново пиши(С НАЧАЛА!!!)")
            return 0 
    t = 34 - len(name)
    for i in range(0,t):
        name += " "
    try:
        age = int(input("age: "))
        
    except ValueError:
        print("пиши заново")
        try:
            age = int(input("age: "))
        except ValueError:
            print('пиши заново(с начала)')
            return 0
    if len(str(age))> 28 :
        print("Тебe рил столько? \nЗаново напиши")
        try:
            age = int(input("age: "))
        except ValueError:
            print("Ты закалибал!\nЗаново пиши(С НАЧАЛА!!!)")
            return 0 
        if len(str(age))> 28:
            print("Ты закалибал!\nЗаново пиши(С НАЧАЛА!!!)")
            return 0 
    ages = str(age)
    d = 29 - len(ages)
    for i in range(0,d):
        ages+= " "
    hobby = input("hobby: ")
    if len(hobby) > 26:
        print("Заново напиши(не более 26 символов)")
        hobby = input("hobby: ")
        if len(hobby) > 26:
            print("Ты закалибал!\nЗаново пиши(С НАЧАЛА!!!)")
            return 0 
    f = 27 - len(hobby)
    for i in range(0,f):
        hobby += " "
    try:
        contact = int(input("phone number: "))
        
    except:
        try:
            contact = int(input("phone number: "))

        except:
            print("Ты закалибал!\nЗаново пиши(С НАЧАЛА!!!)")
            return 0 
    contacs = str(contact)
    if len(contacs)> 24:
        print(" Не ври \nЗаново напиши")
        try:
            contact =int(input("phone number: "))
            contacs = str(contact)
        except:
            print("Ты закалибал!\nЗаново пиши(С НАЧАЛА!!!)")
            return 0
        if len(contacs)> 24:
            print("Ты закалибал!\nЗаново пиши(С НАЧАЛА!!!)")
            return 0 
    contacs = str(contact)
    g = 25 - len(contacs)
    for i in range(0,g):
        contacs+= " "
    print(f'-----------------------------------\n|{name}|\n|age: {ages}|\n|hobby: {hobby}|\n|contact: {contacs}|\n-----------------------------------')
while True:
    anketa()