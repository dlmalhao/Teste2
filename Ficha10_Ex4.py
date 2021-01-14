from tkinter import *

def adicionar ():
    tarefa = str(entry1.get())
    list_box.insert(END,tarefa)

def remove ():
    pos = list_box.curselection()
    list_box.delete(pos)

def clear ():
    list_box.delete(0,END)

def upload ():
    with open("tarefas.txt", "r") as f:
        content = f.readlines()   
        for i in content:
            list_box.insert(END,i)


def download():
    content = list(list_box.get(0,END))
    with open("tarefas.txt", "w") as f:
        for i in content:
            f.write(i + "\n")

def ordenar ():
    lista2 = list(list_box.get(0,END))
    lista_ordenada = sorted(lista2, key = str.casefold)       #############################################
    list_box.delete(0,END)
    for i in lista_ordenada:
        list_box.insert(END,i)
    


window = Tk()
window.geometry("800x600")
window.title("AED")

lista = []

#List Box

frame1 = LabelFrame(window, width = 250, height = 400, relief = "sunken", bd = "3")
frame1.place(x = 20, y = 70)

list_box = Listbox(frame1, width = 30, height = 21)
list_box.place(x = 20, y = 30)

#Tarefa

frame2 = LabelFrame(window, width = 300, height = 150, relief = "sunken", bd = "3")
frame2.place(x = 350, y = 70)

entry1 = Entry(frame2, width = 40)
entry1.place (x = 25, y = 60)

lbl1 = Label(frame2, text = "Tarefa", fg = "blue")
lbl1.place(x = 130, y = 30)

#buttons

btn1 =Button(window, text = "Adicionar", command = adicionar)
btn2 =Button(window, text = "Remove", command = remove)
btn3 =Button(window, text = "Clear", command = clear)
btn4 =Button(window, text = "Upload", command = upload)
btn5 =Button(window, text = "Download", command = download)
btn6 =Button(window, text = "Ordenar", command = ordenar)

btn1.place(x = 350, y =230)
btn2.place(x = 420, y =230)
btn3.place(x = 480, y = 230)
btn4.place(x = 350, y = 260)
btn5.place(x = 410, y = 260)
btn6.place(x = 480, y = 260)





window.mainloop()