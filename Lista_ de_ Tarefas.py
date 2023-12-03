'''Crie um programa que permita aos usuários gerenciarem uma lista de tarefas. Os 
usuários devem poder adicionar, listar e marcar tarefas como concluídas. Use um 
dicionário onde as chaves são as tarefas e os valores indicam se a tarefa foi concluída 
ou não.'''

import os
os.system('cls')

lista = {'tarefas': [], 'concluidas': []}
escolha = 0

menu = ('Menu: \n'
    '1. Adicionar tarefa \n'
    '2. Remover tarefa \n'
    '3. Listar tarefas pendentes \n'
    '4. Listar tarefas concluídas \n'
    '5. Sair \n')

print(menu)



while escolha != 4:
    escolha = int(input('Informe a opção: '))
    if escolha == 1:
        tarefa = input('Descreva a tarefa: ')
        lista['tarefas'].append(tarefa)
        print('Tarefa adicionada com sucesso !')
    elif escolha == 2:
        if len(lista) == 0:
            print('Não tem tarefas !')
        else:
            print(lista)
            tarefa_removida = input('Informe a tarefa que deseja remover: ')
            lista['tarefas'].remove(tarefa_removida)
            print(f"A tarefa '{tarefa_removida}' foi removida com sucesso!")
            print(lista)
    elif escolha == 3:
        if len(lista) == 0:
            print('Não tem tarefas pendentes.')
        else:
            print('Tarefas pendentes:')
            for i, tarefa in enumerate(lista['tarefas']):
                print(f"{i+1}. {tarefa}")
            print()
    elif escolha == 4:
        print(lista)
        tarefa_concluida = input('Informe a tarefa que deseja concluir: ')
        lista['concluidas'].append(tarefa_concluida)
        print(f"A tarefa '{tarefa_concluida}' foi concluir com sucesso!")
        print(lista['concluidas'])
        
    elif escolha == 5:
        print("Aplicativo encerrado.")
        break
    else:
        print('Opção invalida')
        

        
        