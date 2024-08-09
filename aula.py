import random
# Atividade R:2
def is_str(text):
    return isinstance(text, str)

name = input('Digite seu nome: ')
if not is_str(name):
    print('Você não digitou um nome válido.')

last_name = input('Digite seu sobrenome: ')
if not is_str(last_name):
    print('Você não digitou um sobrenome válido.')

print(f'Seu nome completo é: {name} {last_name}')

# Atividade R:1
num = random.randint(0, 100)
print('Número Aleatório:', num)
print('O quadrado deste número é:', num**2)

# Atividade R:3
num1_str = input('Por gentileza informe um número: ')
if not num1_str.isdigit():
    print('Você não digitou um número válido. Por favor, digite apenas números.')
else:
    num1 = int(num1_str)

num2_str = input('Digite mais um número: ')
if not num2_str.isdigit():
    print('Você não digitou um número válido. Por favor, digite apenas números.')
else:
    num2 = int(num2_str)

print(f'Os números Escolhidos foram : {num1} {num2}')

# Atividade R:4
name_python = "Python"
print(f'{name_python}{num1}{num2}') 

# Atividade R:5
frase_do_dia = "O Mundo é um/a "
palavra = input('Digite uma palavra: ')
print(f'{frase_do_dia} {palavra}')