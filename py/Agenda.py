#Projeto Agenda para a faculdade 

     #INPUT === PRONTO
import os
lista={}


while True:
    print('------------------------------------------------')
    print('=====================AGENDA=====================')
    print('------------------------------------------------')
    print('')
    print('Para adicionar contato tecle-----------------[1]')
    print('Para buscar nomes existentes tecle-----------[2]')
    print('Para alterar contatos tecle------------------[3]')
    print('Para remover contato tecle-------------------[4]')
    print('Para sair tecle------------------------------[9]')
    print('')
    print('------------------------------------------------')
    print('')
    escolha = int(input('Digite o número da sua escolha: '))
    
    if escolha == 1:
        nome  = str(input("Digite seu nome: "))
        email = input("Digite seu e-mail: ")
        insta = input("Digite seu usuário no Instagram: ")
        twitt = input("Digite seu usuário no Twitter: ")
        telef = int(input("Digite seu telefone: "))
        lista = nome, email, insta, twitt, telef #aqui problema
        continuar = str(input('vai continuar[S/N]: ')).upper()
        # os.system('cls')
    #===========agora e esse bloco==============================================
    elif escolha == 2:
        nome = input('Digite o nome para ser pesquisado: ')
        controle.listarNome(lista, nome)#problema aqui
    #============================================================================
    elif escolha == 3:
        controle.listarAll(lista)#problema 3
    elif escolha == 4:
        print=('removendo contato')
    else:
        print('Fim de programa')  

    #bloco de repetição 
    # if continuar == 'S':       
    #     def continuar(escolha):
    #         return 'none'
    # else:
    #     break 
    # from controle import telefone
    class controle():
        def inserir(nome, email, insta, twitt, telef):
            return telefone(nome, email, insta, twitt, telef)
#===========agora e esse bloco==============================================
        def listarNome(lista, nome):
            cont = 0
            for tel in lista:#problema aqui
                if tel.getNome() == lista:#aqui lista
                    print('{} | {}'.format(tel.getNome(), tel.getTelefone()))
                    break
                cont += 1
# ==========================================================================
        def listarAll(lista):
            for tel in lista:
                print('{} | {}'.format(tel.getNome(), tel.getTelefone()))# problema 3      


        def deletarAll(lista):
            if len(lista) != 0:
                lista.clear()
                return 'Todos os contatos foram removidos!'
            else:
                return 'A lista telefonica está vazia!'
        def deletarNome(lista, nome):
            if len(lista) != 0:
                cont = 0
                for tel in lista:
                    if tel.getNome() == nome:
                        lista.pop(cont)
                        return 'Contado {} removido com sucesso!'.format(nome)
                    else:
                        return 'Nome não encontrado!'
            else:
                return 'Lista está vazia!' 
    class telefone():
        def __init__(self, nome, email, insta, twitt, telef):
            self.__nome  = nome
            self.__email = email
            self.__insta = insta
            self.__twitt = twitt
            self.__telef = telef

        def getNome(self):
            return self.__nome

        def getNome(self):
            return self.__email

        def getNome(self):
            return self.__insta

        def getNome(self):
            return self.__twitt

        def getTelefone(self):
            return self.__telef
    
   
#BIBLIOTECA

# contato1={'nome': 'Alexandre', 'telefone': '85-9898-0000', 'email': 'alexandre@serv.com', 'instagram': 'alex123', 'twitter': '@alex321'}

# contato2={'nome': 'Kelly', 'telefone': '85-9898-0001', 'email': 'kelly@serv.com', 'instagram': 'keka123', 'twitter': '@keka321'}

# contato3={'nome': 'Vanda', 'telefone': '85-9898-0002', 'email': 'vanda@serv.com', 'instagram': 'vanda123', 'twitter': '@vanda321'}

# contato4={'nome': 'Ricardo', 'telefone': '85-9898-0003', 'email': 'ricardo@serv.com', 'instagram': 'ricardo123', 'twitter': '@ricardo321'}
# print(contato1)