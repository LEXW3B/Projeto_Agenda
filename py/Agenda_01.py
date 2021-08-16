lista = list()
dicionario = dict()
while True:# Estrutura de repetição
    print('-'*48)
    print('=====================AGENDA=====================')
    print('-'*48)
    print('')
    print('Para adicionar contato tecle-----------------[1]')
    print('Para buscar nomes existentes tecle-----------[2]')
    print('Para alterar contatos tecle------------------[3]')
    print('Para remover contato tecle-------------------[4]')
    print('Para exibir todos os contato tecle-----------[5]')
    print('Para sair tecle------------------------------[9]')
    print('')
    print('-'*48)
    print('')
    escolha = int(input('Digite o número da sua escolha: '))#Faz escohas
    
    if escolha == 1:# Estrutura da primeira escolha
        #dicionario.clear()
        dicionario['nome'] = str(input('nome:  '))
        dicionario['Telefone'] = int(input('Telefone:   '))
        dicionario['email'] = (input('email:   '))
        dicionario['Twitter'] = (input('Twitter:   '))
        dicionario['Instagram'] = (input('Instagram:   '))
        lista.append(dicionario.copy())
       
        while True:
            escolha = str(input('quer continuar ? S/N   ')).upper()[0]
            if escolha in  'SN':
                break
            print('ERROR! Responda apenas S ou N.')
            if escolha == 'SN':
                escolha == escolha#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

    elif escolha == 2:#buscar por nomes existentes
        nome = input('Pesquisar: ')
        print(nome, dicionario.items())



        # for k, v in dicionario.items():
        #     print(f' {k} = {v}')    
        
        
        
        

    elif escolha == 3:#alterar contato existente
        print()
    elif escolha == 4:#remover um contato existente
        del dicionario['nome']
        for k, v in dicionario.items():
            print(f'O {k} = {v} foi removido')  
        #print=('Contato removido.')#problema 03





    elif escolha == 5:#Esta pronto imprime tudo salvo no dicionarioxxxxxxxxxxxxxxx
        print(dicionario)
    elif escolha == 9:#final do programa funcionandoxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        print('Fim de programa')
        break  
print('-='*30)
print(lista)






# nome = dict(dicionario)
#         print(dicionario)