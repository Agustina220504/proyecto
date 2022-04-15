from tkinter import *
import tkinter
from translate import Translator

ventana=Tk()
ventana.geometry("530x170")
ventana.title("TRADUCTOR")
ventana.config(relief="groove",bd="20",bg="#a1bda0")



len1=StringVar(ventana)
len2=StringVar(ventana)
choices={'English','Portuguese','Spanish'}

len1.set('Spanish')
len2.set('English')

def translate():
    translator=Translator(from_lang=len1.get(),to_lang=len2.get())
    translation =translator.translate(var.get())
    var1.set(translation)

len1menu=OptionMenu(ventana,len1,*choices)
Label(ventana,text="Seleccione el lenguaje",activeforeground="#F50743",bg='#bde3bc').grid(row=0,column=1)
len1menu.grid(row=2,column=1)

len2menu=OptionMenu(ventana, len2, *choices)
Label(ventana,text="Seleccione el lenguaje",bg='#bde3bc').grid(row=0,column=5)
len2menu.grid(row=2,column=5)

Label(ventana,text="Ingrese el texto",bg='#7cb57b',).grid(row=6,column=0)
var=StringVar()
textbox=Entry(ventana,textvariable=var).grid(row=6,column=1)

Label(ventana,text="Traducción",bg ='#7cb57b').grid(row=6,column=6)
var1 = StringVar()
textbox=Entry(ventana, textvariable=var1, ).grid(row=6,column=5)

b=Button(ventana,text='Traducir',bd=15,command=translate,bg='#5db05b').grid(row=8,column=3,columnspan=2)

ventana.mainloop()
