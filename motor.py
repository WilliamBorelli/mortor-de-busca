# -*- coding: UTF-8 -*-
#!/usr/bin/python

#Autores:
# Lucas de Andrade
# Sidércio Paraíso
# Vitor Hugo
# William Borelli 


import urllib
limite_maximo=5

def pega_pagina(url):#Essa função é apenas para retornar o conteúdo de uma página web; o código fonte de uma página web quando uma url é dada.
	try:
		f = urllib.urlopen(url)
		pagina = f.read()
		f.close()
		#imprimir página
		return pagina
	except:	
		return ""
	return ""

def uniao(a,b):# A função que une a segunda lista na primeira, sem duplicar um elemento de a, se já estiver em a. Similar a configurar o operador de união. Essa função não altera b. Se a=[1,2,3] b=[2,3,4]. Depois da união(a,b), ela transforma a=[1,2,3,4] e b=[2,3,4].
	for e in b:
		if e not in a:
			a.append(e)

def pega_proximo_url(pagina):
	comeco_link=pagina.find("a href")
	if(comeco_link==-1):
		return None,0
	comeco_aspas=pagina.find('"',comeco_link)
	fim_aspas=pagina.find('"',comeco_aspas+1)
	url=pagina[comeco_aspas+1:fim_aspas]
	return url,fim_aspas

def pega_todos_links(pagina):
	links=[]
	while(True):
		url,n=pega_proximo_url(pagina)
		pagina=pagina[n:]
		if url:
			links.append(url)
		else:
			break
	return links

def Procurar(index,palavra_chave):#Essa função é para criar um indexador, e encontrar a plavra chave no indexador e retornar uma lista de links.
	#f=[]
	if palavra_chave in index:
		return index[palavra_chave]
	return []
#O formato do elemento no indexador é <palavra_chave>, [<Lista de urls que contém a palavra-chave>]
def add_para_index(index,url,palavra_chave):

	if palavra_chave in index:
		if url not in index[palavra_chave]:
			index[palavra_chave].append(url)
		return
	index[palavra_chave]=[url]

def add_pagina_para_index(index,url,conteudo):#Adicionando o conteúdo da página web no index.
	for i in conteudo.split():
		add_para_index(index,url,i)

def calcula_ranks(grafo):#Calculando os rankings para um dado grafo -> para todos os links nele
	d=0.8
	numloops=10
	ranks={}
	npaginas=len(grafo)
	for pagina in grafo:
		ranks[pagina]=1.0/npaginas
	for i in range(0,numloops):
		novosranks={}
		for pagina in grafo:
			novorank=(1-d)/npaginas
			for no in grafo:
				if pagina in grafo[no]:
					novorank=novorank+d*ranks[no]/len(grafo[no])
			novosranks[pagina]=novorank
		ranks=novosranks
	return ranks
	
def Rastrear_web(semente):#O site age como uma página "semente" quando é dado como input
	rastrear=[semente]
	rastreado=[]
	index={}
	grafo={}#novo grafo
	global limite_maximo
	while rastrear:
		p=rastrear.pop()
		if p not in rastreado:#Para remover o looping, se uma página já está rastreada e é linkada de volta por algum outro link que estamos rastreando, nós não precisaremos rastrear novamente 
			limite_maximo-=1
			print limite_maximo
			if limite_maximo<=0:
				break
			c=pega_pagina(p)
			add_pagina_para_index(index,p,c)
			f=pega_todos_links(c)
			uniao(rastrear,f)
			grafo[p]=f
			rastreado.append(p) #Logo que um link é rastreado ele é incluído na lista "rastreado". No final, quando todos os links tiverem acabado, retornaremos os rastreados desde que contenham todos os links que temos
	return rastreado,index,grafo #Retorna uma lista de links

#Imprime o index	


def QuickSort(paginas,ranks):#Organiza em ordem decrescente
	if len(paginas)>1:
		piv=ranks[paginas[0]]
		i=1
		j=1
		for j in range(1,len(paginas)):
			if ranks[paginas[j]]>piv:
				paginas[i],paginas[j]=paginas[j],paginas[i]
				i+=1
		paginas[i-1],paginas[0]=paginas[0],paginas[i-1]
		QuickSort(paginas[1:i],ranks)
		QuickSort(paginas[i+1:len(paginas)],ranks)

def Procurar_novo(index,ranks,palavra_chave):
	paginas=Procurar(index,palavra_chave)
	print '\nImprimindo os resultados como em uma página rankeada\n'
	for i in paginas:
		print i+" --> "+str(ranks[i])# Exibindo as listas, dessa forma pode-se ver o rank da página ao lado
	QuickSort(paginas,ranks)
	print "\nDepois de ordenar os resultados por rank de pagina\n"
	pag=0
	for i in paginas:#Isso é exatamente como aparecerá nos resultados do motor de busca - > organizado por rank de página
		pag+=1
		print str(pag)+'.\t'+i+'\n' 


#print index
print "Insira a página que servirá de semente"
pagina_semente=raw_input()
print "O que você deseja procurar?"
busca_termo=raw_input()
try:
	print "Coloque a profundidade que você gostaria de ir"
	limite_maximo=int(raw_input())
except:
	f=None
print '\nComeçando a rastrear, na profundidade...'
rastreado,index,grafo=Rastrear_web(pagina_semente)#Imprimindo todos os links

ranks=calcula_ranks(grafo)#Calculando os rankings da página
Procurar_novo(index,ranks,busca_termo)
