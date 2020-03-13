import requests, json, scripts
from time import sleep

flag_menu = True
lista_de_filmes = []

while flag_menu:

    scripts.menu()

    escolha = int(input('Digite o que deseja: '))

    if escolha == 1:

        try:
             
            title = input(str('\nDigite o nome do filme que deseja buscar: '))
        
            resposta = requests.get('http://www.omdbapi.com/?apikey=e85dca2c&t={}'.format(title)).json()# Fazendo a chamada da API com base no título do filme

            print(f'\nO título do filme é: {resposta["Title"]}')
            print(f'O ano do filme é: {resposta["Year"]}')
            print(f'O diretor do filme é: {resposta["Director"]}')
            print(f'Os atores principais são: {resposta["Actors"]}')
            print(f'O tempo de duração do filme é: {resposta["Runtime"]}')
            print(f'O(s) gênero(s) do filme é(são): {resposta["Genre"]}')
            print(f'O país de origem do filme é: {resposta["Country"]}')
            print(f'A lingua original do filme é: {resposta["Language"]}')

            esc1 = str(input('\nDeseja adicionar este filme a sua lista de desejos [S/N]: ')).upper().strip()# Retornando a str maiúscula sem espaços no começo e no final    

            if esc1 == 'S':

                filme = { # Salvando em um dicionário as informações que me interessam do filme, obtidas através da API 
                    "Titulo": resposta['Title'],
                    "Ano": resposta['Year'],
                    "Diretor": resposta['Director'],
                    "Atores principais": resposta['Actors'],
                    "Tempo de tela": resposta['Runtime'],
                    "Genero": resposta['Genre'],
                    "Pais": resposta['Country'],
                    "Lingua Original": resposta['Language'],
                    "Status de visualizacao": 'A definir'            
                     }
            
                try:
              
                    with open('lista_de_desejos.json') as arquivo: #Abrindo e carregando o arquivo de filmes para uma variável refêrencia
                        reference = []
                        reference = json.load(arquivo)

                    flag_dois = True

                    for movie in reference:
                    
                        if filme["Titulo"] == movie['Titulo']:
                        
                            print('\nEsse filme já existe na sua lista!')
                            scripts.voltando_ao_menu()
                            flag_dois = False
                
                        else:
                            pass
                        
                    if flag_dois == True:

                        reference.append(filme) #Apendando no meu arquivo de filmes o novo filme
                        
                        with open('lista_de_desejos.json', 'w') as arquivo: #Abrindo meu arquivo de filmes como escrita
                        
                            json.dump(reference, arquivo, indent=4) # Salvando as alterações feitas ao adicionar o novo filme

                            sleep(2) 

                            print('\nFilme adicionado com sucesso!')      
                            scripts.voltando_ao_menu()
                    else:
                        pass        

                except FileNotFoundError: #Caso não encontre o arquivo .json cria e adiciona o filme escolhido
                    
                    lista_de_filmes.append(filme)
                    
                    print('\nNenhuma lista de desejos encontrada.... Criando lista de desejos e adicionando filme....')
                    
                    with open('lista_de_desejos.json', 'w') as arquivo:
                        json.dump(lista_de_filmes, arquivo, indent=4)
                    
                    sleep(2)
                    
                    print('\nLista criada e filme adicionado!')
                    scripts.voltando_ao_menu()

            else:
                scripts.voltando_ao_menu()

        except KeyError:
            print('\nNome do filme inválido')
            scripts.voltando_ao_menu()
        
    if escolha == 2:
              
            try:
             
                title_dois = str(input('\nDigite o nome do filme que deseja deletar na sua lista de desejos: '))
        
                resposta = requests.get('http://www.omdbapi.com/?apikey=e85dca2c&t={}'.format(title_dois)).json()

                print(f'\nO título do filme é: {resposta["Title"]}')
                print(f'O ano do filme é: {resposta["Year"]}')
                print(f'O diretor do filme é: {resposta["Director"]}')
                print(f'Os atores principais são: {resposta["Actors"]}')
                print(f'O tempo de duração do filme é: {resposta["Runtime"]}')
                print(f'O(s) gênero(s) do filme é(são): {resposta["Genre"]}')
                print(f'O país de origem do filme é: {resposta["Country"]}')
                print(f'A lingua original do filme é: {resposta["Language"]}')

                esc_dois = str(input('\nEste é o filme que deseja apagar [S/N]: ')).upper().strip()
    
                if esc_dois == 'S':
            
                    with open('lista_de_desejos.json') as arquivo_dois: #Abrindo e carregando o arquivo de filmes para uma variável refêrencia
                        reference_dois = []
                        reference_dois = json.load(arquivo_dois) 

                    flag_tres = True
                
                    for movie2 in reference_dois:
                
                        if resposta['Title'] == movie2['Titulo']:# Fazendo a comparação entre o filme que foi digitado e os filmes já salvos na lista de desenjos
                            flag_tres = False

                        else:
                            pass       
                
                    if flag_tres == False:
                    
                        reference_dois.pop(title_dois == movie2['Titulo']) # Apagando o filme desejado da lista de filmes
                    
                        with open('lista_de_desejos.json', 'w') as arquivo_dois:
                            json.dump(reference_dois, arquivo_dois, indent=4)
                    

                        print('\nFilme apagado da lista de desejos com sucesso!')
                        scripts.voltando_ao_menu()
                
                    elif flag_tres:
                        print('\nEsse filme não existe na sua lista de desejos!')
                        scripts.voltando_ao_menu()

                else:
                    scripts.voltando_ao_menu()
        
            except FileNotFoundError:
                print('\nLista de desejos não existe.')  
                scripts.voltando_ao_menu()
    
    if escolha == 3:

       scripts.visualizar_lista_de_desejos()

    if escolha == 4:
        
        scripts.buscar_filme()          

    if escolha == 5:
        
        scripts.status()

    if escolha == 6:
        
        print('\nAté um outro dia...... Um triste amanhã...... :)\n')
        flag_menu = False    