import requests, json, scripts
from time import sleep

flag = True
lista_de_filmes = []

while flag:

    scripts.menu()

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
                        print('\nVoltando ao menu...')
                        sleep(2)
                        flag_dois = False
                
                    else:
                        pass
                        
                if flag_dois == True:

                    reference.append(filme) #Apendando no meu arquivo de filmes o novo filme
                        
                    with open('lista_de_desejos.json', 'w') as arquivo: #Abrindo meu arquivo de filmes como escrita
                        
                        json.dump(reference, arquivo, indent=4) # Salvando as alterações feitas ao adicionar o novo filme

                        sleep(2) 

                        print('\nFilme adicionado com sucesso!')      
                        print('\nRetornando ao menu...')
                        
                        sleep(2)

            except FileNotFoundError: #Caso não encontre o arquivo .json cria e adiciona o filme escolhido
                
                lista_de_filmes.append(filme)
                
                print('\nNenhuma lista de desejos encontrada.... Criando lista de desejos e adicionando filme....')
                
                with open('lista_de_desejos.json', 'w') as arquivo:
                    json.dump(lista_de_filmes, arquivo, indent=4)
                
                sleep(2)
                
                print('Lista criada e filme adicionado!')

        else:
            print('\nRetornar ao menu [1]')
            print('\nSair [2]\n')
            opcao = int(input('Digite o que deseja: '))

            if opcao == 1:
                pass
            else:
                print('\nAté um outro dia...... Um triste amanhã...... :)\n')
                flag = False
            sleep(1)
        
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

                sleep(1)

                esc_dois = str(input('\nEste é o filme que deseja apagar [S/N]: ')).upper().strip()
    
                #if esc_dois == 'S':
            
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
                    print('Retornando ao menu...')

                    sleep(2)
                
                elif flag_tres:
                    print('\nEsse filme não existe na sua lista de desejos!')
                    print('Retornando ao menu...')
        
                sleep(2)
        
            except FileNotFoundError:
                print('Lista de desejos não existe.')  
    
    if escolha == 3:
        cont = 0

        try:
            
            flag = True

            with open('lista_de_desejos.json') as arquivo_tres:
                reference_tres = json.load(arquivo_tres)
                      
                if len(reference_tres) == 0:
                    print('Você não tem nenhum filme na sua lista de desejos!')
                    flag = False
                           
                if flag:
                    
                    for intem in reference_tres:
                        
                        cont += 1

                    print(f'\nVocê possui {cont} filme(s) na sua lista de desejos.')
                    print('\nOs filmes na sua lista são:')
                    print(json.dumps(reference_tres, indent=4, separators = (". ", " = ")))
            
                else:
                    pass

            print('\nRetornar ao menu [1]')
            print('\nSair [2]\n')
            opcao = int(input('Digite o que deseja: '))

            if opcao == 1:
                pass
            else:
                print('\nAté um outro dia...... Um triste amanhã...... :)\n')
                flag = False 

        except FileNotFoundError:
            print('Nenhuma lista de desejos encontrada. ):')
            print('\nRetornar ao menu [1]')
            print('\nSair [2]\n')
            opcao = int(input('Digite o que deseja: '))

            if opcao == 1:
                sleep(2)
            else:
                print('\nAté um outro dia...... Um triste amanhã...... :)\n')
                sleep(2)
                flag = False 
            

    if escolha == 4:
        
        filme_desejado = str(input('\nDigite o nome do filme que deseja buscar na sua lista de desejos: ')).title().strip()
        
        flag_quatro = True
        
        try:
            with open('lista_de_desejos.json') as arquivo_tres:
                reference_quatro = json.load(arquivo_tres)

            for filme_na_lista in reference_quatro:
               
                if filme_desejado == filme_na_lista['Titulo']:
                    flag_quatro = False
                    print(json.dumps(filme_na_lista, indent=4, separators = (". ", " = ")))
                
                else:
                    pass    
            
            if flag_quatro == True:
                print('Você não possui este filme na sua lista de desejos!')

            else:
                pass  

        except FileNotFoundError:
            
            print('Nenhuma lista de desejos encontrada. ):')
            print('\nRetornar ao menu [1]')
            print('\nSair [2]\n')
            opcao = int(input('Digite o que deseja: '))

            if opcao == 1:
                sleep(2)
            else:
                print('\nAté um outro dia...... Um triste amanhã...... :)\n')
                sleep(2)
                flag = False 
        
        print('\nRetornar ao menu [1]')
        print('\nSair [2]\n')
        
        opcao = int(input('Digite o que deseja: '))

        if opcao == 1:
            sleep(2)
        else:
            print('\nAté um outro dia...... Um triste amanhã...... :)\n')
            sleep(2)
            flag = False            

    if escolha == 5:
        
        flag = True

        title = str(input('\nDigite o nome do filme que deseja alterar o status de visualização: ')).title().strip()
        
        try:    
        
            with open('lista_de_desejos.json') as arquivo:
            
                reference = json.load(arquivo)

                for item in reference:
                
                    if title == item['Titulo']:
                    
                        print('\nAssistido [1]')
                        print('Não assistido [2]')
                        print('Assistir mais tarde [3]')
                        escolha_de_status = input('Escolha a opção de status de visualização que deseja: ')

                        if escolha_de_status == '1':

                            item['Status de visualizacao'] = 'Assistido'
                            
                            print(item['Status de visualizacao'])

                            with open('lista_de_desejos.json', 'w') as arquivo:    
                                json.dump(reference, arquivo, indent=4)

                            print('Status atualizado!')

                        elif escolha_de_status == '2':

                            item['Status de visualizacao'] = 'Não assistido'
                            
                            with open('lista_de_desejos.json', 'w') as arquivo:    
                                json.dump(reference, arquivo, indent=4)

                        if escolha_de_status == '3':

                            item['Status de visualizacao'] = 'Assistir mais tarde' 
                            
                            with open('lista_de_desejos.json', 'w') as arquivo:    
                                json.dump(reference, arquivo, indent=4)

                    else:
                        
                        flag = False               
            
                if flag == False:
                    
                    print('Você não possui esse filme na sua lista')

        except FileNotFoundError:
            print('\nVocê ainda não possui uma lista de desejos')           

    if escolha == 6:
        
        print('\nAté um outro dia...... Um triste amanhã...... :)\n')
        flag = False 

    
    
    
        

    
        

#print(json.dumps(lista, indent=4, separators = (". ", " = ")))      

...

'''if escolha == 2:
              
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

                sleep(1)

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
                    print('Retornando ao menu...')

                    sleep(2)
                
                elif flag_tres:
                    print('\nEsse filme não existe na sua lista de desejos!')
                    print('Retornando ao menu...')
        
                sleep(2)
        
            except FileNotFoundError:
                print('Lista de desejos não existe.')'''