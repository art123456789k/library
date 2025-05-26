import sqlite3

def output_all(cursor):
    cursor.execute("""SELECT * FROM biblioteka ORDER BY title;""")
        
    rows = cursor.fetchall()
        
    u = 0

    for data in rows:
        u +=1
        
        print(str(u)+")",str(data[1])," ",str(data[2])," ",str(data[3])," ",str(data[4])," ")
def search(cursor):
    d = input("Автор: ")
    cursor.execute(f"""SELECT * FROM biblioteka  WHERE author = '{d}';""")
    
    rows = cursor.fetchall()
    u = 0

    for data in rows:
        u +=1
        
        print(str(u)+")",str(data[1])," ",str(data[2])," ",str(data[3])," ",str(data[4])," ")
def new_books(cursor):
    cursor.execute("""SELECT * FROM biblioteka WHERE year > 2010  ORDER BY title;""")

    rows = cursor.fetchall()
    u = 0

    for data in rows:
        u +=1
        
        print(str(u)+")",str(data[1])," ",str(data[2])," ",str(data[3])," ",str(data[4])," ")
def count(cursor):
    cursor.execute("""SELECT * FROM biblioteka ORDER BY title;""")

    rows = cursor.fetchall()
    u = 0

    for data in rows:
        u +=1
        
    print(u)
def genres(cursor):
    cursor.execute("""SELECT DISTINCT genre FROM biblioteka ;""")

    rows = cursor.fetchall()
    u = 0

    for data in rows:
        u +=1
        
        print(str(u)+")",data)
def delete(cursor):
    d = input("Название книги: ")
    cursor.execute(f"""DELETE FROM biblioteka  WHERE title = '{d}';""")
def update(cursor):
    d = input("Название книги: ")
    d2 = input("новый год:")
    cursor.execute(f"""UPDATE biblioteka SET year = {d2} WHERE title = {d};""")
def add(cursor):
    d = input("Название книги: ")
    d2 = input("Автор: ")
    d3 = input("Год издания: ")
    d4 = input("Жанр: ")
    cursor.execute(f"""INSERT INTO biblioteka (title,author,year,genre) VALUES ('{d}','{d2}',{d3},'{d4}');""")
def ARB(cursor):
    d = input("Введите ФИО читателя: ")
    b = input("Введите книгу: ")
    cursor.execute(f"INSERT INTO readers (name,books) VALUES ('{d}','{b}');")
def RBR(cursor):
    d = input("Введтите ФИО читателя: ")
    cursor.execute(f"""SELECT books FROM readers WHERE name = '{d}' ;""")
        
    rows = cursor.fetchall()
        
    u = 0

    for data in rows:
        u +=1
        
        print(str(u)+")",str(data[0]))
def DR(cursor):
    d = input("ФИО читателя: ")
    cursor.execute(f"""DELETE FROM readers WHERE name = '{d}';""")
while True:
    connection = sqlite3.connect('my_database.db')
    cursor = connection.cursor()


    dd = input('Выберите действие\n1-вывести книги\n2-найти книги по автору\n3-найти новые книги(позже 2010)\n4-кол-во разных книг в библиотеке\n5-жанры\n6-удалить книгу по названию\n7-изменить год издания\n8-добавить книгу \n9-добавить книгу читателю\n10-просмотреть книги читателя\n11-удалить читателя\n: ')
    if dd == "1": 
        output_all(cursor)
    if dd == "2":
        search(cursor)
    if dd == "3":
        new_books(cursor)
    if dd == "4":
        count(cursor)
    if dd == "5":
        genres(cursor)
    if dd == "6":
        delete(cursor)
    if dd == "7":
        update(cursor)
    if dd == "8":
        add(cursor)
    if dd == "9":
        ARB(cursor)
    if dd == "10":
        RBR(cursor)
    if dd == "11":
        DR(cursor)
    connection.commit()

    connection.close()