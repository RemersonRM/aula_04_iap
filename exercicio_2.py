n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
s = (n1+n2)/2
if s > 6.0:
    print('Você foi aprovado!')
    print(f'Média: {s}')
else:
    print('Você foi reprovado!')
    print(f'Média: {s}')