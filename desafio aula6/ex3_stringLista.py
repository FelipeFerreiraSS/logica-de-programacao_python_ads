mochila = ['machado', 'camisa', 'comida', 'agua']

print(mochila[1][3])

#lista dentro de lista
mercado = []

for i in range(3):
    nome = input('digite o nome do item: ')
    qtd = int(input('digite a quantidade: '))
    valor = float(input('digite o valor: '))
    mercado.append([nome, qtd, valor])
print(mercado)
