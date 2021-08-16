#segunda parte de listas

# galera = [['joão', 19], ['ana', 33], ['joaquim', 13], ['maria', 45]]
# for pessoa in galera:
#     print(f'{pessoa[0]} tem {pessoa[1]} anos de idade')

# galera = list()
# dado = list()
# for c in range(0,3):
#     dado.append(str(input('Nome: ')))
#     dado.append(int(input('Idade: ')))
#     galera.append(dado[:])
#     dado.clear()
#     print(galera)

galera = list()
dado = list()
totmaior = totmenor = 0
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for pessoa in galera:
    if pessoa[1] >= 21:
        print(f'{pessoa[0]} é maior de idade.')
        totmaior +=1
    else:
        print(f'{pessoa[0]} é menor de idade.')
        totmenor +=1
print(f'temos {totmaior} maiores e {totmenor} menores de idade.')















