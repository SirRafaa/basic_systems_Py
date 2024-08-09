import random 

# Atividade 1
print('Boas Vindas ao Sistema')

# Atividade 2
casado = True
print("Casado ou solteiro: ",casado)

# Atividade 3
nume1 = random.randint(0, 100)
nume2 = random.randint(0, 100)
multiplicar_dois_numeros = nume1 * nume2 
print(f'A multiplicação de dois números: {nume1} * {nume2} = {multiplicar_dois_numeros}')

# Atividade 4

div1 = random.randint(1, 100)
div2 = random.randint(1, 100)
dividir_dois_numeros = div1 / div2
print(f'Divisão de dois números: {div1} / {div2} = {dividir_dois_numeros:.2f}')

# Atividade 5
sub1 = random.randint(0, 100)
sub2 = random.randint(0, 100)
subtrair_dois_numeros = sub1 - sub2 
print(f'Subtração de dois números: {sub1} - {sub2} = {subtrair_dois_numeros}')

# Atividade 6
div3 = random.randint(1, 100)
div4 = random.randint(1, 100)
dividir_dois_numeros2 = div3 / div4
print(f'Divisão de dois números: {div3} / {div4} = {dividir_dois_numeros2:.2f}')

# Atividade 7 

decim1 = float(random.randint(0, 100))
decim2 = float(random.randint(0, 100))
multiplicar_decimais = decim1 * decim2
print(f'Multiplicar dois decimais: {decim1} * {decim2} = {multiplicar_decimais:.2f}')

# Atividade 8 
dobro = int(random.randint(0, 100))
dobrado = dobro*2
print(f'o dobro deste número: {dobro} É {dobrado}')

# Atividade 9 (calculadora)

def somar(numero1, numero2):
  return numero1 + numero2

def subtrair(numero1, numero2):
  return numero1 - numero2

def multiplicar(numero1, numero2):
  return numero1 * numero2

def dividir(numero1, numero2):
  if numero2 == 0:
    return "Divisão por zero!"
  else:
    return numero1 / numero2

numero1 = float(input('Digite um número: '))
numero2 = float(input('Digite um número: '))

operacao = input("Escolha a operação (+, -, *, /): ")
if operacao == '+':
  resultado = somar(numero1, numero2)
elif operacao == '-':
  resultado = subtrair(numero1, numero2)
elif operacao == '*':
  resultado = multiplicar(numero1, numero2)
elif operacao == '/':
  resultado = dividir(numero1, numero2)
else:
  print("Operação inválida!")

print("Resultado:", resultado)

# Atividade 10 

nome = input("Digite seu nome: ")
senha = input("Digite sua senha: ")

if senha == "1234":
    print("Bem-vindo(a),", nome + "!")
else:
    print("Senha incorreta.")