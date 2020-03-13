import requests, json, time
from time import sleep

def menu():
  
    print('\n****** Bem vindo(a) a sua lista de desejos! ******')
    print('*** Adicionar filme a lista de desejos: [1] ***')
    print('*** Deletar filme da lista de desejos: [2] ***')
    print('*** Visualizar a lista de desejos: [3] ***')
    print('*** Buscar filme na lista de desejos: [4] ***')
    print('*** Atualizar status de filme da lista de desejos: [5] ***')
    print('*** Sair da lista de desejos: [6] ***')
    print('***********************************************\n')

def status():

    flag_status = True

    title = str(input('\nDigite o nome do filme que deseja alterar o status de visualização: ')).title().strip()
        
    try:    
        
        with open('lista_de_desejos.json') as arquivo:
            
            reference = json.load(arquivo)

            for item in reference:
                
                if title == item['Titulo']:
                        
                    print('\nOpções de status de visualização: ')
                    print('\nAssistido [1]')
                    print('Não assistido [2]')
                    print('Assistir mais tarde [3]\n')
                        
                    escolha_de_status = input('Digite o número da escolha de status desejada: ')

                    if escolha_de_status == '1':

                        item['Status de visualizacao'] = 'Assistido'

                        with open('lista_de_desejos.json', 'w') as arquivo:    
                            json.dump(reference, arquivo, indent=4)
                            print('\nStatus atualizado!')
                            voltando_ao_menu()

                    elif escolha_de_status == '2':

                        item['Status de visualizacao'] = 'Nao assistido'
                            
                        with open('lista_de_desejos.json', 'w') as arquivo:    
                            json.dump(reference, arquivo, indent=4)
                            print('\nStatus atualizado!')
                            voltando_ao_menu()

                    elif escolha_de_status == '3':

                        item['Status de visualizacao'] = 'Assistir mais tarde' 
                            
                        with open('lista_de_desejos.json', 'w') as arquivo:    
                            json.dump(reference, arquivo, indent=4)
                            print('\nStatus atualizado!')
                            voltando_ao_menu()

                        
                    else:
                        
                        print('\nOpção inválida.')
                        voltando_ao_menu()
                else:
                        
                    flag_status = False               
            
                if flag_status == False:
                    
                    print('\nVocê não possui esse filme na sua lista')
                    voltando_ao_menu()

                else:
                    pass    

    except FileNotFoundError:
        
        print('\nVocê ainda não possui uma lista de desejos. ):')  
        voltando_ao_menu()    

def voltando_ao_menu():  
    
    print('\nRetornando ao menu...')
    sleep(2)          

def visualizar_lista_de_desejos():

    try:
            
        flag = True

        with open('lista_de_desejos.json') as arquivo_tres:
            reference_tres = json.load(arquivo_tres)
                      
            if len(reference_tres) == 0:
                print('\nVocê não tem nenhum filme na sua lista de desejos!')
                flag = False
                           
            if flag:

                    print(f'\nVocê possui {len(reference_tres)} filme(s) na sua lista de desejos.')
                    print('\nO(s) filme(s) na sua lista é(são):')
                    print(json.dumps(reference_tres, indent=4, separators = (". ", " = ")))
            
            else:
                pass

            voltando_ao_menu()

    except FileNotFoundError:
        
        print('\nNenhuma lista de desejos encontrada. ):')
        voltando_ao_menu()
        
def buscar_filme():

    filme_desejado = str(input('\nDigite o nome do filme que deseja buscar na sua lista de desejos: ')).title().strip()
        
    flag_quatro = True
        
    try:
        with open('lista_de_desejos.json') as arquivo_tres:
            reference_quatro = json.load(arquivo_tres)

        for filme_na_lista in reference_quatro:
               
            if filme_desejado == filme_na_lista['Titulo']:
                
                flag_quatro = False
                print(json.dumps(filme_na_lista, indent=4, separators = (". ", " = ")))
                voltando_ao_menu()

            else:
                
                pass    
            
        if flag_quatro == True:
            
            print('\nVocê não possui este filme na sua lista de desejos!')
            voltando_ao_menu()

        else:
            pass  

    except FileNotFoundError:
            
        print('\nNenhuma lista de desejos encontrada. ):')
        voltando_ao_menu()     