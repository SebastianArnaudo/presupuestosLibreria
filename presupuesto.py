import tkinter as tk
from tkinter import messagebox
import math


def main():
    ventana = tk.Tk()
    ventana.title("Calculo presupuesto")
    ventana.geometry("500x500")

    def extras():

        def calcular():
            cantidad=eExtra.get()
            valor=eValorExtra.get()
            cantidad=int(cantidad)
            valor=int(valor)

            presu= cantidad*valor

            messagebox.showinfo("Pres.Extra",presu)

            eExtra.delete(0,tk.END)
            eValorExtra.delete(0,tk.END)



        extra=tk.Toplevel()
        extra.title("Calcule los agregados")
        extra.geometry("350x350")

        lExtra=tk.Label(extra,text="Insumos usados:")
        lExtra.place(x=30,y=50)
        eExtra=tk.Entry(extra)
        eExtra.place(x=200, y=50)
        
        lValorExtra=tk.Label(extra,text="Valor de insumo x unidad:")
        lValorExtra.place(x=30,y=100)
        eValorExtra=tk.Entry(extra)
        eValorExtra.place(x=200, y=100)

        

        botonIngresar=tk.Button(extra,text="Ingresar valor",command=calcular)
        botonIngresar.place(x=170,y=200)

        






    
    
    def presupuesto():
        cantidadHojas=eHojas.get()
        precioHojas=ePrecioHojas.get()
        cantidadCartulina=eCartulina.get()
        precioCartulina=ePrecioCartulina.get()
        cantidadImpresion=eCantidadImpresion.get()
        precioImpresion=ePrecioImpresion.get()
        valorExtra=eValorExtra.get()
        
        cantidadHojas=int(cantidadHojas)
        precioHojas=float(precioHojas)
        cantidadCartulina=int(cantidadCartulina)
        precioCartulina=float(precioCartulina)
        cantidadImpresion=int(cantidadImpresion)
        precioImpresion=float(precioImpresion)
        valorExtra=float(valorExtra)

        presupuesto = cantidadHojas*precioHojas + cantidadCartulina*precioCartulina + cantidadImpresion*precioImpresion + valorExtra

        messagebox.showinfo("Presupuesto", presupuesto)

    lHojas = tk.Label(text= "Cantidad de hojas:",font="arial")
    lHojas.place(x=30, y= 50)
    eHojas = tk.Entry()
    eHojas.place(x=200, y= 50)

    lPrecioHojas = tk.Label(text= "Valor de hoja:",font="arial")
    lPrecioHojas.place(x=30, y=100)
    ePrecioHojas = tk.Entry()
    ePrecioHojas.place(x= 200, y= 100)

    lCartulina = tk.Label(text= "Cantidad de cartulina:",font="arial")
    lCartulina.place(x=30, y= 150)
    eCartulina = tk.Entry()
    eCartulina.place(x=200, y= 150)

    lPrecioCartulina = tk.Label(text= "Valor de cartulina:",font="arial")
    lPrecioCartulina.place(x=30, y=200)
    ePrecioCartulina = tk.Entry()
    ePrecioCartulina.place(x=200, y= 200)

    lCantidadImpresion = tk.Label(text= "Cantidad de Impresion:",font="arial")
    lCantidadImpresion.place(x=30, y= 250)
    eCantidadImpresion = tk.Entry()
    eCantidadImpresion.place(x=200, y= 250)

    lPrecioImpresion= tk.Label(text= "Valor de impresion:",font="arial")
    lPrecioImpresion.place(x=30, y=300)
    ePrecioImpresion= tk.Entry()
    ePrecioImpresion.place(x=200, y= 300)

    
    lValorExtra= tk.Label(text= "Valores Agregados:",font="arial")
    lValorExtra.place(x=30, y=350)
    eValorExtra= tk.Entry()
    eValorExtra.place(x=200, y= 350)

    botonCalculo= tk.Button(text="Calcular costo", command= presupuesto)
    botonCalculo.place(x=150, y=400)

    botonExtra= tk.Button(text="Calcular Extra",command= extras)
    botonExtra.place(x=150,y=450)

    tk.mainloop()

if __name__ == "__main__":
    main()