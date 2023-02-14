import tkinter as tk
import qrcode

def gerarQRCODE(conteudo):
    data = str(conteudo)
    codigo = qrcode.make(data)
    codigo.save('qrcode.png')
    
def lerCONTEUDO():
    dados = conteudo.get()
    gerarQRCODE(dados)
    tk.Label(font=('Montserrat', 12), text=f"Geramos um QR CODE com as informações: {dados}{' '*50}").place(x=5, y=120)
    tk.Label(font=('Montserrat', 12), text=f"Verificar a pasta do projeto pelo explorador de arquivos").place(x=5, y=160)

home = tk.Tk()
home.geometry('600x300')
home.wm_iconbitmap('qrcode.ico')
home.resizable(False, False)
home.title("Gerador QR Code | HOME")
tk.Label(font=('Montserrat', 20), text="GERADOR QR CODE").place(x=150, y=10)
conteudo = tk.Entry(home, font=('Montserrat', 14)); conteudo.place(x=30, y=60)
enviarCONTEUDO = tk.Button(master=home, font=('Montserrat', 14), text="ENVIAR CONTEÚDO", fg='white', background='red', command=lerCONTEUDO); enviarCONTEUDO.place(x=300, y=50)
home.mainloop()