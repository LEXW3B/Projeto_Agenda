def salvar_contatos(lista):
    arquivo = open('contatos.txt', 'write')#salva os contatos em um arquivo txt

    for contato in lista:
        arquivo.write('{}#{}#{}\n'.format(contato['nome'], contato['email'], contato['telefone']))

    arquivo.close()#so salva realmente quando fecha o arquivo aqui.

def carregar_contatos():
    lista = []

    try:
        arquivo = open('contatos.txt', 'r')#abrir o arquivo txt e ler.

        for linha in arquivo.readlines():
            coluna = linha.strip().split('#')

            contato = {#dicionario
                'email': coluna[1],
                'nome': coluna[0],
                'telefone': coluna[2]
            }
            lista.append(contato)    
        arquivo.close()

    except FileNotFoundError:
       pass 
    return lista

def existe_contato(lista, email):
    if len(lista)>0:
        for contato in lista:
            if contato['email'] == email:
                return True
    return False          

def adicionar(lista):
    
    while True:
        email = input('Digite o e-mail do contato: ')
        if not existe_contato(lista, email):
            break
        else:
            print('Esse e-mail já está cadastrado.')
            print('Por favor, tente com outro e-mail.')
    #nesse passo, o email recebido será único

    contato = {#dicionario
        'email': email,
        'nome': input('Digite o nome do contato: '),
        'telefone': input('Digite o telefone do contato: ')
    }
    lista.append(contato)
    print('O contato {} foi cadastrado!\n'.format(contato['nome']))


def alterar(lista):
    print('-=-=-=-=-=-=-=-= Alterar Contato =-=-=-=-=-=-=-=-')
    if len(lista)>0:

        email = input('Digite o e-mail do contato a ser alterado: ')
        print('-='*24)
        if existe_contato(lista, email):
            for i, contato in enumerate(lista):
                if contato['email'] == email:
                    print('Nome: {}'.format(contato['nome']))
                    print('Email: {}.'.format(contato['email']))
                    print('Telefone: {}.'.format(contato['telefone']))
                    print('-='*24) 

                    contato['nome'] = input('Digite o novo nóme do contato: ')
                    contato['telefone'] = input('Digite o novo telefone  do contato: ')
                    print('Os dados do contato com o e-mail {}, foram alterados com sucesso!'.format(contato['email']))
                    break
        else:
            print('Não existe contato cadastrado com o email {}.'.format(email))     
    else:
        print('Não existem contatos cadastrados.\n')

def excluir(lista):
    print('-=-=-=-=-=-=-=-= Excluir Contato =-=-=-=-=-=-=-=-')
    if len(lista)>0:

        email = input('Digite o e-mail do contato a ser excluído: ')
        print('-='*24)
        if existe_contato(lista, email):
            for i, contato in enumerate(lista):
                if contato['email'] == email:
                    print('Nome: {}'.format(contato['nome']))
                    print('Email: {}.'.format(contato['email']))
                    print('Telefone: {}.'.format(contato['telefone']))
                    print('-='*24) 

                    del lista[i]
                    print('O contato foi apagado com sucesso!')
                    break
        else:
            print('Não existe contato cadastrado com o email {}.\n'.format(email))     
    else:
        print('Não existem contatos cadastrados.\n')

def buscar(lista):
    print('-=-=-=-=-=-=-=-= Buscar Contato =-=-=-=-=-=-=-=-')
    if len(lista)>0:

        email = input('Digite o e-mail do contato a ser encontrado: ')
        print('-='*24)
        if existe_contato(lista, email):
            for i, contato in enumerate(lista):
                if contato['email'] == email:
                    print('Nome: {}'.format(contato['nome']))
                    print('Email: {}.'.format(contato['email']))
                    print('Telefone: {}.'.format(contato['telefone']))
                    print('-='*24)
                    break 
        else:
            print('Não existe contato cadastrado com o email {}.'.format(email))     
    else:
        print('Não existem contatos cadastrados.\n')

def listar(lista):
    if len(lista)>0:
        for i, contato in enumerate(lista):
            print('Contato {}:'.format(i+1))

            print('\tNome: {}'.format(contato['nome']))
            print('\tEmail: {}.'.format(contato['email']))
            print('\tTelefone: {}.'.format(contato['telefone']))
            print('-='*24)
        print('Quantidade de contatos: {}'.format(len(lista)))

    else:
        print('Não existem contatos cadastrados.')

def principal():

    lista = carregar_contatos() #aqui inicia a lista

    while True:
        print('-'*48)
        print('=====================AGENDA=====================')
        print('-'*48)
        print('')
        print('Para adicionar contato tecle-----------------[1]')
        print('Para alterar contatos tecle------------------[2]')
        print('Para remover contato tecle-------------------[3]')
        print('Para buscar nomes existentes tecle-----------[4]')
        print('Para exibir todos os contato tecle-----------[5]')
        print('Para sair tecle------------------------------[6]')
        print('')
        print('-'*48)
        print('')
        opcao = int(input('Digite o número da sua escolha: '))

        if opcao == 1:
            adicionar(lista)
            #salvar_contatos(lista)#sempre que modificar os contatos tem que salvar
        elif opcao == 2:
            alterar(lista)
            #salvar_contatos(lista)#sempre que modificar os contatos tem que salvar
        elif opcao == 3:
            excluir(lista)
            #salvar_contatos(lista)#sempre que modificar os contatos tem que salvar
        elif opcao == 4:
            buscar(lista)
        elif opcao == 5:
            listar(lista)
        elif opcao == 6:
            print('Saindo do programa...')
            break
        else:
            print('Opção inválida. Digite novamente.')


principal()














