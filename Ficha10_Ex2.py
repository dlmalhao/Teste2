
from tkinter import *

def function ():
    result = 0
    h = int(entry1.get())
    if selected.get() == "Masculino":
        result = (h-100)-(h-150)/4
    elif selected.get() == "Feminino":
        result = (h-100)-(h-150)/2
    entry2.delete(0,END)
    entry2.insert(0,str(result))




window = Tk()
window.geometry("800x600")
window.title("AED")

#Altura em cm

lbl1 = Label(window, text = "Altura em cm", fg = "blue")
lbl1.place(x = 20, y = 20)

entry1 = Entry(window, width = 20)
entry1.place(x = 100, y = 20)

#Genero

selected = StringVar()
selected.set("Masculino")

frame1 = LabelFrame(window, text = "Género", width = 300, height = 150, relief = "sunken", bd = "3", fg = "blue")
frame1.place(x = 20, y = 70)

rad1 = Radiobutton(frame1, text = "Masculino", variable = selected, value = "Masculino")
rad2 = Radiobutton(frame1, text = "Feminino", variable = selected, value = "Feminino")

rad1.place(x = 20, y = 30)
rad2.place(x = 20, y = 70)

#Button calcular peso ideal

btn1 = Button(window, width = 10, height = 6, text = "Calcular \n peso ideal", command = function )
btn1.place (x = 350, y = 100)

# Peso ideal em kg

frame2 = LabelFrame(window, width = 150, height = 150, relief = "sunken", bd = "3", fg = "blue")
frame2.place(x = 475, y = 75)

lbl2 = Label(frame2, text = "Peso ideal em kg", fg = "blue" )
lbl2.place(x = 10, y = 20)

entry2 = Entry(frame2, width = 20)
entry2.place(x = 10, y = 45)

window.mainloop()