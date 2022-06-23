from tkinter import *
from tkinter import ttk
from tkinter import Label
import tkinter as tk

class Aplicacion():
     def __init__(ventana):
        
          ventana.raiz = Tk()
          ventana.raiz.geometry('300x300')
          ventana.raiz.title("Calculadora")
          
          ventana.numero1=StringVar()
          ventana.numero2=StringVar()
          ventana.numero3=StringVar()
          
          ventana.titulo=Label(ventana.raiz,text="Ingrese numero 1").place(x=90,y=0)
          ventana.Entrada1=Entry(ventana.raiz,textvariable=ventana.numero1).place(x=90,y=25)
          ventana.titulo=Label(ventana.raiz,text="Ingrese numero 2").place(x=90,y=50)
          ventana.Entrada1=Entry(ventana.raiz,textvariable=ventana.numero2).place(x=90,y=80)
          
          boton1=Button(ventana.raiz,text="SUMAR",command=ventana.suma).place(x=20,y=140)
          boton1=Button(ventana.raiz,text="RESTAR",command=ventana.resta).place(x=80,y=140)
          boton1=Button(ventana.raiz,text="MULTIPLICAR",command=ventana.multiplicacion).place(x=150,y=140)
          boton1=Button(ventana.raiz,text="DIVIDIR",command=ventana.division).place(x=237,y=140)
          
          s=tk.Label(ventana.raiz,font=("arial",10,"bold"),borderwidth=10,width=30,background="white",textvariable=ventana.numero3).place(x=20,y=180)
          boton1=Button(ventana.raiz,text="Salir",command=ventana.raiz.destroy).place(x=130,y=240)
          
          ventana.raiz.mainloop()
          
     def suma(ventana):
         ventana.suma=int(ventana.numero1.get())+int(ventana.numero2.get())
         return ventana.numero3.set(ventana.suma)
    
     def resta(ventana):
         ventana.resta=int(ventana.numero1.get())-int(ventana.numero2.get())
         return ventana.numero3.set(ventana.resta)
        
     def multiplicacion(ventana):
         ventana.multiplicacion=int(ventana.numero1.get())*int(ventana.numero2.get())
         return ventana.numero3.set(ventana.multiplicacion)

     def division(ventana):
         ventana.division=int(ventana.numero1.get())/int(ventana.numero2.get())
         return ventana.numero3.set(ventana.division)
          

def main():
    mi_app = Aplicacion()
    return(0)

if __name__ == '__main__':
    main()
