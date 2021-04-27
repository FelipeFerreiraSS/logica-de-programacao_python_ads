km = int(input('Quantos quilometros foram percoridos? '))
dias = int(input('Quantos dias você ficol como carro? '))

preco = 60 * dias + 0.15 * km
print('Km: {} , Dias: {}' .format(km, dias))
print('Valor a ser pago: {}' .format(preco))