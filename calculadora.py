# Sierra Ariza, Dorian Gabriel 10A
#Calculadora usando librerías
from tkinter import*
from math import*

def btnClik(num):
    global operador
    operador=operador + str(num)
    input_text.set(operador)
def resultado():
    global operador
    try:
        op=str(eval(operador))
        input_text.set(op)
    except:
        input_text.set("ERROR")
    operador=""
def clear():
    global operador
    operador=""
    input_text.set("0")
      
ventana = Tk()
ventana.title("Calculadora")
ventana.geometry("400x600")
ventana.iconbitmap("calculadora.ico")
ventana.configure(background="#0a0e27")
color_boton = "#00d9ff"
ancho_boton = 9
alto_boton = 3
ancho_boton_igual = 36
input_text = StringVar()
operador = ""
Salida = Entry(
    ventana,
    font=("arial", 20, "bold"),
    width=20,
    textvariable=input_text,
    bd=10,
    insertwidth=200,
    background="#162541",
    justify="center"
)
Salida.place(x=20, y=20)
Button(ventana,text="C",background=color_boton,width=ancho_boton,height=alto_boton,command=clear).place(x=16,y=100)
Button(ventana,text="%",background=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("%")).place(x=103,y=100)
Button(ventana,text="(",background=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("(")).place(x=190,y=100)
Button(ventana,text=")",background=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(")")).place(x=277,y=100)
Button(ventana,text="7",background=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(7)).place(x=16,y=180)
Button(ventana,text="8",background=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(8)).place(x=103,y=180)
Button(ventana,text="9",background=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(9)).place(x=190,y=180)
Button(ventana,text="/",background=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("/")).place(x=277,y=180)
Button(ventana,text="4",background=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(4)).place(x=16,y=260)
Button(ventana,text="5",background=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(5)).place(x=103,y=260)
Button(ventana,text="6",background=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(6)).place(x=190,y=260)
Button(ventana,text="*",background=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("*")).place(x=277,y=260)
Button(ventana,text="1",background=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(1)).place(x=16,y=340)
Button(ventana,text="2",background=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(2)).place(x=103,y=340)
Button(ventana,text="3",background=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(3)).place(x=190,y=340)
Button(ventana,text="-",background=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("-")).place(x=277,y=340)
Button(ventana,text="0",background=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(0)).place(x=16,y=420)
Button(ventana,text=".",background=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(".")).place(x=103,y=420)
Button(ventana,text="EXP",background=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("**")).place(x=190,y=420)
Button(ventana,text="+",background=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("+")).place(x=277,y=420)
Button(ventana,text="=",background=color_boton,width=ancho_boton_igual,height=alto_boton,command=resultado).place(x=16,y=500)

clear()
ventana.mainloop()
