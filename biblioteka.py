import sqlite3
import datetime


def menu():
    print('''    ______________МЕНЮ_______________
    1-вывести книги                  |
    2-найти книги по автору          |
    3-найти новые книги(позже 2010)  |
    4-кол-во разных книг в библиотеке|
    5-жанры                          |
    6-удалить книгу по названию      |
    7-изменить год издания           |
    8-добавить книгу                 |
    9-добавить книгу читателю        |
    10-просмотреть книги читателя    |
    11-удалить читателя              |
    12-просмотр просроченных книг    |
    _________________________________| ''')
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
    b = input("Введите название книги: ")
    D = input("Введите срок сдачи в формате(YYYY.MM.DD): ")
    
    cursor.execute(f"SELECT * FROM biblioteka WHERE title = '{b}'")
    rows = cursor.fetchall()
    u = 0
    
    for data in rows:
        u +=1
        if data[0]:
            cursor.execute(f"INSERT INTO readers (name) VALUES ('{d}');")
            cursor.execute(f"INSERT INTO lol (due_date)VALUES ('{D}');")
    if u == 0:
        print("Такой книги нет!")
        ARB(cursor)    
def RBR(cursor):
    d = input("Введтите ФИО читателя: ")
    cursor.execute(f"""SELECT readers.name,biblioteka.title,lol.due_date  FROM readers  INNER JOIN lol ON lol.book_id = readers.id INNER JOIN biblioteka ON readers.id != -3  WHERE readers.name = '{d}' ;""")
    
    rows = cursor.fetchall()
        
    u = 0

    for data in rows:
        u +=1
        
        print(str(u)+")",str(data[0])," ",str(data[1])," до",str(data[2]))
def DR(cursor):

    d = input("ФИО читателя: ")
    cursor.execute(f"""DELETE FROM readers WHERE name = '{d}';""")
def VOB(cursor):
    d = input("Введите ФИО читателя: ")
    cursor.execute(f"SELECT biblioteka.title,biblioteka.author,biblioteka.year,biblioteka.genre FROM readers INNER JOIN biblioteka ON biblioteka.id = readers.id INNER JOIN lol ON lol.book_id = readers.id  WHERE name = '{d}' AND lol.due_date < datetime('now'); ")

    rows = cursor.fetchall()

    u = 0

    for data in rows:
        u +=1
        
        print(str(u)+")",str(data[0])," ",str(data[1])," ",str(data[2])," ",str(data[3]))

dd = 0
while True:
    connection = sqlite3.connect('m.db')
    cursor = connection.cursor()

    
    menu()
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
    if dd == "12":
        VOB(cursor)
    
    dd = input(':')
    
    connection.commit()

    connection.close()