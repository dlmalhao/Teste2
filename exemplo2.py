# Biblioteca Tkinter: UI
from tkinter import *
from tkinter import ttk # treeview
from tkinter import filedialog   # filedialog boxes
from PIL import ImageTk,Image  


def lista_imagens():
  lista.clear()                 # Limpa a lista de imagens a visualizar
  cont = lbox_img.size()        # nº linhas na listbox
  for indice in range (cont):   # para cada linha da listbox
     ficheiro = lbox_img.get(indice)    # Obtem conteúdo da linha da listbox
     img = ImageTk.PhotoImage(file = ficheiro)
     lista.append(img)              # criar imagem na lista de imagens


def escolhe_imagem():
  # file dialog, para selecionar ficheiro em disco
  filename = filedialog.askopenfilename(title = "Select file",filetypes = (("jpeg files","*.jpg"),("png files", "*.png"), ("all files","*.*")))
# adiciona à listBox
  lbox_img.insert("end", filename)
  lista_imagens()
 


def remove_listbox():
  #remove da lisbox o item selecionado
  lbox_img.delete(lbox_img.curselection())
  lista_imagens()


def primeira_foto():
  global current_image
  global lista

  current_image = 0
 # change image on canvas
  canvas.itemconfig(image_id, image=lista[current_image])


def ultima_foto():
  global current_image
  global lista

  current_image = len(lista)-1
 # change image on canvas
  canvas.itemconfig(image_id, image=lista[current_image])

def anterior_foto():
  global current_image
  global lista

  if current_image > 0:
     current_image-=1
 # change image on canvas
  canvas.itemconfig(image_id, image=lista[current_image])


def seguinte_foto():
  global current_image
  global lista

  current_image+=1
  if current_image > len(lista) - 1:
     current_image= len(lista)-1
 # change image on canvas
  canvas.itemconfig(image_id, image=lista[current_image])


current_image =0
lista = []   # Lista com imagems adicionadas à Listbox

window=Tk()   # invoca classe tk , cria a "main window"
window.geometry("700x450")
window.title('Gestor de Fotos')

lbox_img = Listbox(window, width = 40, height = 12, bd = "3", relief = "sunken")
lbox_img.place(x=10, y=30)


#----- Button 1 -------
btn_adicionar = Button(window, text = "Selecionar imagem", width=34, height = 3, command = escolhe_imagem)
btn_adicionar.place(x=10, y=250)

#----- Button 2 -------
btn_eliminar = Button(window, text = "Remover imagem", width = 34, height = 3, command = remove_listbox)
btn_eliminar.place(x=10, y=320)


# Panel -----------------------------------------
panel1 = PanedWindow(window, width = 320, height = 190, bd = "3", relief = "sunken")
panel1.place(x=300, y=30)

# container Canvas, usado para aplicações de desenho: imagens e formas geométricas
canvas = Canvas(panel1, width = 280, height = 150, bd = 4, relief = "sunken")
canvas.place(x=10, y=10)

img = ImageTk.PhotoImage(file = "img1.jpg")
# set first image on canvas
image_id = canvas.create_image(0, 0, anchor='nw', image=img)

#----- Button imagem PRIMEIRA -------
btn1 = Button(window, text = "<<", width = 10, command = primeira_foto)
btn1.place(x=300, y=250)

#----- Button imagem ANTERIOR -------
btn2 = Button(window, text = "<", width = 10, command = anterior_foto)
btn2.place(x=380, y=250)

#----- Button imagem SEGUINTE -------
btn2 = Button(window, text = ">", width = 10, command = seguinte_foto)
btn2.place(x=460, y=250)

#----- Button imagem ULTIMA -------
btn2 = Button(window, text = ">>", width = 10, command = ultima_foto)
btn2.place(x=540, y=250)

window.mainloop()   # event listening loop by calling the mainloop()