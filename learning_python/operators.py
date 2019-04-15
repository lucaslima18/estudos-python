#aritiméticos
print("\nOperadores Aritiméticos:")
a = 1
b = 2
print(f"o valor de a é {a} e o de b é {b}, logo:")

soma = a + b
print(f"a + b = {soma}")

subtracao = a - b
print(f"a - b = {subtracao}")

multiplicacao = a * b
print(f"a * b = {multiplicacao}")

divisao = a / b
print(f'a / b = {divisao}')

#modulus exibe o resto da divisão
modulus = a % b
print(f"a % b = {modulus}")
print("-----------------------------------------\n")

#atribuição 
print("Operadores de Atribuições")

#atribuir um valor
x = 5
print(f"o valor de x é: {x}, logo:")

#incremento
y = x
y += 3
print(f"y += 3: {y}")

#decremento
z = x
z -= 3
print(f"x -= 3: {z}")

#x = x * 3
w = x
w *= 3
print(f"x *= 3: {w}")

#x = x / 3
d = x
d /= 3
print(f"x /= 3: {d}")
print("-----------------------------------------\n")

#comparação
print("Operadores de Comparação:")
comp1 = 12
comp2 = 21
print(f"aqui temos comp1 = {comp1} e comp2 = {comp2}")

if comp1 == 12:
   print(f"o valor de comp1 é igual a: {comp1}")
else:
    print("erro")

if comp1 != comp2:
    print("comp1 é diferente de comp2")
else:
    print("erro")

if comp1 < comp2:
    print("comp1 é menor que comp2")
else:
    print("erro")

if comp2 > comp1: 
    print("comp2 é maior que comp1")

maig = ">="
meig = "<="

print(f"temos também os operadores maior igual: {maig}, e menor igual: {meig}")
print("-----------------------------------------\n")

#lógicos
print("Operadores Lógicos:")
log1 = 4
log2 = 3
print(f"neste caso teremos log1 = {log1} e log2 = {log2}")

if log1 and log2 > 0:
    print("log1 e log2 são maiores que zero")
else:
    print("erro")

if log1 == 4 or log2 == 4:
    print("Bem, um deles é igual a quatro")
else:
    print("erro")

#para Inverter o resultado, ou seja, retornar False se o resultado for verdadeiro
if not(log1 == 4):
    print("erro")
else:
    print("aqui o resultado voltou invertido, mesmo que log1 seja igual a 4, por causa do operador not()")


#identidade
print("Operadores de Identidade")
x = 10

#verifica se um objeto é igual a outro
print(x is 10)

#verifica se não é 
print(x is not 10)

j = ["lucas", "john", "leo", 10]
k = 10
print(10 in j)
#ssociação
#bit a bit