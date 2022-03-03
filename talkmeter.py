from tkinter import messagebox
from tkinter import *

root = Tk()

root.title('Coloque aqui suas maravilhosas e importantes palavras')

prompt = Label(root, text='Você dizia...?', padx=10, pady=10)
prompt.pack()

entry = Entry(root, width=100, borderwidth=10)
entry.pack()

def btClick():
    input_words = entry.get()

    size = len(input_words.split())

    if size > 1:
        messagebox.showinfo('Cano de PVC informa:','Esse ganha pelo cansaço!!!Parabéns!!')
    else:    
        messagebox.showinfo('Cano de PVC informa:','Falou pouco e bonito!')

okButton = Button(root, text='Eu disse...', padx=20, pady=20, command=btClick, background='gray')

okButton.pack()

root.mainloop()

