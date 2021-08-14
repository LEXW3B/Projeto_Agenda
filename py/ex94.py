# criar um program que leia nome, sexo, idad de varias pessoas, guardando os dados de cada pessoa em um dicionario em uma lista.no final mostra:
# --QUANTAS PESSOAS CADASTRADAS
# --A MEDIA DE IDADE
# --UMA LISTA COM MULHERS
# --UMA LISTA COM IDADE ACIMA DA MEDIA

galera= list()
pessoa = dict()
while True:
    pessoa.clear()
    pessoa['nome']=str(input('nome: '))
    while True:
        pessoa['sexo'] = str(input('sexo: [M/F]'))
        if pessoa ['sexo'] in  'm/f':
            break
        print('ERROR! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('idade: '))
    galera.append(pessoa.copy())
    while True:
        resp = str(input('quer continuar ? S/N ')).upper()[0]
        if resp in  'SN':
            break
        print(ERROR! Responda apenas S ou N.)
    if resp == 'N':
        break
print('-='*30)
print(galera)















