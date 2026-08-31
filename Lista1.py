#Questao 1 lista 1##
numero = int(input("Digite um número: "))

sobra = numero % 2

if (sobra == 0 ):
    print("É um número par!")
else:
    print("É um número impar!")

#Questao 2 lista 1##

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))

if (numero1 > numero2):
    print(f"{numero1} é maior!")
else:
    print(f"{numero2} é maior!")

#Questao 3 lista 1##

letra = input("Digite uma letra: ")

if (letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u'):
    print("É vogal!")
else:
    print("É consoante!")

#Questao 4 lista 1##

nota1 = float(input("Digite a 1° nota: "))
nota2 = float(input("Digite a 2° nota: "))

media = (nota1 + nota2) / 2

if (media == 10):
    print("Aprovado com distinção!")
elif (media < 7):
    print("Reprovado!")
elif (media >= 7):
    print("Aprovado!")

#Questao 5 lista 1##

numero1 = float(input("Digite o 1° número: "))
numero2 = float(input("Digite o 2° número: "))
numero3 = float(input("Digite o 3° número: "))

if (numero1 > numero2 and numero1 > numero3):
    print(f"{numero1} é o maior número!")
elif (numero2 > numero1 and numero2 > numero3):
    print(f"{numero2} é o maior número!")
elif (numero3 > numero1 and mumero3 > numero2):
    print(f"{numero3} é o maior número!")

#Questao 6 lista 1##

turno = input("M- Matutino\nV- Vespetino\nN- Noturno\nQual turno você estuda? ").upper()

if (turno == 'M'):
    print("Bom dia!")
elif (turno == 'V'):
    print("Boa tarde!")
elif (turno == 'N'):
    print("Boa noite!")
else:
    print("Valor inválido!")

#Questao 7 lista 1##

pontos = 0

resposta = input("Telefonou para vítima? ").lower()
if (resposta == "sim"):
    pontos += 1

resposta = input("Esteve no local do crime? ").lower()
if (resposta == "sim"):
    pontos += 1

resposta = input("Mora perto da vítima? ").lower()
if (resposta == "sim"):
    pontos += 1

resposta = input("Devia para a vítima? ").lower()
if (resposta == "sim"):
    pontos += 1

resposta = input("Já trabalhou com a vítima? ").lower()
if (resposta == "sim"):
    pontos += 1

if (pontos == 2):
    print("Suspeito!")
elif (pontos == 3 or pontos == 4):
    print("Cúmplice!")
elif (pontos == 5):
    print("Assasino!")
else:
    print("Inocente!")

#Questao 1 lista 2(Basico)##

contador = 0

while (contador <= 100):
    print(contador)
    contador += 1

#Questao 2 lista 2(Basico)##

contador = 0
numero = int(input("Digite um número: "))

while (contador <= numero):
    print(contador)
    contador += 1

#Questao 3 lista 2(Basico)##

print("Operação - Adição!")

resposta = 'S'

while (resposta == 'S'):
    numero1 = int(input("\nDigite um número: "))
    numero2 = int(input("Digite outro número: "))
    soma = numero1 + numero2
    print(f"\n{numero1} + {numero2} = {soma}")
    resposta = input("\nDeseja realizar mais uma soma? [S ou N]\nresposta: ").upper()

#Questao 1 lista 2(Desafios)##

anterior = 0
atual = 1
proximo = 1

while (proximo <= 500):
    print(anterior)
    proximo = anterior + atual
    anterior = atual
    atual = proximo
    
#Questao 2 lista 2(Desafios)##

quantidade = int(input("Quantos números você vai digitar? "))
contador = 0 
soma = 0

while (contador < quantidade):
    contador += 1
    numero = int(input(f"Digite o {contador}° número: "))
    soma += numero
    
    if (contador == 1):
        maior = numero
        menor = numero
    
    if (numero > maior):
        maior = numero
    
    if (numero < menor):
        menor = numero

print(f"Maior número: {maior}")
print(f"Menor número: {menor}")
print(f"Soma: {soma}")

#Questao 3 lista 2(Desafios)##

quantidade = int(input("Quantos números você vai digitar? "))
contador = 0 
soma = 0

while (contador < quantidade):
    contador += 1
    numero = int(input(f"Digite o {contador}° número: "))
    while (numero < 0 or numero > 1000):
        numero = int(input(f"Número inválido, Digite o {contador}° novamente: "))
    soma += numero
    
    if (contador == 1):
        maior = numero
        menor = numero
    
    if (numero > maior):
        maior = numero
    
    if (numero < menor):
        menor = numero

print(f"Maior número: {maior}")
print(f"Menor número: {menor}")
print(f"Soma: {soma}")

#Questao 4 lista 2(Desafios)##

nome = input("Digite seu nome: ")

while(len(nome) < 3):
    nome = input("Nome inválido, digite seu nome novamente: ")

idade = int(input("Digite sua idade: "))

while(idade < 0 or idade > 150):
    idade = int(input("Idade inválida, digite sua idade novamente:"))

salario = float(input("Digite seu salário: "))

while(salario < 0):
    salario = float(input("Salário inválida, digite seu salário novamente:"))

sexo = input("Digite seu sexo [M ou F]: ").upper()

while(sexo != 'M' and sexo != 'F'):
    sexo = input("Sexo inválido, digite seu sexo novamente: ").upper()

estadocivil = input("Digite seu estado civil [S, C, V, D]: ").upper()

while(estadocivil != 'S' and estadocivil != 'C' and estadocivil != 'V' and estadocivil != 'D'):
    estadocivil = input("Estado civil inválido, digite seu estado civil novamente: ").upper()

#Questao 5 lista 2(Desafios)##

numero = int(input("Digite um número: "))
divisor = 2
primo = True 

while (divisor < numero):
    if (numero % divisor == 0):
       primo = False
    divisor += 1

if (primo == True):
    print(f"{numero} é um número primo")
else:
     print(f"{numero} não é um número primo")