opção = 0
print('-' * 30)
print(f'{"\033[1;36mGerenciador de tarefas\033[m":^40}')
print('-' * 30)
print(f'{"\033[1;34mMENU\033[m":^32}')
while opção != 4:
    print(''' Escolha uma das opções
        [ 1 ] Adicionar
        [ 2 ] Exibir
        [ 3 ] Remover
        [ 4 ] Sair''')
    opção = int(input('----> Qual opção <---- '))
    if opção == 1:
        adicionar = str(input('O que deseja adicionar? '))
        print(f'{adicionar} Adicionado Com Sucesso!!!')
    for i, tarefa in enumerate(tarefa):
        
        




