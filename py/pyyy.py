#biblioteca dicionarios
#pessoas=()estrutura para uma tupla
#pessoas=[]estruura para uma lista
#pessoas={}estrutura para um dicionario
#pessoas={'nome': 'gustavo', 'sexo': 'M', 'idade': '22'}
#print=(pessoas.keys())vai aparecer nome, sexo, idade
#print=(pessoas.values())vai aparecer gustavo, M, 22
#print(pessoas.items())vai mostar(nome,gustavo),(sexo,M),(idade,22)



#pessoas={'nome': 'gustavo', 'sexo': 'M', 'idade': '22'}
#print(pessoas.items())

#for k,v in pessoas.items():#O (k) é keys & o (v) é values
#    print(f'{k} = {v}')


           #novo

aluno =dict()
aluno['nome']=str(input('nome: '))
aluno['media']=float(input(f'media de {aluno["aluno"]}:'))
if aluno['media']>=7:
    aluno['situação']='Aprovado'
elif 5<= aluno ['media']<7:
    aluno['situação']='Recuperação'
else:
    aluno['situação']='Reprovado'
for k,v in aluno.items():
    print(f'{k} é igual a {v}')





