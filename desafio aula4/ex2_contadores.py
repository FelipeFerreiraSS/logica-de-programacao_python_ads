inicial = int(input('Qual o numero inicial?'))
final = int(input('Qual o numero final?'))

x = inicial
while( x <= final):
    if(x % 2 == 0):
        print(x)
    x = x + 1