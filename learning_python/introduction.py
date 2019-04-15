#criar variáveis
x = 1
y = 'lucas'
print(x)
print(y)

#criando variáveis com tuplas 
x, y = 1, 2
print(x, y)

#Para combinar texto e uma variável
a = "python is "
b = 'awersome'
text = a + b
print(text)
print(a, b)
print(f'{a}{b}')
print("what python is? " + a, b)
print(f"what python is? {a}{b}")

#existem 3 tipos numéricos (casting)
c = 1 
d = int(1)

e = 2.8
f = float(2.8)

g = 2j
h = complex(2j)

print("---------------")
print(f"tipos numéricos: {c} é do tipo {type(c)}, {e} é do tipo {type(e)}, e {f} é do tipo {type(g)}")
