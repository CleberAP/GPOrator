# -*- ISO-8859-1 -*-
#
# file: orator_main_002.py
#
# Created by Cleber Almeida Pereira
# e-mail: cleber.ap.desenvolvedor@gmail.com
#
# programming language: Python v3.7.3
#

"""
Utilizando Query Builder do Orator
Fonte: https://orator-orm.com/docs/0.9/query_builder.html

A tradução de Query Builder do inglês para o português é "construtor de consulta de banco de dados".
Este construtor disponibiliza uma maneiro mais fácil para criar e executar consultas de banco de dados.

O banco de dados utilizado ainda possui uma única tabela 'person' na qual foi adicionada mais um campo:
- age INTEGER

Etapas desenvolvidas no algoritmo:
1º. importamos a biblioteca que realiza o gerenciamento;
2º. criamos a descrição da configuração de conexão do nosso banco de dados;
3º. instanciamos a classe do Orator responsável pelo gerenciamento do banco de dados;
4º. declarando as funções que rodam as queries;*
    - SELECT Query Builder
    - INSERT Query Builder
    - UPDATE Query Builder
        - atualiza pelo id (Esta função apresenta um tratamento para identificar quais campos serão atualizados.
    - DELETE Query Builder
        - deleta o registro do id informado
    - INCREMENT Query Builder
    - DECREMENT Query Builder
5º. declarando uma função menu para auxiliar na iteração e teste das outras funções;*
6º. uma função que executa um tipo 'formulário', ou simplesmente, que apresenta os campos para inserção dos valores;* 
7º. exibe cada registro separadamente, como se fosse uma tabela;*
8º. função tipo 'formulário' para atualização do registro;*
9º. função para deletar registro pelo id;*
10º. função para incrementar (aumentar) a idade;
11º. função para decrementar (diminuir) a idade;
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
# SELECT Query Builder
def select_person():
    # Retorna um lista de dicionários com todos os registros (linhas), onde cada chave é o nome do campo na entidade
    return db.table('person').get()

# 4º 
# INSERT Query Builder
def insert_person(fields_dict):
    db.table('person').insert(fields_dict)

# 4º 
# UPDATE Query Builder
def update_person_byId(person_id, fields_dict):
    db.table('person').where('id', person_id).update(fields_dict)

# 4º 
# DELETE Query Builder
def delete_person_byId(person_id):
    db.table('person').where('id','=',person_id).delete()

# 4º
# INCREMENT Query Builder
def increment_age(increment_age=None, person_id=None):
    # Se não foi informado valor para incrementar a idade
    if increment_age is None:
        db.table('person').where('id','=',person_id).increment('age')
    else:
        db.table('person').where('id','=',person_id).increment('age', increment_age)

# 4º   
# DECREMENT Query Builder
def decrement_age(decrement_age=None, person_id=None):
    # Se não foi informado valor para incrementar a idade
    if decrement_age is None:
        db.table('person').where('id','=',person_id).decrement('age')
    else:
        db.table('person').where('id','=',person_id).decrement('age', decrement_age)


# 5º
def menu():
    print("\n******************** MENU ********************\n")
    print("    1. Exibir os dados da tabela 'person'")
    print("    2. Inserir novo registro")
    print("    3. Atualizar um registro existente informando o ID")
    print("    4. Deletar um registro existente")
    print("    5. Aumenta idade da pessoa")
    print("    6. Diminui idade da pessoa")
    print("    99. para sair")
    print()
    return int(input("Informe a opção desejada: "))

# 6º
def insert_form():
    print("\nCadastro de Pessoa - NOVO")
    # a função input captura o que foi digitado como tipo texto (string)
    name = input("nome: ")
    last_name = input("sobrenome: ")
    sex = input("sexo (M/F/I): ").upper()
    age = int(input("idade: ") or "0") # lê o valor digitado ou, se teclado ENTER, insere o valor '0' e converte para tipo inteiro
    birth_date = input("data de nascimento (AAAA-mm-dd): ")

    dicionario_de_campos = {
        'name': name,
        'last_name': last_name,
        'sex': sex,
        'birth_date': birth_date,
        'age': age
        }

    insert_person(dicionario_de_campos)

# 7º
def view_person():
    print("\nRegistros da tabela 'person' ******************\n")
        
    # Cabeçalho da tabela
    print("{:^5}{:<20}{:<20}{:^6}{:^20}{:^5}".format('id', 'nome', 'sobrenome', 'sexo', 'data de nascimento','idade'))
    
    for dict_registro in select_person():
        print("{:^5}{:<20}{:<20}{:^6}{:^20}{:^5}".format(dict_registro['id'], dict_registro['name'], dict_registro['last_name'], dict_registro['sex'], dict_registro['birth_date'], dict_registro['age']))
    print()

# 8º
def update_form():

    dicionario_de_campos = {}
    
    print("\nCadastro de Pessoa - ATUALIZAR")

    try:
        person_id = int(input("ID do registro que será atualizado: "))

        print("\n    Para os demais campos, tecle ENTER para não alterar.")
        name = input("nome: ")
        last_name = input("sobrenome: ")
        sex = input("sexo (M/F/I): ").upper()
        birth_date = input("data de nascimento (AAAA-mm-dd): ")
        age = int(input("idade: ") or "0") # lê o valor digitado ou, se teclado ENTER, insere o valor '0' e converte para tipo inteiro

    except:
        person_id = 0
    

    # se id foi invalidado não atualiza registro
    if person_id == 0:
        print("  Atualização cancelada!")
    else: 
        if len(name) != 0:
            dicionario_de_campos['name'] = name

        if len(last_name) != 0:
            dicionario_de_campos['last_name'] = last_name
        
        if len(sex) != 0:
            dicionario_de_campos['sex'] = sex
        
        if len(birth_date) != 0:
            dicionario_de_campos['birth_date'] = birth_date

        if age > 0:
            dicionario_de_campos['age'] = age
        
        update_person_byId(person_id, dicionario_de_campos)

# 9º
def delete_form():
    print("\nCadastro de Pessoa - DELETAR")

    try:
        person_id = int(input("ID do registro que será deletado: "))
    except:
        person_id = 0

    # Se id não é válido então operação não é realizada
    if person_id == 0:
        print("  Deletar cancelado!")
    else:
        delete_person_byId(person_id)

# 10º
def increment_age_formById():
    print("\nCadastro de Pessoa - Aumentar Idade")

    try:
        person_id = int(input("ID do registro: "))
        #person_name = input("Nome: ")
    except:
        person_id = 0

    try:
        increment_value = int(input("Informe em quantos anos deseja aumentar: "))
    except:
        increment_value = None

    # Se id não é válido então operação não é realizada
    if person_id == 0:
        print("  Incrementar idade cancelado!")
    else:
        increment_age(increment_value, person_id)

# 11º
def decrement_age_formById():
    print("\nCadastro de Pessoa - Diminuir Idade")

    try:
        person_id = int(input("ID do registro: "))
        #person_name = input("Nome: ")
    except:
        person_id = 0

    try:
        decrement_value = int(input("Informe em quantos anos deseja diminuir: "))
    except:
        decrement_value = None

    # Se id não é válido então operação não é realizada
    if person_id == 0:
        print("  Decrementar idade cancelado!")
    else:
        decrement_age(decrement_value, person_id)
    

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
    elif opcao == 5:
        increment_age_formById()
    elif opcao == 6:
        decrement_age_formById()
    elif opcao == 99:
        executar_script = False

print("\n************ Algoritmo Finalizado ************\n")
