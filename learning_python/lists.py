#uma lista em é uma coleção ordenada e modificável
thislist = ["maçã", 'banana', "morango"]

search = input("digite o que voce deseja procurar em nosso estoque:\n")

if search in thislist:
    print(f"sim, temos {search} em nosso estoque !!!\n")

else:
    print(f"infelizmente não temos {search} em nosso estoque :(\n") 

#os itens de uma lista podem ser acessados referindo - se o numero do indice
#print(f"desta list só quero 0 {thislist[2]}")
print("nesta lista temos apenas:")
for l in thislist:
    print(l)

add = input("deseja adicionar alguma coisa a sua lista de compras?")






