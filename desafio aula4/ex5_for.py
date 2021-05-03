soma = 0
qtd = 0
for i in range(1,101):
    if (i % 2 == 0):
        soma += i
        qtd += i
media = soma / qtd
print('media é {}'.format(media))