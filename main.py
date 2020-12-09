from tkinter import *
import app

def main():
    root = Tk()
    root.title('Agenda de contacto por maria dolores')
    root.configure(bg = "green")
    root.geometry("+350+80")
    root.resizable(0,0)
    app.App(root) 
    root.mainloop()

if __name__ == "__main__":
    main()