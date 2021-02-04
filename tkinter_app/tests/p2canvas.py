from tkinter import *
from tkinter import ttk

class Field(Frame):
    def __init__(self, parent, text, ix):
        Frame.__init__(self, parent, bd=1, relief=GROOVE)
        self.pack_propagate(0)
        self.label = Label(self, text=text)
        self.value = Label(self, text= ix)
        self.label.config(font="Arial 16 bold")
        self.label.pack(side=LEFT)
        self.value.pack(side=LEFT, fill=X)
        
class Scroll_List(Frame):
    vbWidth = 22
    def __init__(self, parent, **kwargs):
        self.width = kwargs.get('width', 0)
        self.height = kwargs.get('height', 0)
        # El frame que contendrá el canvas que a su vez tendrá un Frame
        self.marco = Frame(parent, width=self.width, height=self.height)
        # La scrollbar, se crea dentro del frame marco
        self.vbar = Scrollbar(self.marco, orient=VERTICAL)
        self.vbar.pack(side=RIGHT, fill=Y)

        # Crear el canvas en el que irá el frame mayor que él
        self.canvas = Canvas(self.marco, width=self.width - self.vbWidth, bg="#ffffff")
        self.canvas.pack(side=LEFT, fill=BOTH)

        # Este es el frame al que le añadimos los widgets que queramos y  que quedarán con scroll
        super().__init__(self.canvas, width=self.width-self.vbWidth, bg="#FFDDDD")
        #Asociar el frame al canvas y a la scrollbar
        self.canvas.create_window(0, 0, anchor=NW, window=self)
        self.vbar.config(command=self.canvas.yview)
        self.canvas.config(yscrollcommand=self.vbar.set, scrollregion=self.canvas.bbox('all'))

        #importante. Debe actualizarse cada vez que se modifica el contenido del frame. Método update

    def position(self, geometry, **kwargs):
        '''
        La posición del control debe ser la de self.marco. Así que se aplica a él, 
        ya que si se hace directamente se hace sobre el contenido y no sobre el continente
        '''
        func = getattr(self.marco, geometry)
        func(**kwargs)        

    def add(self, control):
        h = control.winfo_reqheight()
        print(h, '-', self.winfo_reqheight() + h)
        control.pack(side=TOP, fill=X)
        self.config(height=self.winfo_reqheight() + h )

    def update(self):
        '''
        Actualiza el canvas tras incluir algo en el control
        '''
        h = self.winfo_height()
        print(h)
        self.pack_propagate(0)
        self.config(width=self.width - self.vbWidth, height=h)
        self.canvas.config(scrollregion=self.canvas.bbox('all'))
        self.update_idletasks()




# Contenedor principal que será scrollable
class ScrollableFrame(Frame):
    rowHeight=22
    vbWidth = 22
    def __init__(self, parent, **kwargs):
        self.width = kwargs.get('width')
        self.height = kwargs.get('height')

        Frame.__init__(self, parent, width=self.width, height=self.height, bd=2, relief=GROOVE)
        
        # Scrollbar vertical
        self.vbar = Scrollbar(self, orient=VERTICAL)
        self.vbar.pack(side=RIGHT, fill=Y)
        # Canvas en que se pintarán los controle (lineas de movimiento)
        self.canvas = Canvas(self, width=self.width - self.vbWidth, height=self.height, bg="#ffffff", yscrollcommand=self.vbar.set)
        self.canvas.pack(side=LEFT, fill=BOTH)
        # Generamos una ventana en el canvas y le asociamos el frame en el que montaremos las líneas
        self.__marco = Frame(self.canvas, width=self.width-22, bg="#FFDDDD")
        self.__marco.pack_propagate(1)
        window = self.canvas.create_window(0,0, anchor=NW, window=self.__marco)
        # Enganchamos todo
        self.vbar.config(command=self.canvas.yview)
        self.canvas.config(yscrollcommand=self.vbar.set)
    
    def update(self, control):
        control.config(width=self.width-22, height=self.rowHeight)
        control.pack(side=TOP, fill=X)
        self.marco.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox('all'))

    @property
    def marco(self):
        return self.__marco

if __name__ == '__main__':
    root = Tk()
    sc = Scroll_List(root, width=400, height=300)
    sc.position('pack')
    for i in range(1, 101):
        sc.add(Label(sc, text=i))
    sc.update()

    root.mainloop()
