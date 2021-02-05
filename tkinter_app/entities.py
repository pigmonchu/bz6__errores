from tkinter import *
from tkinter import ttk

from configparser import ConfigParser

c = ConfigParser()
c.read('tkinter_app/config.ini')
config = c['DEFAULT']


class mainApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        s = ttk.Style()
        s.theme_use('alt')
        self.movimientos = Movimientos(self)
        self.movimientos.pack(side=TOP)
        self.transaccion = Transaccion(self)
        self.transaccion.pack(side=TOP)
        print(config['API_KEY'])


class Header(ttk.Frame):
    titles = [("Fecha", 12), ("Hora", 10), ("From", 5), 
              ("Q", 20), ("To", 5), ("Q", 20), 
              ("P.U.", 20), ]
    
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.w = 0
        self.h = 0
        for title in self.titles:
            lbl = Label(self, text=title[0], font="Helvetica 16 bold", bd=1, relief=GROOVE, width=title[1])
            lbl.pack(side=LEFT)
            self.w += lbl.winfo_reqwidth()
            self.h = max(self.h, lbl.winfo_reqheight())


class AddButton(Frame):
    w=40
    h=40
    def __init__(self, parent, text, command):

        Frame.__init__(self, parent, width=self.w, height=self.h)
        self.pack_propagate(0)
        self.text = text
        self.command = command

        ttk.Button(self, text=self.text, command=self.command).pack(fill=BOTH, expand=True)





class Movimientos(Frame):
    padding = 8
    def __init__(self, parent):
        Frame.__init__(self, parent, padx=self.padding, pady=self.padding)
        self.grid_propagate(0)

        self.header = Header(self)
        self.header.pack(side=TOP)
        self.header.grid(row=0, column=0)
        self.addBtn = AddButton(self, text = "+", command=lambda: print('click'))
        self.addBtn.grid(row=0, column=1)

        w = self.header.w + self.addBtn.w
        h = max(self.header.h, self.addBtn.h)

        self.config(width= w + self.padding*2, height= h + self.padding*2)

class Transaccion(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)

        ttk.Label(self, text="Aquí ira el formulario de compra").pack()
