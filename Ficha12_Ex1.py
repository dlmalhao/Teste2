
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

def select ():
    choose_image1 = filedialog.askopenfilename(title = "Selecionar imagem", filetypes = (("jpeg files","*.jpg"),("png files","*.png")))
    list_box.insert(END,choose_image1)
    function()
    

def remove ():

    pos = list_box.curselection()
    list_box.delete(pos)
    function ()

window = Tk()
window.geometry("800x600")
window.title("AED")

def function ():
    lista.clear()
    quantity = list_box.size()
    for i in range(quantity):
        ficheiro = list_box.get(i)
        img = ImageTk.PhotoImage(file = ficheiro )
        lista.append(img)
    

def primeira ():
    global imagem_selecionada
    imagem_selecionada = 0
    canvas2.itemconfig(img_pr, image = lista[imagem_selecionada])

def ultima():
    global imagem_selecionada
    imagem_selecionada = len(lista)-1
    canvas2.itemconfig(img_pr, image = lista[imagem_selecionada])

def anterior ():
    global imagem_selecionada
    if imagem_selecionada > 0:
        imagem_selecionada -= 1
    canvas2.itemconfig(img_pr, image = lista[imagem_selecionada])

def seguinte ():
    global imagem_selecionada
    if imagem_selecionada < len(lista)-1:
        imagem_selecionada += 1
    canvas2.itemconfig(img_pr, image = lista[imagem_selecionada])

imagem_selecionada = 0    
#List box

list_box = Listbox(window, width = 30, height = 15)
list_box.place(x = 20, y = 30)


#Buttons

btn1 =Button(window, text = "Selecionar Imagem", height = 3, width = 20, command = select)
btn2 =Button(window, text = "Remover Imagem", height = 3, width = 20, command = remove)
btn3 =Button(window, text = "<<", height = 3, width = 10, command = primeira)
btn4 =Button(window, text = "<", height = 3, width = 10, command = anterior)
btn5 =Button(window, text = ">", height = 3, width = 10, command = seguinte)
btn6 =Button(window, text = ">>", height = 3, width = 10, command = ultima)



btn1.place(x = 30, y = 330)
btn2.place(x = 30, y = 400)

btn3.place(x = 300, y = 300)
btn4.place(x = 400, y = 300)
btn5.place(x = 500, y = 300)
btn6.place(x = 600, y = 300)
#Canvas

canvas1 = Canvas(window, width = 400, height = 250, relief = "sunken", bd = "3")
canvas1.place(x = 300, y = 30)

canvas2= Canvas(window, width = 350, height = 200, relief = "sunken", bd = "3")
canvas2.place(x = 325, y = 55)

img_pr = canvas2.create_image(0,0, anchor = "nw")

lista = []

window.mainloop()