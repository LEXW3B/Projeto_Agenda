#Projeto Agenda para a faculdade 

     #INPUT === PRONTO
import os
lista=[]
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
        lista = (controle.inserir(nome, email, insta, twitt, telef))#aqui problema
        continuar = str(input('vai continuar[S/N]: ')).upper()
        # os.system('cls')
    #===========agora e esse bloco==============================================
    elif escolha == 2:
        nome = input('Digite o nome para ser pesquisado: ')
        controle.listarNome(nome, email, insta, twitt, telef)#problema aqui
    #============================================================================
    elif escolha == 3:
        print('alterando contato')
    elif escolha == 4:
        print=('removendo contato')
    else:
        print('Fim de programa')  

    #bloco de repetição 
    if continuar == 'S':       
        def continuar(escolha):
            return 'none'
    else:
        break 
    class controle():
        def inserir(nome, email, insta, twitt, telef):
            return telefone(nome, email, insta, twitt, telef)
        def listarAll(lista):
            for tel in lista:
                print('{} | {}'.format(tel.getNome(), tel.getTelefone()))       
#===========agora e esse bloco==============================================
        def listarNome(nome, email, insta, twitt, telef):
            cont = 0
            for tel in lista:#problema aqui
                if tel.getNome() == lista:#aqui lista
                    print('{} | {}'.format(tel.getNome(), tel.getTelefone()))
                    break
                cont += 1
# ==========================================================================
   
#BIBLIOTECA

# contato1={'nome': 'Alexandre', 'telefone': '85-9898-0000', 'email': 'alexandre@serv.com', 'instagram': 'alex123', 'twitter': '@alex321'}

# contato2={'nome': 'Kelly', 'telefone': '85-9898-0001', 'email': 'kelly@serv.com', 'instagram': 'keka123', 'twitter': '@keka321'}

# contato3={'nome': 'Vanda', 'telefone': '85-9898-0002', 'email': 'vanda@serv.com', 'instagram': 'vanda123', 'twitter': '@vanda321'}

# contato4={'nome': 'Ricardo', 'telefone': '85-9898-0003', 'email': 'ricardo@serv.com', 'instagram': 'ricardo123', 'twitter': '@ricardo321'}
# print(contato1)