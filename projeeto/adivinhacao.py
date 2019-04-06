print("*********************************")
print("Bem vindo ao Jogo de Adivinhação!")
print("*********************************")

#a variável deve ser definida com int(), para indicar que vai ter que receber um numero
chute = int(input("Digite o seu número:\n"))
numero_secreto = 42
acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto

print(f"seu chute foi: {chute}")

if acertou:
    print("parabéns!!!, você acertou!!!")

#elif == else if() 

else:
    if maior:
        print("você errou, seu chute foi maior que o número secreto")
    elif menor:
        print("você errou, seu chute foi menor que o número secreto")
   
print("Fim de Jogo!!!")