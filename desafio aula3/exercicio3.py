print('O que deseja comprar?')
print('1 - maça')
print('2 - laranja')
print('3 - banana')
produto = int(input('Qual sua escolha?'))
qtd = int(input('Quantas quantidades?'))

if (produto == 1):
    pagar = qtd * 2.3
    print('Você comprol {} maças. Total a pagar R${}' .format(qtd, pagar))
elif (produto == 2):
    pagar = qtd * 3.6
    print('Você comprol {} laranjas. Total a pagar R${}'.format(qtd, pagar))
elif (produto == 3):
    pagar = qtd * 1.85
    print('Você comprol {} banana. Total a pagar R${}'.format(qtd, pagar))
else:
    print('produto invalido')