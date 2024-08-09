# Exercício 1
print('NÚMEROS PARES')
def numeros_pares(inicio, fim):
  
  pares = []
  for numero1 in range(inicio, fim + 1):
    if numero1 % 2 == 0:
      pares.append(numero1)
  return pares

inicio1 = 1
fim1 = 20
resultado1 = numeros_pares(inicio1, fim1)
print(resultado1)  

# Exercício 2

print('MULTIPLOS DE 5')

def multiplos_cinco(inicio2, fim):
  
  multiplos = []
  for numero in range (inicio2, fim + 4):
    if numero % 5 == 0: 
      multiplos.append(numero)
  return multiplos

inicio2 = 1
fim2 = 50
resultado2 = multiplos_cinco(inicio2, fim2)
print (resultado2)

# Exercício 3

print('FUNÇÃO TYPE EM AÇÃO')

v = 0==0
tipo = type(v)
print(tipo)
v = str(v)
tipo = type(v)
print(tipo)

# Exercício 4 

print('SAUDAÇÃO PERSONALIZADA')

saudacao = input('Digite seu nome para uma grande saudação: ')
print(f'Bom dia. É um prazer conhecê-lo(a). {saudacao}')

# Exercício 5

print('NÚMEROS IMPARES')

def numeros_impares(inicio3,fim3):
  
  impares = []
  for numero3 in range (inicio3, fim3 - 1):
    if numero3 % 2 == 1:
      impares.append(numero3)
  return impares

inicio3 = 1
fim3 = 11
resultado3 = numeros_impares(inicio3, fim3)
print(resultado3)

