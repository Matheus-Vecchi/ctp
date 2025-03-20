# Mostrar a categoria do nadador

# Operadore lógicos:
# and (e): verdadeiro se todas as condições forem verdade
# OR (ou): verdadeiro se apenas uma condição for verdade

idade = int(input('Digite sua idade: '))

if idade < 5 or idade > 80:
    print(f'Idade não permitida.')
else:
    if 5 <= idade <= 12:
        print(f'Categoria infantil.')
    elif 13 <= idade <= 18:
        print(f'Categoria juvenil.')
    elif 19 <= idade <= 59:
        print(f'Categoria adulta.')
    else:
        print(f'Categoria senior.')
