#uma lista em é uma coleção ordenada e modificável
print("******LISTA DE COMPRAS******\n")
thislist = []
search = input("digite o que voce deseja procurar em nosso estoque:\n")

def adiciona_na_lista():
    z = str()
    print(z)
    while z != "nao": 

        binary = input(str("Você gostaria de alterar algo da lista?\n"))    
        if binary == 'sim':
            alterar_lista = input("Você deseja Adicionar ou Remover?\n")
            
            if alterar_lista == "adicionar":
                add = input("Digite o que você deseja Adicionar:\n")
                thislist.append(add)

            elif alterar_lista == "remover":
                try:
                    if thislist == []:
                        print("Desculpe, mas não há nada para remover!")
                        adiciona_na_lista
                    else:
                        rem = input("Digite o que você deseja Remover:\n")
                        thislist.remove(rem)
                        consultar_lista()
                except:
                    print("este item não existe")

            else:
                print("\n")
                print("Desculpe, não consegui te entender :(")
                adiciona_na_lista()
        
        elif binary == 'não' or binary == "nao":
            print("caiu no bate")
            consultar_lista()

        else:
            print("Desculpe, não consegui te entender :(")
            adiciona_na_lista()

def consultar_lista():
    binary3 = input("Quer consultar a sua lista de compras?")

    if binary3 == "sim":    
        print("\n")
        print("agora a lista tem:")
            
        for n in thislist:
            print(n)

    else:
        print("ok")

if thislist == []:
    print("\n")
    print("Sua Lista de Compras está vazia no momento!")
    adiciona_na_lista()

elif search in thislist:
    print(f"sim, temos {search} em nosso estoque !!!\n")
    adiciona_na_lista()

else:
    print(f"infelizmente não temos {search} em nosso estoque :(\n")
    adiciona_na_lista()

adiciona_na_lista()



#os itens de uma lista podem ser acessados referindo - se o numero do indice
#print(f"desta list só quero 0 {thislist[2]}")
#print("nesta lista temos apenas:")
#for l in thislist:
    #print(l)








