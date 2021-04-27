produto = float(input('Qual o preço do produto? '))
percentual = float(input('Persentual do produto? '))

desconto = produto * (percentual / 100)
final = produto - percentual

print('o produto custa: {}. Menos o desconto de {}%. O preço fica: {}'.format(produto, percentual, final))
