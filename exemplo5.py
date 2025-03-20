# Criar um menu de opcoes pro usuario escolher uma das 3 operacoes

num1 = int(input('Digite um número: '))
num2 = int(input('Digite o outro número: '))

print('[1] -> Somar')
print('[2] -> Subrtair')
print('[3] -> Multiplicar')
print('[4] -> Dividir')

operacao = int(input('Digite a operação que deseja: '))

match operacao:
    case 1:
        print(f'A soma deu {num1 + num2}.')
    case 2:
        print(f'A subtração deu {num1 - num2}.')
    case 3:
        print(f'A multiplicação deu {num1 * num2}.')
    case 4:
        print(f'A divisão deu {num1 / num2}.')
