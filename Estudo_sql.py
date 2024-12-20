import sqlite3
banco = sqlite3.connect('C:/Users/caina/Desktop/Estudos/sql_pasta/Estudo_sql.db')
cursor = banco.cursor()


cursor.execute ("INSERT INTO alunos VALUES ('luana', '18', 'luana@gmail.com')")

banco.commit()
cursor.execute ("SELECT*FROM alunos")
print(cursor.fetchall())




