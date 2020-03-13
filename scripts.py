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

def saindo_do_programa(flag):
    
    print('\nAté um outro dia...... Um triste amanhã...... :)\n')
    sleep(2)
    flag = False