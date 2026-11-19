import tkinter as tk
from tkinter import ttk


class app(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Editor de txt")
        self.geometry("900x600")
        self.resizable(False, False)
        style = ttk.Style(self)
        style.theme_use("clam")
        self.configure(bg="#DCE6F2")
        
        container = ttk.Frame(self)
        container.pack(fill = "both", expand = True)
        
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        
        for F in (telaInicial,):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            
        self.mostrar_tela(telaInicial)
        
    def mostrar_tela(self, tela):
        frame = self.frames[tela]
        frame.tkraise()
        
class telaInicial(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        self.columnconfigure(0, weight = 0)
        self.columnconfigure(1, weight = 1)
        self.columnconfigure(2, weight = 0)

        self.rowconfigure(0, weight = 1)
        self.rowconfigure(1, weight = 0)
        
        rodape = ttk.Frame(self, padding = 10, relief = "raised", bg = "#6A89A7")
        rodape.grid(row = 1, column = 0, columnspan = 3, sticky = "nsew")
        

if __name__ == "__main__":
    App = app()
    App.mainloop()