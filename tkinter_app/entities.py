from tkinter import *
from tkinter import ttk

class mainApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.movimientos = Movimientos(self)
        self.movimientos.pack(side=TOP)
        self.transaccion = Transaccion(self)
        self.transaccion.pack(side=TOP)


class Movimientos(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)

        ttk.Label(self, text="Aquí ira la lista de movimientos").pack()


class Transaccion(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)

        ttk.Label(self, text="Aquí ira el formulario de compra").pack()
