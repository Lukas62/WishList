import requests, json, time, os
from time import sleep

def menu():

    print('\n****** Bem vindo(a) a sua lista de desejos! ******')
    print('*** Adicionar filme a lista de desejos: [1] ***')
    print('*** Deletar filme da lista de desejos: [2] ***')
    print('*** Visualizar a lista de desejos: [3] ***')
    print('*** Buscar filme na lista de desejos: [4] ***')
    print('*** Atualizar status de filme da lista de desejos: [5] ***')
    print('*** Sugestões com base no último filme adicionado: [6] ***')
    print('*** Sugestões com base no último filme adicionado: [7] ***')
    print('*** Sair da lista de desejos: [8] ***')
    print('***********************************************\n')

def status():

    flag_status = False
        
    try:    
        
        with open('lista_de_desejos.json') as arquivo:
            reference = json.load(arquivo)
            
            if len(reference) != 0:
                
                print('\nEsses são os filmes que você possui na sua lista de desejos.\n')

                for filme_na_lista in reference:
            
                    print(f'\nO título do filme é: {filme_na_lista["Titulo"]}')
                    print(f'O ano do filme é: {filme_na_lista["Ano"]}')
                    print(f'O diretor do filme é: {filme_na_lista["Diretor"]}')
                    print(f'Os atores principais são: {filme_na_lista["Atores Principais"]}')
                    print(f'O tempo de duração do filme é: {filme_na_lista["Tempo De Tela"]}')
                    print(f'O(s) gênero(s) do filme é(são): {filme_na_lista["Genero"]}')
                    print(f'O país de origem do filme é: {filme_na_lista["Nacionalidade"]}')
                    print(f'A lingua original do filme é: {filme_na_lista["Lingua Original"]}')
                    print(f'Status De Visualização: {filme_na_lista["Status De Visualizacao"]}')
            
        title_status = str(input('\nDigite o nome do filme que deseja alterar o status de visualização: ')).lower().strip()
        
        with open('lista_de_desejos.json') as arquivo:
            
            reference = json.load(arquivo)

            for filme_na_lista in reference:
                
                if title_status == filme_na_lista['Titulo']:
                    
                    flag_status = True  
            
            if flag_status:     
                print('\nOpções De Status De Visualização: ')
                print('\nAssistido [1]')
                print('Não assistido [2]')
                print('Assistir mais tarde [3]\n')
                    
                escolha_de_status = input('Digite o número da escolha de status desejada: ')

                if escolha_de_status == '1':

                    filme_na_lista['Status De Visualizacao'] = 'Assistido'

                    with open('lista_de_desejos.json', 'w') as arquivo:    
                        json.dump(reference, arquivo, indent=4)
                        print('\nStatus atualizado!')
                        voltando_ao_menu()

                elif escolha_de_status == '2':

                    filme_na_lista['Status De Visualizacao'] = 'Nao assistido'
                        
                    with open('lista_de_desejos.json', 'w') as arquivo:    
                        json.dump(reference, arquivo, indent=4)
                        print('\nStatus atualizado!')
                        voltando_ao_menu()

                elif escolha_de_status == '3':

                    filme_na_lista['Status De Visualizacao'] = 'Assistir mais tarde' 
                        
                    with open('lista_de_desejos.json', 'w') as arquivo:    
                        json.dump(reference, arquivo, indent=4)
                        print('\nStatus atualizado!')
                        voltando_ao_menu()

                        
                else:
                        
                        print('\nOpção inválida.')
                        voltando_ao_menu()
                
            else:
                pass               
            
            if flag_status == False:
                    
                print('\nVocê não possui esse filme na sua lista')
                voltando_ao_menu()

            else:
                pass    

    except FileNotFoundError:
        
        print('\nVocê ainda não possui uma lista de desejos. ):')  
        voltando_ao_menu()    

    except KeyError:

        print('Esse não é um filme válido.')

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
                    
                    for filme_na_lista in reference_tres:

                        print(f'\nO título do filme é: {filme_na_lista["Titulo"]}')
                        print(f'O ano do filme é: {filme_na_lista["Ano"]}')
                        print(f'O diretor do filme é: {filme_na_lista["Diretor"]}')
                        print(f'Os atores principais são: {filme_na_lista["Atores Principais"]}')
                        print(f'O tempo de duração do filme é: {filme_na_lista["Tempo De Tela"]}')
                        print(f'O(s) gênero(s) do filme é(são): {filme_na_lista["Genero"]}')
                        print(f'O país de origem do filme é: {filme_na_lista["Nacionalidade"]}')
                        print(f'A lingua original do filme é: {filme_na_lista["Lingua Original"]}')
                        print(f'Status De Visualização: {filme_na_lista["Status De Visualizacao"]}')
                            
            else:
                pass

            voltando_ao_menu()

    except FileNotFoundError:
        
        print('\nNenhuma lista de desejos encontrada. ):')
        voltando_ao_menu()
        
def buscar_filme():

    filme_desejado = str(input('\nDigite o nome do filme que deseja buscar na sua lista de desejos: ')).strip()
        
    flag_quatro = True
        
    try:
        with open('lista_de_desejos.json') as arquivo_tres:
            reference_quatro = json.load(arquivo_tres)

        for filme_na_lista in reference_quatro:
               
            if filme_desejado == filme_na_lista['Titulo']:
                
                flag_quatro = False

                print(f'\nO título do filme é: {filme_na_lista["Titulo"]}')
                print(f'O ano do filme é: {filme_na_lista["Ano"]}')
                print(f'O diretor do filme é: {filme_na_lista["Diretor"]}')
                print(f'Os atores principais são: {filme_na_lista["Atores Principais"]}')
                print(f'O tempo de duração do filme é: {filme_na_lista["Tempo De Tela"]}')
                print(f'O(s) gênero(s) do filme é(são): {filme_na_lista["Genero"]}')
                print(f'O país de origem do filme é: {filme_na_lista["Nacionalidade"]}')
                print(f'A lingua original do filme é: {filme_na_lista["Lingua Original"]}')
                print(f'Status De Visualização: {filme_na_lista["Status De Visualizacao"]}')

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

def adicionar_filme():

    lista_de_filmes = []
   
    try:
             
        print('\nAdicionar filme fornecendo apenas um título: [1] ')
        print ('Adicionar um filme fornecendo um título e um ano: [2]')
        escolha_para_adicionar = str(input('\nDigite o número da escolha que deseja: '))
        

        if escolha_para_adicionar == '1':

            title = str(input('\nDigite o nome do filme que deseja buscar: '))
        
            try:
        
                filme_na_lista = requests.get('http://www.omdbapi.com/?apikey=e85dca2c&t={}'.format(title)).json()# Fazendo a chamada da API com base no título do filme
            
            except ConnectionError:
                print('Erro de conexão!')
                voltando_ao_menu()
            
        elif escolha_para_adicionar == '2':

            title = str(input('\nDigite o nome do filme que deseja buscar: '))
            ano = int(input('Digite o ano do filme: '))
            
            try:
            
                filme_na_lista = requests.get('http://www.omdbapi.com/?apikey=e85dca2c&t={}&y={}'.format(title, ano)).json()

            except ConnectionError:
                print('Erro de conexão!')
                voltando_ao_menu()

        print(f'\nO título do filme é: {filme_na_lista["Title"]}')
        print(f'O ano do filme é: {filme_na_lista["Year"]}')
        print(f'O diretor do filme é: {filme_na_lista["Director"]}')
        print(f'Os atores principais são: {filme_na_lista["Actors"]}')
        print(f'O tempo de duração do filme é: {filme_na_lista["Runtime"]}')
        print(f'O(s) gênero(s) do filme é(são): {filme_na_lista["Genre"]}')
        print(f'O país de origem do filme é: {filme_na_lista["Country"]}')
        print(f'A lingua original do filme é: {filme_na_lista["Language"]}')

        esc1 = str(input('\nDeseja adicionar este filme a sua lista de desejos [S/N]: ')).upper().strip()# Retornando a str maiúscula sem espaços no começo e no final    

        if esc1 == 'S':

            filme = { # Salvando em um dicionário as informações que me interessam do filme, obtidas através da API 
                "Titulo": filme_na_lista['Title'].lower(),
                "Ano": filme_na_lista['Year'],
                "Diretor": filme_na_lista['Director'],
                "Atores Principais": filme_na_lista['Actors'],
                "Tempo De Tela": filme_na_lista['Runtime'],
                "Genero": filme_na_lista['Genre'],
                "Nacionalidade": filme_na_lista['Country'],
                "Lingua Original": filme_na_lista['Language'],
                "Status De Visualizacao": 'A definir'            
                    }
            
            try:
              
                with open('lista_de_desejos.json') as arquivo: #Abrindo e carregando o arquivo de filmes para uma variável refêrencia
                    reference = []
                    reference = json.load(arquivo)

                flag_dois = True

                for movie in reference:
                    
                    if filme["Titulo"] == movie['Titulo']:
                        
                        print('\nEsse filme já existe na sua lista!')
                        voltando_ao_menu()
                        flag_dois = False
                
                    else:
                        pass
                        
                if flag_dois == True:

                    reference.append(filme) #Apendando no meu arquivo de filmes o novo filme
                        
                    with open('lista_de_desejos.json', 'w') as arquivo: #Abrindo meu arquivo de filmes como escrita
                        
                        json.dump(reference, arquivo, indent=4) # Salvando as alterações feitas ao adicionar o novo filme
                        print('\nFilme adicionado com sucesso!') 

                    voltando_ao_menu()
                
                else:
                    pass        

            except FileNotFoundError: #Caso não encontre o arquivo .json cria e adiciona o filme escolhido
                    
                lista_de_filmes.append(filme)
                    
                print('\nNenhuma lista de desejos encontrada.... Criando lista de desejos e adicionando filme....')
                    
                with open('lista_de_desejos.json', 'w') as arquivo:
                    json.dump(lista_de_filmes, arquivo, indent=4)
                    
                sleep(2)
                    
                print('\nLista criada e filme adicionado!')
                voltando_ao_menu()

        elif esc1 == 'N':

            voltando_ao_menu()
        
        else:
            print('\nOpção inválida.')
            voltando_ao_menu()

    except KeyError:

        print('\nNome do filme ou ano(Caso opção de de fornecer ano também tenha sido selecionada) inválido.')
        voltando_ao_menu()        

def deletar_filme():

    try:
        
        with open('lista_de_desejos.json') as arquivo:
            reference = json.load(arquivo)
            
            if len(reference) != 0:
                
                print('\nEsses são os filmes que você possui na sua lista de desejos.')
                
                for filme_na_lista in reference:
                    
                    print(f'\nO título do filme é: {filme_na_lista["Titulo"]}')
                    print(f'O ano do filme é: {filme_na_lista["Ano"]}')
                    print(f'O diretor do filme é: {filme_na_lista["Diretor"]}')
                    print(f'Os atores principais são: {filme_na_lista["Atores Principais"]}')
                    print(f'O tempo de duração do filme é: {filme_na_lista["Tempo De Tela"]}')
                    print(f'O(s) gênero(s) do filme é(são): {filme_na_lista["Genero"]}')
                    print(f'O país de origem do filme é: {filme_na_lista["Nacionalidade"]}')
                    print(f'A lingua original do filme é: {filme_na_lista["Lingua Original"]}')
                    print(f'Status De Visualização: {filme_na_lista["Status De Visualizacao"]}')

        title_dois = str(input('\nDigite o nome do filme que deseja deletar na sua lista de desejos: ')).lower().strip()
            
        with open('lista_de_desejos.json') as arquivo_dois: #Abrindo e carregando o arquivo de filmes para uma variável refêrencia
            reference_dois = json.load(arquivo_dois) 

        flag_tres = True
                
        for movie2 in reference_dois:
                
            if title_dois == movie2["Titulo"]:# Fazendo a comparação entre o filme que foi digitado e os filmes já salvos na lista de desenjos
                            
                flag_tres = False

            else:
                pass       
                
        if flag_tres == False:
                    
            lista = []

            for filme_delete in reference_dois:

                if title_dois != filme_delete["Titulo"]:
                            
                    lista.append(filme_delete)


            with open('lista_de_desejos.json', 'w') as arquivo_dois:
                json.dump(lista, arquivo_dois, indent=4)
                    

            print('\nFilme apagado da lista de desejos com sucesso!')
            voltando_ao_menu()
                
        elif flag_tres:
            print('\nEsse filme não existe na sua lista de desejos!')
            voltando_ao_menu()
        
    except FileNotFoundError:
        print('\nLista de desejos não existe.')  
        voltando_ao_menu()
    
    except KeyError:
        print('\nNão é um filme válido.')
        voltando_ao_menu()  

def sugestoes_com_base_no_ultimo_filme_adicionado():

    try:
        
        with open ('lista_de_desejos.json') as arquivo:

            reference = json.load(arquivo)

            if len(reference) != 0:

                for filme in reference:

                    if filme == reference[len(reference) - 1]:

                        nome = filme["Titulo"]

                        consulta = requests.get('http://www.omdbapi.com/?apikey=e85dca2c&s={}'.format(nome)).json()
                        
                        if 'Error' not in consulta and 'False' not in consulta:    
                            
                            print('\nTemos algumas sugestões com base no seu último filme adicionado!\n ')
                            print(json.dumps(consulta["Search"], indent=4))
                            voltando_ao_menu()

                        else:
                            print('\n"Desculpe, não foi possível sugerir mídias com base no seu último filme adicionado a lista de desejos,'
                             ' adicione um novo filme e tente novamente!')
                            voltando_ao_menu()
                    else:
                        pass
            
            else:
                print('Você não possui nenhum filme na sua lista!')
                voltando_ao_menu()


    except FileNotFoundError:
        print('Você ainda não possui uma lista de desejos!')
        voltando_ao_menu()

def sugestoes_com_base_em_todos_os_filmes_adicionados():

    try: 

        with open ('lista_de_desejos.json') as arquivo:
            
            reference = arquivo

            if len(reference) != 0:

                for filme in reference:

                    nome = filme["Titulo"]

                    consulta = requests.get('http://www.omdbapi.com/?apikey=e85dca2c&s={}'.format(nome)).json()

                     if 'Error' not in consulta and 'False' not in consulta:    
                            
                            print('\nTemos algumas sugestões com base nos filmes adicionados a lista de desejos !\n ')
                            print(json.dumps(consulta["Search"], indent=4))
                            voltando_ao_menu()