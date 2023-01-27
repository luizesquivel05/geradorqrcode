import qrcode
import os
import time as tm

while True:
    print('Vamos começar o programa! Nos diga o conteúdo, que deseja colocar:')
    data = str(input('Digite o conteúdo: '))
    codigo = qrcode.make(data)
    print('Estamos gerando o QR Code')
    tm.sleep(2)
    codigo.save('qrcode.png')
    print('Salvamos o seu QR Code!')
    requisito = int(input('Digite 0 para fazer outro e 1 para finalizar o programa: '))
    if requisito != 1: os.system('cls')
    else: break