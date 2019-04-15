#acessar os valores de uma string
s = "açaí não tem gosto de terra"

print(f"a string inteira é -{s}-")
print(f"na posição 3 temos {s[3]}, pois uma string começa na posição 0 que seria o {s[0]}")

#acessar de uma posição a outra
print(f"da posição 5 à 8 temos: {s[5:8]}")

#o metodo strip() remove todos os espaços no começo ou fim de uma string
s2 = " eu amo minha família "
print(s2.strip())

#substituir uma string por outra
ex = "serei substituido"
print(ex.replace("s", "o"))

#retornar a string em letras minúsculas
min = input(str('digite em letras maiúsculas:'))
print(min.lower())

#retornar a string em letras maiúsculas
max = input(str('escreva em letras minúsculas:'))
print(max.upper())


