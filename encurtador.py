from tkinter import *
from tkinter import messagebox
import pyautogui
import pyshorteners
import pyperclip


app = Tk()
app.title('ENCURTADOR DE LINK')
app.geometry('300x200')
app.configure(background='black')
app.iconbitmap('link_20914.ico')





def Encurta():
    global saida
    global entrada
    entrada = entrada.get()
    S = pyshorteners.Shortener().tinyurl.short(entrada)
    saida = print(S)
    S = vartexto.set(S)
    pyautogui.hotkey('ctrl','a')
    pyautogui.press('delete')
    
    saida = vartexto.get()
    
    arquivo = open('LINK_encurtado.txt', 'w')
    print(saida, file=arquivo) 
    arquivo.close()
    valor_str = str(saida)
    pyperclip.copy(valor_str)
    pyautogui.alert('Seu link foi copiado, e salvo em TXT na mesma pasta do progama!\n clique em OK \n')
    app.destroy()
    
    
    
    
    
    
    
    
    
vartexto = StringVar()

espaco = Label(app,bg='black').pack()
link = Label(app,text='cole seu link abaixo',bg='black',fg='green').pack()    
espaco = Label(app,bg='black').pack()
entrada = Entry(app,fg='blue',bg='#bcb9b0')
entrada.pack()

espaco = Label(app,bg='black').pack()


saida = Label(app, textvariable=vartexto,bg='black',fg='orange').pack()

espaco = Label(app,bg='black').pack()



bt = Button(app,text='Encurtar Link', activeforeground='white',activebackground='green' ,bg='orange',command=Encurta).pack()



    
    
    
    
    
    
    
    
    
    
    
    
    
    
app.mainloop()