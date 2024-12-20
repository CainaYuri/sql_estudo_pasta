import sqlite3, time
banco = sqlite3.connect ('C:/Users/caina/Desktop/Estudos/sql_pasta/agenda.db')
cursor = banco.cursor()

def criar_db():
    cursor.execute("CREATE TABLE IF NOT  EXISTS  cadastro (Nome text, Telefone varchar, Email text, Data text)")

try:
    criar_db()
except:
    print("erro ao criar agenda")
else:
    print("Criação da agenda ok")

def pesquisar(p):
    sql = 'SELECT*FROM cadastro WHERE nome = ?'
    for row in cursor.execute(sql, (p,)):
        print(row)


    
def inserir(n,t,e):
    d = time.strftime("%d/%m/%Y")
    cursor.execute( "INSERT INTO cadastro VALUES(?,?,?,?)",(n,t,e,d))
    banco.commit()

fc = int(input("1-cadastro\n 2-pesquisar \n Selecione uma opção: "))

if fc == 1:

    try:
        print("Cadastro Agenda")
        time.sleep(3)
        n = str(input("informe seu nome:"))
        t = str(input("informe seu telefone: "))
        e = str(input("informe seu email: "))
        inserir(n,t,e)

    except:
        print("Erro ao efetuar cadastro")
    else: 
        print("Cadastro realizado com suceso")
        
elif fc == 2:
    print()
    p = str(input("informe o nome a ser pesquisad0: "))
    pesquisar(p)



