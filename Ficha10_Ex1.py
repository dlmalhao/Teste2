from tkinter import *
import os

window = Tk()
window.geometry("500x300")
window.title("Form 1")

def inserir ():
    os.chdir("C:\\Users\\dlmal\\OneDrive\\Ambiente de Trabalho\\Code")
    f = open("text.txt", "w", encoding="utf-8")
    f.write(txt.get(1.0, END))
    f.close()

def ler ():
    f = open("text.txt", "r", encoding="utf-8")
    leitura = f.read()
    txt.insert(END, leitura)
    f.close()

def limpar():
    txt.delete(1.0, END)
    


#text
txt = Text(window, width=30, height=10, wrap ="word")
txt.place(x=150,y=10)


#buttons
save_file = Button(window, text="Guardar ficheiro", command=inserir)
save_file.place(x=5, y=10)

read_file = Button(window, text="Ler Ficheiro", command=ler)
read_file.place(x=5, y=50)

delete_file = Button(window, text="Limpar", command=limpar)
delete_file.place(x=5, y=90)



window.mainloop()
