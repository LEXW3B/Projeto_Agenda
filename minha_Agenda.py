
lista = [] 
dicionario = {}
while True:
    print('adicionar novos contatos-------------------------[1]')#feito
    print('para ver todos os contatos-----------------------[2]')#feito
    print('Para alterar contatos tecle----------------------[3]')
    print('Para remover contato tecle-----------------------[4]')#
    print('Para buscar nomes existentes tecle---------------[5]')
    print('para sair----------------------------------------[9]')#feito
    print(' ')
    menu = int(input('Digite sua escolha: '))
    print(' ')

    if menu == 1:
        #bloco de adicionar contatos esta feito
        dicionario = {
            'email': input('Digite seu e-mail: '),
            'nome': input('Digite o nome do contato: '),
            'telefone': input('Digite o telefone do contato: ')
        }
        lista.append(dicionario)
        print('O contato {} foi cadastrado!\n'.format(dicionario['nome']))
        resp = str(input('deseja continuar S/N: ')).upper()
        if resp == 'S':
            lista = lista
        elif resp != 'S/N':
            print('Resposta invalida! Digite novamente.')
            menu = menu           
            
        else:
            print('Adicionar contato fim...')
            resp = resp
        #bloco de adicionar contatos esta feito

    elif menu == 2:
        #bloco de listar todos os contatos esta feito
        if len(lista)>0:
            for i, dicionario in enumerate(lista):
                print('Contato {}:'.format(i+1))
                print('-='*24)
                print('\tNome: {}'.format(dicionario['nome']))
                print('\tEmail: {}.'.format(dicionario['email']))
                print('\tTelefone: {}.'.format(dicionario['telefone']))
                print('-='*24)
        print('Quantidade de contatos: {}'.format(len(lista)))
        #bloco de listar todos os contatos esta feito

    elif menu == 4:
        #bloco para excluir contato nao funciona
        print('-=-=-=-=-=-=-=-= Excluir Contato =-=-=-=-=-=-=-=-')
        if len(lista)>0:

            email = input('Digite o e-mail do contato a ser excluído: ')
            print('-='*24)
            if dicionario(lista, email):
                for i, dicionario in enumerate(lista):
                    if dicionario['email'] == email:
                        print('Nome: {}'.format(dicionario['nome']))
                        print('Email: {}.'.format(dicionario['email']))
                        print('Telefone: {}.'.format(dicionario['telefone']))
                        print('-='*24) 

                        del lista[i]
                        print('O contato foi apagado com sucesso!')
                        break
            else:
                print('Não existe contato cadastrado com o email {}.\n'.format(email))     
        else:
            print('Não existem contatos cadastrados.\n')

    elif menu == 9:
        #bloco de fechar o programa esta feito
        break


        #bloco de buscar contato ainda nao funciona
    elif menu == 5:            
        if len(lista)>0:
            email = input('Digite o e-mail do contato a ser encontrado: ')
            print('-='*24)
            if dicionario(lista, email):
                for i, dicionario in enumerate(lista):
                    if dicionario['email'] == email:
                        print('Nome: {}'.format(dicionario['nome']))
                        print('Email: {}.'.format(dicionario['email']))
                        print('Telefone: {}.'.format(dicionario['telefone']))
                        print('-='*24)
                        break 
            else:
                print('Não existe contato cadastrado com o email {}.'.format(email))     
        else:
            print('Não existem contatos cadastrados.\n')    























