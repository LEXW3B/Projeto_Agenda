nome = input('nome: ')
massa = float(input('massa (Kg):  '))
altura = float(input('altura (m):  '))
IMC = massa/(altura*altura)
print('-='*15)
print('Nome\tAltura\tMassa\tIMC\n{}\t{:.2f}\t{:.1f}\t{:.2f}'.format(nome, altura, massa, IMC))