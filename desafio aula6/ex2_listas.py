mochila = ['machado', 'camisa', 'comida', 'agua']
print(mochila)

#alterar lista
mochila[2] = 'laranja'
print(mochila)

# manipular lista
print('---------- manipular listas')
mochila.append('bota') #adicionando
print(mochila)
mochila.insert(1,'meia') #adicionar em posição especifica
print(mochila)
del mochila[2] #deletar
print(mochila)
mochila.remove('agua') #remover
print(mochila)

#copia
print('-------------copia')
x = [1,3,4,5,6,]
y = x[:]
print(x)
print(y)