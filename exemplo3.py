# Estrutura de decisão if...elif...else (usar quando tem 3 ou mais situações)

# Exemplo: mostrar se um número inteiro é positivo, negativo ou neutro

num = int(input('Digite um número inteiro: '))

if num > 0:
    print(f'O número {num} é positivo!')
elif num < 0:
    print(f'O número {num} é negativo!')
else:
    print(f'{num} é neutro!')
