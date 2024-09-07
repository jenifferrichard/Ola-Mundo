from time import sleep
print('-' *30)
print(f'{"MEDIA DAS NOTAS":^30}')
print('-'*30)
n1 = int(input('Digite a sua nota de Português : '))
n2 = int(input('Digite a sua nota de Matemática : '))
nota = (n1 + n2) / 2
print('Calculando...')
sleep(2)
print(f'Sua nota total foi {nota} ')
sleep(2)
if nota > 8:
    print('Parabéns você é inteligente')
elif nota < 7 :
    print('Você ficou de Recuperação. ')
sleep(2)
recuperação = int(input('Digite a sua nota de Recuperação : '))
print('Verificando...')
sleep(2)
if recuperação < 5:
    print('Desisti, vc é muito BURRO 😎')