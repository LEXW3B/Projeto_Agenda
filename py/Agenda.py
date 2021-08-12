#Projeto Agenda para a faculdade 

     #INPUT === PRONTO
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
    escolha = ('lista')
elif escolha == 2:
    print('buscar contatos cadastrados') 
elif escolha == 3:
    print('alterando contato')
elif escolha == 4:
    print=('removendo contato')
else:
    print('Fim de programa')   
          
    #Bloco para adicionar contatos

lista = dict()

lista   ['Nome' ]   = str(input("Digite seu nome: "))
lista   ['Email']  = input("Digite seu e-mail: ")
lista   ['Insta']  = input("Digite seu usuário no Instagram: ")
lista   [ 'Twi' ]    = input("Digite seu usuário no Twitter: ")
lista   [ 'Tel' ]    = int(input("Digite seu telefone: "))
continuar = str(input('vai continuar[S/N]: ')).upper()

#bloco de repetição 
if continuar == 'S':       
    escolha = int(input('Digite o número da sua escolha: '))
    if escolha==1:
        escolha = ('lista')
    else:
        print('Fim de programa')
















#BIBLIOTECA

# contato1={'nome': 'Alexandre', 'telefone': '85-9898-0000', 'email': 'alexandre@serv.com', 'instagram': 'alex123', 'twitter': '@alex321'}

# contato2={'nome': 'Kelly', 'telefone': '85-9898-0001', 'email': 'kelly@serv.com', 'instagram': 'keka123', 'twitter': '@keka321'}

# contato3={'nome': 'Vanda', 'telefone': '85-9898-0002', 'email': 'vanda@serv.com', 'instagram': 'vanda123', 'twitter': '@vanda321'}

# contato4={'nome': 'Ricardo', 'telefone': '85-9898-0003', 'email': 'ricardo@serv.com', 'instagram': 'ricardo123', 'twitter': '@ricardo321'}
# print(contato1)