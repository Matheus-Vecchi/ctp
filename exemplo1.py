# Estruturas de Decisão no Python

# 2 Situações

# Exemplo: Mostrar se um aluno foi aprovado ou reprovado de acodo com a média (>= 7 aprovado / <= 6 reprovado)

media = float(input('Média do aluno: '))

if media >= 7:
    print(f'Aprovado com média {media:.2f}!')
elif 5 <= media <= 7:
    print(f'Recuperação!')
else:
    print(f'Reprovado!')
