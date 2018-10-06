import mysql.connector

con = mysql.connector.connector(user='noc', password='concrete123', host='127.0.0.1', database='agenda')
cur = con.cursor()

def db_create():

#Se nao existe cria a tabela
    cur.execute("CREATE TABLE IF NOT EXISTS agenda (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), phone VARCHAR(15))")


#Criar os dados na tabela
    try: 
        data = [
            ('Fred', '(21)12345678'),
            ('Vilma', '(22)9876367'),
            ('Carlos', '(23)9993871')
            ]
        cur.execute("""INSERT INTO agenda
            values (?, ?)""", data)
    except:
        print("dados existem")
        pass
    con.close()

def db_select():
    cur.execute("SELECT * FROM TABLE agenda")
    array = []
    for data in cur:
        array.append(data)
    return array




