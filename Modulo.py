import requests, json, scripts, os
from time import sleep

flag_menu = True
lista_de_filmes = []

while flag_menu:

    scripts.menu()

    escolha = str(input('Digite o que deseja: '))

    if escolha == '1':

        scripts.adicionar_filme()
        
    elif escolha == '2':

        scripts.deletar_filme()
    
    elif escolha == '3':

       scripts.visualizar_lista_de_desejos()

    elif escolha == '4':
        
        scripts.buscar_filme()          

    elif escolha == '5':
        
        scripts.status()

    elif escolha == '6':
        
        scripts.sugestoes_com_base_no_ultimo_filme_adicionado()   

    elif escolha == '7':

        scripts.sugestoes_com_base_em_todos_os_filmes_adicionados()

    elif escolha == '8':

        print('\nAté um outro dia...... Um triste amanhã...... :)\n')
        flag_menu = False 

    else:
        print('\nOpção inválida, por favor, escolha uma opção válida!.')