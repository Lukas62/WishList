import requests, json
from time import sleep

flag = True
lista_de_filmes = []

while flag:

    print('\n****** Bem vindo(a) a sua lista de desejos! ******')
    print('*** Adicionar filme a lista de desejos: [1] ***')
    print('*** Deletar filme da lista de desejos: [2] ***')
    print('*** Buscar filme na lista de desejos: [3] ***')
    print('*** Atualizar status de filme da lista de desejos: [4] ***')
    print('*** Sair da lista de desejos: [5] ***')
    print('***********************************************\n')

    escolha = int(input('Digite o que deseja: '))

    if escolha == 1:

        try:
             title = input(str('\nDigite o nome do filme que deseja buscar: '))
        
        except KeyError:
            print('Nome inválido!')
        
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
                "Status": 'Pendente'            
                }
            
            try:
              
                with open('lista_de_desejos.json') as arquivo: #Abrindo e carregando o arquivo de filmes para uma variável refêrencia
                    reference = []
                    reference = json.load(arquivo)

                flag_dois = True

                for movie in reference:
                
                    if filme["Titulo"] == movie['Titulo']:
                        
                        print('\nEsse filme já existe na sua lista!')
                        print('\nVoltando ao menu...')
                        sleep(2)
                        flag_dois = False
                
                    else:
                        pass
                        
                if flag_dois == True:

                    reference.append(filme) #Apendando no meu arquivo de filmes o novo filme
                        
                    with open('lista_de_desejos.json', 'w') as arquivo: #Abrindo meu arquivo de filmes como escrita e salvando as alterações feitas ao adicionar o novo filme
                        
                        json.dump(reference, arquivo, indent=4)

                        sleep(2) 

                        print('\nFilme adicionado com sucesso!')      
                        print('Retornando ao menu...')
                        
                        sleep(2)

            except FileNotFoundError: #Caso não encontre o arquivo .json cria e adiciona o filme escolhido
                
                lista_de_filmes.append(filme)
                
                print('\nNenhuma lista de desejos encontrada.... Criando lista de desejos e adicionando filme....')
                
                with open('lista_de_desejos.json', 'w') as arquivo:
                    json.dump(lista_de_filmes, arquivo, indent=4)
                
                sleep(2)
                
                print('Lista criada e filme adicionado!')

        else:
            print('\nRetornando ao menu...')
            sleep(1)
        
    if escolha == 2:
              
            try:
             
                title2 = str(input('\nDigite o nome do filme que deseja deletar na sua lista de desejos: '))
        
                resposta = requests.get('http://www.omdbapi.com/?apikey=e85dca2c&t={}'.format(title2)).json()

                print(f'\nO título do filme é: {resposta["Title"]}')
                print(f'O ano do filme é: {resposta["Year"]}')
                print(f'O diretor do filme é: {resposta["Director"]}')
                print(f'Os atores principais são: {resposta["Actors"]}')
                print(f'O tempo de duração do filme é: {resposta["Runtime"]}')
                print(f'O(s) gênero(s) do filme é(são): {resposta["Genre"]}')
                print(f'O país de origem do filme é: {resposta["Country"]}')
                print(f'A lingua original do filme é: {resposta["Language"]}')

                sleep(1)

                esc2 = str(input('\nEste é o filme que deseja apagar [S/N]: ')).upper().strip()
    
                if esc2 == 'S':
            
                    with open('lista_de_desejos.json') as arquivo2: #Abrindo e carregando o arquivo de filmes para uma variável refêrencia
                        reference2 = []
                        reference2 = json.load(arquivo2) 

                flag_tres = True
                
                for movie2 in reference2:
                
                    if resposta['Title'] == movie2['Titulo']:# Fazendo a comparação entre o filme que foi digitado e os filmes já salvos na lista de desenjos
                        flag_tres = False

                    else:
                        pass       
                
                if flag_tres == False:
                    
                    reference2.pop(title2 == movie2['Titulo']) # Apagando o filme desejado da lista de filmes
                    
                    with open('lista_de_desejos.json', 'w') as arquivo2:
                        json.dump(reference2, arquivo2, indent=4)
                    

                    print('\nFilme apagado da lista de desejos com sucesso!')
                    print('Retornando ao menu...')

                    sleep(2)
                
                elif flag_tres:
                    print('\nEsse filme não existe na sua lista de desejos!')
                    print('Retornando ao menu...')
        
                sleep(2)
        
            except FileNotFoundError:
                print('Lista de desejos não existe.')  
    
    if escolha == 5:
        
        print('\nAté um outro dia...... Um triste amanhã...... :)\n')
        flag = False 

    
    
    
        

    
        

#print(json.dumps(lista, indent=4, separators = (". ", " = ")))      