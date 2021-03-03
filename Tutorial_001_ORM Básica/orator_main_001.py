# -*- ISO-8859-1 -*-
#
# file: orator_main_001.py
#
# Created by Cleber Almeida Pereira
# e-mail: cleber.ap.desenvolvedor@gmail.com
#
# programming language: Python v3.7.3
#

"""
Utilizando Orator ORM de forma básica
Fonte: https://orator-orm.com/docs/0.9/basic_usage.html

Neste script vamos testar, de forma básica, a conexão com um banco de dados sqlite3 denominado 'person.db' previamente criado.
O banco de dados utilizado pode estar, ou não, vazio.
Neste caso o banco de dados possui uma única tabela 'person' que possui os campos:
- id INTEGER (autoincrement)
- name VARCHAR(20)
- last_name VARCHAR(30)
- sex CHAR
- birth_date DATE

Etapas desenvolvidas no algoritmo:
1º. importamos a biblioteca que realiza o gerenciamento;
2º. criamos a descrição da configuração de conexão do nosso banco de dados;
3º. instanciamos a classe do Orator responsável pelo gerenciamento do banco de dados;
4º. declarando as funções que rodam as queries;*
    - SELECT query
    - INSERT query
    - UPDATE query
        - atualiza pelo id (Esta função apresenta um tratamento para identificar quais campos serão atualizados.
    - DELETE query
        - deleta o registro do id informado
5º. declarando uma função menu para auxiliar na iteração e teste das outras funções;*
6º. uma função que executa um tipo 'formulário', ou simplesmente, que apresenta os campos para inserção dos valores;* 
7º. exibe cada registro separadamente, como se fosse uma tabela;*
8º. função tipo 'formulário' para atualização do registro;*
9º. função para deletar registro pelo id;*
* Estas funções foram criados para facilitar a iteração deste script de forma dinâmica;


FINAL. bloco de repetição para iteração neste script

"""

# 1º
from orator import DatabaseManager

# 2º
config = {
    'sqlite3':{
        'driver':'sqlite',
        'database': 'person.db'
        }
    }

# 3º
db = DatabaseManager(config)

# 4º 
# SELECT query
def select_person():
    results = db.select('SELECT * FROM person')
    # Retorna um lista de dicionários, onde cada chave é o nome do campo na entidade
    return results

# 4º 
# INSERT query
def insert_person(name=None, last_name=None, sex=None, birth_date=None):
    db.insert('INSERT INTO person (name, last_name, sex, birth_date) values (?,?,?,?)', [name,last_name,sex,birth_date])

# 4º 
# UPDATE query
def update_person_byId(person_id=None, name=None, last_name=None, sex=None, birth_date=None):

    # definindo variável com a query que será executada
    sql_query = 'UPDATE person SET '
    # declarando lista de valores necessários para a query final
    sql_list_values = []
    

    # Identificando quais campos serão atualizados
    # Se campo nome foi informado
    if name is not None:
        sql_query += 'name=?,'
        sql_list_values.append(name)    # adicionando novo valor para nome à lista
    
    # Se campo nome foi informado
    if last_name is not None:
        sql_query += 'last_name=?,'
        sql_list_values.append(last_name)    # adicionando novo valor para sobrenome à lista
    
    # Se campo nome foi informado
    if sex  is not None:
        sql_query += 'sex=?,'
        sql_list_values.append(sex)    # adicionando novo valor para sexo à lista
    
    # Se campo nome foi informado
    if birth_date is not None:
        sql_query += 'birth_date=?,'
        sql_list_values.append(birth_date)    # adicionando novo valor para data de nascimento à lista

    # removendo última 'vírgula' inserida
    sql_query = sql_query[:-1]

    # inserindo cláusula 'where' para o id e inserindo valor do id à lista
    sql_query += ' where id=?'
    sql_list_values.append(person_id)
    
    db.update(sql_query, sql_list_values)

# 4º 
# DELETE query
def delete_person_byId(person_id):
    db.delete('delete from person where id=?', [person_id])

# 5º
def menu():
    print("\n************ Algoritmo Finalizado ************\n")
    print("\n******************** MENU ********************\n")
    print("    1. Exibir os dados da tabela 'person'")
    print("    2. Inserir novo registro")
    print("    3. Atualizar um registro existente informando o ID")
    print("    4. Deletar um registro existente")
    print("    99. para sair")
    print()
    return int(input("Informe a opção desejada: "))

# 6º
def insert_form():
    print("\nCadastro de Pessoa - NOVO")
    name = input("nome: ")
    last_name = input("sobrenome: ")
    sex = input("sexo (M/F/I): ").upper()
    birth_date = input("data de nascimento (AAAA-mm-dd): ")

    insert_person(name, last_name, sex, birth_date)

# 7º
def view_person():
    print("\nRegistros da tabela 'person' ******************\n")
        
    lista_retornada = select_person()

    # Cabeçalho da tabela
    print("{:^5}{:<20}{:<30}{:^6}{:^20}".format('id', 'nome', 'sobrenome', 'sexo', 'data de nascimento'))
    
    for dict_registro in select_person():
        print("{:^5}{:<20}{:<30}{:^6}{:^20}".format(dict_registro['id'],dict_registro['name'],dict_registro['last_name'],dict_registro['sex'],dict_registro['birth_date']))
    print()

# 8º
def update_form():
    print("\nCadastro de Pessoa - ATUALIZAR")

    try:
        person_id = int(input("ID do registro que será atualizado: "))

        print("\n    Para os demais campos, tecle ENTER para não alterar.")
        name = input("nome: ")
        last_name = input("sobrenome: ")
        sex = input("sexo (M/F/I): ").upper()
        birth_date = input("data de nascimento (AAAA-mm-dd): ")
    except:
        person_id = 0
    

    # se id foi invalidado não atualiza registro
    if person_id == 0:
        print("  Atualização cancelada!")
    else: 
        if len(name) == 0:
            name = None

        if len(last_name) == 0:
            last_name = None
        
        if len(sex) == 0:
            sex = None
        
        if len(birth_date) == 0:
            birth_date = None
        
        #print("nome: {} - tipo: {}".format(name,type(name)))
        update_person_byId(person_id, name, last_name, sex, birth_date)

# 9º
def delete_form():
    print("\nCadastro de Pessoa - DELETAR")

    try:
        person_id = int(input("ID do registro que será deletado: "))
    except:
        person_id = 0

    if person_id == 0:
        print("  Deletar cancelado!")
    else:
        delete_person_byId(person_id)
    
# FINAL
executar_script = True # variável que tem a função de 'flag' (bandeira) para sinalizar a execução do laço de repetição
while executar_script:
    opcao = menu()

    if opcao == 1:
        view_person()
    elif opcao == 2:
        insert_form()
    elif opcao == 3:
        update_form()
    elif opcao == 4:
        delete_form()
    elif opcao == 99:
        executar_script = False

print("\n************ Algoritmo Finalizado ************\n")
