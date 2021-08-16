# listas em python usa colchetes [] , e pode mudar valores d elementos
# para adicionar um novo elemento no final da lista usa o metodo append
# para adicionar um no elemento na lista em qualquer lugar usa o metodo insert
# para eliminar um elemento de lista usa o del xxxx [3] ele elimina o elemento 3. ou o xxx.pop(3) mesma coisa , tambem tem o  xxxx.remove('str')o elemento escrito

# num = [2,5,9,1]
# num [2] = 3 #transformar quem esta no indice 2 em 3
# num.append(7)#acrescenta o 7 na ultima posição
# num = (sorted(num))#coloca em ordem numerica
# #num.sort(reverse=True)#coloca em ordem inversa
# #num.insert(2,0)#inseri o numero 0 no indice 2
# #num.pop(2)#apaga o numero do indice 2
# #num.remove(7)#ele remove o numero que esta no parentese
# # if 5 in num: #uma estrutura q remove diretamente o numero que quer se ele existir
# #     num.remove(5)
# # else:
# #     print('não achei')
# print(num)
# print(f'essa lista tem {len(num)} elementos.')#mostra quantos elemtos tem na lista


# valores = []
# for cont in range(0,5):
#     valores.append(int(input('Digite um valor: ')))
# valores.append(5)
# valores.append(9)
# valores.append(4)
# for c, v in enumerate(valores):
#     print(f'na posição {c} encontrei o valor {v}!')
# print('cheguei ao fim da lista.')


a = [2,3,4,7]
b = a#isso cria uma ligação entre eles tudo que faz em um acontece no outro tambem 
b = a[:]#isso faz uma copia
print(f'Lista A: {a}')
print(f'Lista B: {b}')







