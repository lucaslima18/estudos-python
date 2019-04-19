#List é uma coleção ordenada e modificável. Permite membros duplicados.
thislist = ["lucas", "pedro", "mario"]
thiscopy = list(thislist)
print(thislist)

#alterar valor de uma lista
thislist[1] = "geraldo"
print(thislist)

#loop através de uma lista
for x in thislist:
    print(x)

#verificar se o item existe
name = ["geraldo", "miguel", "lucas", "bárbara", "pedro", "mario"]

for n in name:
    if n in thislist:
        print(f"sim, temos um {n} neste lista!!!")

    else:
        print(f"Me desculpa mas não consegui encontrar nenhum(a) {n} nesta lista!!!")

#Determinar quantos itens uma lista possui
#utilizando o método len()-retorna o cumprimento da lista ou string
clone = input("Digite algo que eu te digo o tamanho:")

print(f"O tamanho da Sting é: {len(clone)}")

#adicionar itens
#com o metodo append()
thislist.append("Orange")
thislist.append("34")
thislist.append(len(clone))

#para adicionar no índice especificado
thislist.insert(2, "jooj")
print(f"agora a lista ficou assim: {thislist}")

#acessar itens
#referir ao número do índice
#tive que colocar o input dentro do int pois caso contrário ele me retornaria uma string
position = int(input("Digite a posição que você deseja acessar na lista:"))

try:
    print(thislist[position])
except:
    print("esta posição não existe na lista!")

#remover item
#utilizando o método remove()
rem1 = input("digite o que você deseja remover da lista:")
try:
    thislist.remove(rem1)
    print(f"agora a lista esta assim: {thislist}")
except:
    print(f"não existe {rem1} nesta lista!!!")


#utilizando pop()- remove o índice especificado
rem2 = int(input("digite a posição do que você deseja remover da lista:"))

try:
    thislist.pop(rem2)
    print(f"agora a lista esta assim {thislist}")
except:
    print(f"não existe a posição {rem2} nesta lista!!!")

#utilizando del- palavra chave que remove o índice especificado
rem3 = int(input("digite a posição do que você deseja remover da lista:"))

try:
    del thislist[rem3]
    print(f"agora a lista esta assim {thislist}")
except:
    print(f"não existe a posição {rem3} nesta lista!!!")

#Copiar uma lista
#Você não pode copiar uma lista simplesmente digitando list2 = list1, porque: list2será apenas uma referência para list1, e as alterações feitas list1também serão feitas automaticamente em list2.
#Utilize então o método copy()
thislist2 = thislist.copy()

#Esvaziar lista
#utiliza-se o método clear()
thislist.clear()
print(f"a lista agora está vazia: {thislist}")
print(f"mas ainda bem que tenho um beckup: {thislist2}")
print(f"lembrando que no começo a lista estava assim: {thiscopy}")

#outros métodos
#count() -retorna o número de vezes que um elemento se repetiu
find = input("o que você desja procurar na lista?")
print(f"A quantidade de vezes que este elemento se repete é: {thislist2.count(find)}")

#extent() -permite unir duas listas distintas
carlist1 = ["uno", "bmw", "masserati"]
carlist2 = ["audi", "mustangue", "ferrari"]
carlist1.extend(carlist2)
print(f"Temos duas listas, a lita 1 tem: {carlist1}, e a lista 2: {carlist2}")
print(f"fundindo as duas temos: {carlist1}")

#index() -retorna o valor do índice do objeto
inp = input("procure algo na lista de carros:")
try:
    index = carlist1.index(inp)
    print(f"a posição de {inp}, é: {carlist1.index(inp)}")
except:
    print(f"o elemento {inp} não existe")

#reverse() -inverte a ordem da lista
print(f"a lista de carro é: {carlist1}")
carlist1.reverse()
print(f"o inverso dela é: {carlist1}")

#short() -organiza a lista em ordem alfabética
carlist1.sort()
print(f"em ordem alfabética, a lista de carros fica assim: {carlist1}")
listexamplenumeric = [1,3,9,4,3,4,2,8,12,3,54,7,331,2232,435,32,12,5,2]
print(f"temos uma lista desordenada de números: {listexamplenumeric}")
listexamplenumeric.sort()
print(f"agora ela está ordenada:{listexamplenumeric}")