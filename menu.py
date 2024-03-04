# -*- coding: utf-8 -*-
import os
from datetime import datetime

data = datetime.now()

def banner():
    print('************************************')
    print(f'\tPYTHON MENU {data.day}/{data.month}/{data.year}')
    print('************************************')

menu_options = {
    1: 'Opção 1',
    2: 'Opção 2',
    3: 'Opção 3',
    0: 'Sair',
}

def print_menu():
    os.system('clear')
    banner()
    for key in menu_options.keys():
        print ('\t',key, '-', menu_options[key] )
    print('************************************')

def opcao1():
     os.system('clear')
     print('Selecionado a opção 1')
     input('\n\t[ Pressione Enter para continuar ] ')

def opcao2():
     os.system('clear')
     print('Selecionado a opção 2')
     input('\n\t[ Pressione Enter para continuar ] ')

def opcao3():
     os.system('clear')
     print('Selecionado a opção 3')
     input('\n\t[ Pressione Enter para continuar ] ')

if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Escolha uma opção: '))
        except:
            print_menu()

        if option == 1:
           opcao1()
        elif option == 2:
            opcao2()
        elif option == 3:
            opcao3()
        elif option == 0:
            os.system('clear')
            print('Até breve!')
            input('\n\t[ Pressione Enter para sair ]')
            os.system('clear')
            exit()
        else:
            os.system('clear')
            print('Opção inválida!')
            input('\n\t[ Pressione Enter para continuar ]')
