import sqlite3 as conector
from modelo import Pessoa

# Abertura de conexão e aquisição de cursor
try:
    conexao = conector.connect("./meu_banco.db")
    cursor = conexao.cursor()

    #Criar tabela Pessoa
    comando = ''' CREATE TABLE Pessoa (
cpf INTEGER NOT NULL,
nome TEXT NOT NULL,
nascimento DATE NOT NULL,
oculos BOOLEAN NOT NULL,
PRIMARY KEY (cpf)
); '''
    cursor.execute(comando)


    # Criar tabela Marca
    comando = ''' CREATE TABLE Marca (
    id INTEGER NOT NULL,
    nome TEXT NOT NULL,
    sigla CHARACTER(2) NOT NULL,
    PRIMARY KEY (id)
    ); '''
    cursor.execute(comando)


    # Criar tabela Veiculo
    comando = ''' CREATE TABLE Veiculo (
placa CHARACTER(7) NOT NULL,
ano INTEGER NOT NULL,
cor TEXT NOT NULL,
proprietario INTEGER NOT NULL,
marca INTEGER NOT NULL,
PRIMARY KEY (placa),
FOREIGN KEY(proprietario) REFERENCES Pessoa(cpf),
FOREIGN KEY(marca) REFERENCES Marca(id)
); '''
    cursor.execute(comando)

    #Efetivação dos comandos
    conexao.commit()



    #Inserindo dados na tabela pessoa
    comando = ''' INSERT INTO Pessoa (cpf, nome, nascimento, oculos)
VALUES (12345678900, 'João', '2000-01-31', 1); '''
    cursor.execute(comando)

    comando = ''' INSERT INTO Pessoa (cpf, nome, nascimento, oculos)
VALUES (10000000099, 'Maria', '1990-01-31', 0); '''
    cursor.execute(comando)

    comando = ''' INSERT INTO Pessoa (cpf, nome, nascimento, oculos)
VALUES (20000000099,'José','1990-02-28',0); '''
    cursor.execute(comando)

    comando = ''' INSERT INTO Pessoa (cpf, nome, nascimento, oculos)
VALUES (30000000099,'Silva','1990-03-30',1); '''
    cursor.execute(comando)


    #Efetivação dos comandos
    conexao.commit()


except conector.DatabaseError as erro:
    print("Erro no Banco de dados", erro)

finally:
    #Fechamento das conexões
    if conexao:
        cursor.close()
        conexao.close()


from modelo import Veiculo
from modelo import Marca

try:
    conexao = conector.connect("./meu_banco.db")
    conexao.execute("PRAGMA foreign_keys = on")
    cursor= conexao.cursor()

    #Inserindo dados na tabela Marca
    comando1 = ''' INSERT INTO Marca (nome, sigla) VALUES (:nome, :sigla);'''

    marca1 = Marca ("Marca A", "MA")
    cursor.execute(comando1, vars(marca1))
    marca1.id = cursor.lastrowid

    marca2 = Marca("Marca B", "MB")
    cursor.execute(comando1, vars(marca2))
    marca2.id = cursor.lastrowid


    #Inserindo dados na tabela Veiculo
    comando2 = ''' INSERT INTO Veiculo VALUES (:placa, :ano, :cor, :proprietario, :marca);'''

    veiculo1= Veiculo('AAA0001', 2001, 'Prata', 10000000099, marca1.id)
    veiculo2= Veiculo('BAA0002', 2002, 'Preto', 10000000099, marca1.id)
    veiculo3= Veiculo('CAA0003', 2003, 'Branco', 20000000099, marca2.id)
    veiculo4= Veiculo('DAA0004', 2004, 'Azul', 30000000099, marca2.id)
    cursor.execute(comando2, vars(veiculo1))
    cursor.execute(comando2, vars(veiculo2))
    cursor.execute(comando2, vars(veiculo3))
    cursor.execute(comando2, vars(veiculo4))

    #Efetivando comandos
    conexao.commit()

except conector.DatabaseError as erro:
    print("Erro no Banco de dados", erro)

finally:
    #Fechamento das conexões
    if conexao:
        cursor.close()
        conexao.close()

