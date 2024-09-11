import sqlite3

class BancoDeDados:
    def __init__(self, par1="agenda.db"):
        self.nome_banco = par1
        self.conexão = sqlite3.connect(self.nome_banco)
        self.cursor = self.conexão.cursor()
        self.criar_tabela_pessoa()

    def criar_tabela_pessoa(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS pessoa (
                id INTEGER PRIMARY KEY,
                nome TEXT,
                telefone TEXT
            );
        """)
        self.conexão.commit()

    def fechar_conexão(self):
        if self.conexão:
            self.conexão.close()

class PessoaDAO:
    def __init__(self, db):
        self.db = db

    def create(self, nome, telefone):
        self.db.cursor.execute("INSERT INTO pessoa (nome, telefone) VALUES (?, ?)", (nome, telefone))
        self.db.conexão.commit()

    def read(self, id=None):
        if id:
            self.db.cursor.execute("SELECT * FROM pessoa WHERE id = ?", (id,))
            return self.db.cursor.fetchone()
        else:
            self.db.cursor.execute("SELECT * FROM pessoa")
            return self.db.cursor.fetchall()

    def update(self, id, nome, telefone):
        self.db.cursor.execute("UPDATE pessoa SET nome = ?, telefone = ? WHERE id = ?", (nome, telefone, id))
        self.db.conexão.commit()

    def delete(self, id):
        self.db.cursor.execute("DELETE FROM pessoa WHERE id = ?", (id,))
        self.db.conexão.commit()

# Usage example
db = BancoDeDados()
pessoa_dao = PessoaDAO(db)

while True:
    print("1. Adicionar pessoa")
    print("2. Listar pessoas")
    print("3. Atualizar pessoa")
    print("4. Deletar pessoa")
    print("5. Sair")
    opção = input("Escolha uma opção: ")

    if opção == "1":
        nome = input("Digite o nome da pessoa: ")
        telefone = input("Digite o telefone da pessoa: ")
        pessoa_dao.create(nome, telefone)
        print("Pessoa adicionada com sucesso!")

    elif opção == "2":
        pessoas = pessoa_dao.read()
        for pessoa in pessoas:
            print(f"ID: {pessoa[0]}, Nome: {pessoa[1]}, Telefone: {pessoa[2]}")

    elif opção == "3":
        id = int(input("Digite o ID da pessoa a ser atualizada: "))
        nome = input("Digite o novo nome da pessoa: ")
        telefone = input("Digite o novo telefone da pessoa: ")
        pessoa_dao.update(id, nome, telefone)
        print("Pessoa atualizada com sucesso!")

    elif opção == "4":
        id = int(input("Digite o ID da pessoa a ser deletada: "))
        pessoa_dao.delete(id)
        print("Pessoa deletada com sucesso!")

    elif opção == "5":
        break

    else:
        print("Opção inválida. Tente novamente!")

# Close the database connection
db.fechar_conexão()
