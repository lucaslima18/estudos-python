#esta é a função de fibonacci, ela irá receber o valor da variável x que foi lhe passado como parâmetro no loop
def fibonacci(n):
    #este if faz com que o 0 e 1 sejam imprimidos 
    if n < 2:
        return n
    else:
        #formula de fibonacci
        return fibonacci(n-1)+fibonacci(n-2)

#neste loop é criada uma vaiável x que corresponderá a um numero do range por loop
for x in range(10):
    fibonacci(x)
print(fibonacci(x))

print("------------")

#observe que o resultado todal de intervalos é 9, pois o intervalo começa com 0
print(x)
