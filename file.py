import uuid
import psycopg2
def task_list():
  try:
      conn = psycopg2.connect(dbname='citizix_db', user='citizix_user', host='localhost', password='S3cret')
      print("подключение прошло успешно")
  except:
      print("I am unable to connect to the database")
  cur = conn.cursor()
  cur.execute("""SELECT * FROM users 
  ORDER BY status;""")
  conn.commit()
  rows = cur.fetchall()
  u = 0
  
  for data in rows:
    u +=1
    if data[2] == True:
      print(str(u)+")",str(data[1])+":", "V")
    else:
      print(str(u)+")",str(data[1])+":", "X")

  
    
  d = input("Введите действие (1-удалить задание, 2-переименовать, 3-обновить статус, 4-добавить задание): ")
  if d == "1":
    delete_task(conn,d, rows)
  if d == "2":
    update_task(conn,d,rows)
  if d == "3":
    update_status(conn,d,rows)
  if d == "4":
    add_task(conn,d, u)
  

def delete_task(conn, d,rows):
  try:
    dd = int(input("Введите номер задания для удаления: "))
    gf = rows[dd-1]
    conn.cursor().execute(f"DELETE FROM users WHERE id ={gf[0]}; ")
    conn.commit()
    print("успешно удалено")
  except:
    delete_task(conn,d,rows)
  

def update_status(conn,d, rows):
  dd = int(input("Введите id задания для обновления: "))
  print(rows)
  fg = rows[dd-1]
  print(fg)
  
  conn.cursor().execute(f"UPDATE users SET status = True WHERE id = {int(fg[0])}; ")
  conn.commit()
  print("успешно обновлено")

def update_task(conn,d, rows):
  try:
    dd = int(input("Введите название задания для переименования: "))
    dd2 = input("Введите новое имя для переименования: ")
    fg = rows[dd-1]
    conn.cursor().execute(f"UPDATE users SET task = '{dd2}' WHERE id = {fg[0]} ;")
    conn.commit()
    print("успешно переименовавно")
  except:
    update_task(conn,d, rows)

def add_task(conn,d, u):
  
  try:
    dd2 = input("Введите имя задания для добавления: ")
    
    conn.cursor().execute(f"INSERT INTO users (task,status) VALUES ('{dd2}',False);")
    conn.commit()
  except:
    add_task(conn,d, u)
      
  print("успешно обновлено")
  
while True:
  task_list()