# tuplas em python usa parenteses()
lanche = ('hamburger', 'suco', 'pizza', 'pudim', 'batata frita')
print(lanche[:])
print(sorted(lanche))#mostra em ordem alfabetica
# tuplas são dentro e parenteses e são imutavéis

for comida in lanche:                  #jeito 01
    print(f'eu vou comer {comida}')
print('eita comi pra caramba!!!') 

# tuplas são dentro e parenteses e são imutavéis
for cont in range(0, len(lanche)):     #jeito 02
    print(f'eu vou comer {comida}')
print('eita comi pra caramba!!!') 


a = (2,5,4)
b = (5,8,1,2)
c = b + a
print(a)
print(b)
print(a+b)
print(sorted(a+b))#vai por em ordem numerica
print(c.count(5))#vai dizer quantas vezes o numero 5 foi repetido
print(c)
print(c.index(8))#vai dizer em qual posição esta o número 8
del(lanche)#vai apagar a tupla inteira






