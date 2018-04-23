# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252

import pickle

#Função que imprime o cabeçalho
def header():
	print '____________________________________________'
	print '__  Trabalho da disciplina de Python 2.7  __'
	print '____________________________________________'
	print 'Digite o número da opção desejada: '
	print '1 - Entrar com as informações de peças'
	print '2 - Ver registro das peças'
	print '3 - Sair'

#Função que salva as peças
def save():
	arq = open('arq/pecas.dat', 'wb')
	for i in range(1,51):

		print 'CADASTRANDO O PRODUTO NÚMERO: ',i

		cod = int(raw_input('Digite o código do produto:'))
		peca = str(raw_input('Digite a peça:'))
		desc = str(raw_input('Digite a descrição do produto:'))
		qtd = int(raw_input('Digite a quantidade do produto em estoque:'))
		preco = float(raw_input('Digite o preço do produto em questão:'))

		pickle.dump(cod,arq)
		pickle.dump(peca,arq)
		pickle.dump(desc,arq)
		pickle.dump(qtd,arq)
		pickle.dump(preco,arq)

	print 'Produtos cadastrados com sucesso!'
	arq.close()		
	init()		

#Função que mostra as peças
def read():
	arq = open('arq/pecas.dat','rb')

	print 'TODOS OS PRODUTOS CADASTRADOS:'

	for i in range(1,51):
		cod = pickle.load(arq)
		peca = pickle.load(arq)
		desc = pickle.load(arq)
		qtd = pickle.load(arq)
		preco = pickle.load(arq)

		print '\033[32m Listando o produto: ', i , '\033[0;0m' 
		print 'Código : ', cod
		print 'Peça:', peca
		print 'Descrição: ', desc
		print 'Quantidade: ', qtd
		print 'Preço: ', preco

	arq.close()
	init()	

#Função principal
def init():
	
	header()

	answer = int(raw_input())

	if answer == 1:
	    save()

	elif answer == 2:
		read()

	elif answer == 3:
		print 'Fechando programa, até mais!'
		exit()

	else:	
		print 'Opção digitada inválida, vamos tentar novamente.'		
		init()


#Primeira chamada da função principal
init()


