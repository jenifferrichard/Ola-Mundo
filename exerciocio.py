produtos = ('Notbook',  2500.00 ,
            'Mouse', 89.00, 
            'Monitor',  899.00, 
            'Teclado', 1500.00)
print('-' *40)
print(f'{"LISTA DE PREÇOS":^32}')
print('-' *40)
for posição in range(0, len(produtos)):
    if posição % 2 == 0:
        print(f'{produtos[posição]:.<30}', end='')
    else:
        print(f'R$ {produtos[posição]:>7.2f}')
print('-' *30)


       