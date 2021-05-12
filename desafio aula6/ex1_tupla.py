mochila = ('machado', 'camisa', 'comida', 'aqua')
print(mochila)
print(mochila[1])
print(mochila[0:2]) #elementos 1 e 2, indice 0 e 1
print(mochila[2:])  #elementos apartir do 2
print(mochila[-1])  #ultimo elemento
print('-----------------------------')
# varendo tupla
for item in mochila:
    print('Na mochila tem: {}'.format(item))

#somando
tupla1 = ('maça', 'banana')
tupla2 = ('laranja', 'melancia')

#desenpacotamento
def soma(*num):
    soma = 0
    print('tupla: {}'.format(num))
    for i in num:
        soma += i
    return soma
print('resulatado: {}\n'.format(soma(1,2)))
print('resulatado: {}\n'.format(soma(1,2,3,4,5,6,7,8,)))

soma = tupla1 + tupla2
print(soma)