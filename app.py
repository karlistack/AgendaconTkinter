from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox as CajadeMensajes
import ordenadalo
import csv

# -------------------------- GLOBAL FUNCTIONS ------------------------------------------

# ----------- MESAGE BOX ---------------------------------------
def nohay(var):
    var_s = str(var)
    CajadeMensajes.showinfo("no se encontro", var_s + ' ' + "no hay")

def escribelnombre():
    CajadeMensajes.showinfo("No hay", "tienes que escribir un contacto")

def escribe_contacto():
    CajadeMensajes.showinfo("Escribe un contacto", "usa añadir contacto para añadir la infromacion")

def delete_mesageBox(nombre):
    var_nombre = str(nombre)
    if var_nombre == '':
        escribelnombre()
    else:
        buscando = CajadeMensajes.askquestion("Ojo","¿Quires borrar este contacto?\n" + var_nombre)
        if buscando == "Si":
            return True
        else:
            return False

def modifica_lacaja(contact):
    var_nombre = str(contact[0])
    var_telefono = str(contact[1])
    var_email = str(contact[2])
    buscando = CajadeMensajes.askquestion("Alerta","¿quieres guardar los cambios que ha sufrido este contacto?\n" + " nombre:" + var_nombre + "\n telefono:" + var_telefono + "\n Email:" + var_email)
    if buscando == "Si":
        return True
    else:
        return False

class App():
    def __init__(self, root):
        self.window = root

        menubar = Menu(self.window)
        self.window.config(menu = menubar)

        filemenu = Menu(menubar, tearoff = 0, bg = "#FFBB20")
        filemenu.add_command(label = "Show all contactos", command = lambda: muestra_los_contactos(), font = ("Helveltica", "9", "normal"))
        filemenu.add_command(label = "User manual", font = ("Helveltica", "9", "normal"))
        filemenu.add_separator()
        filemenu.add_command(label = "Close", command = self.window.quit, font = ("Helveltica", "9", "normal"))

        menubar.add_cascade(label = "Menu", menu = filemenu)

        # ---------------- FRAMES DECLARATION -----------------
        inbox_frame = LabelFrame(self.window, bg = "#53CDB8")
        inbox_frame.grid(row = 0, column = 0)
        
        button_frame = LabelFrame(self.window, bg = "#53CDB8")
        button_frame.grid(row = 2, column = 0)

        three_frame = LabelFrame(self.window, bg = "#53CDB8")
        three_frame.grid(row = 4, column = 0)
        
        three_button_frame = LabelFrame(self.window, bg = "#53CDB8")
        three_button_frame.grid(row = 5, column = 0)

        # --------------- INBOX WIDGETS ZONE ------------------
        Label(inbox_frame, text = 'nombre', bg = "#53CDB8", font = ("Comic Sans MS", "11", "normal")).grid(row = 0, column = 0)
        inbox_nombre = Entry(inbox_frame, font = ("Comic Sans MS", "11", "normal"), width = 28)
        inbox_nombre.grid(row = 1, column = 0)
        inbox_nombre.focus()

        Label(inbox_frame, text = 'telefono', bg = "#53CDB8", font = ("Comic Sans MS", "11", "normal")).grid(row = 0, column = 1)
        inbox_telefono = Entry(inbox_frame, font = ("Comic Sans MS", "11", "normal"), width = 20)
        inbox_telefono.grid(row = 1, column = 1)

        Label(inbox_frame, text = 'Email', bg = "#53CDB8", font = ("Comic Sans MS", "11", "normal")).grid(row = 0, column = 2)
        inbox_Email = Entry(inbox_frame, font = ("Comic Sans MS", "11", "normal"), width = 30)
        inbox_Email.grid(row = 1, column = 2)

        # --------------- BUTTON WIDGETS ZONE -----------------
        Add_contact_button = Button(button_frame, command = lambda: añadir(), text = 'Add Contact', width = 20)
        Add_contact_button.configure(bg = "#FFBB20", cursor = 'hand2', font = ("Comic Sans MS", "10", "normal"))
        Add_contact_button.grid(row = 0, column = 0, padx = 2, pady = 3, sticky = W + E)

        buscando_button = Button(button_frame, command = lambda: buscando(), text = 'buscando contact', width = 20)
        buscando_button.configure(bg = "#FFBB20", cursor = 'hand2', font = ("Comic Sans MS", "10", "normal"))
        buscando_button.grid(row = 0, column = 1, padx = 2, pady = 3, sticky = W + E)

        delete_button = Button(button_frame, command = lambda: borra(), text = 'Delete contact', width = 20)
        delete_button.configure(bg = "#F26262", cursor = 'hand2', font = ("Comic Sans MS", "10", "normal"))
        delete_button.grid(row = 1, column = 0, padx = 2, pady = 3, sticky = W + E)

        modify_button = Button(button_frame, command = lambda: modfica(), text = 'Modify contact')
        modify_button.configure(bg = "#FFBB20", cursor = 'hand2', font = ("Comic Sans MS", "10", "normal"))
        modify_button.grid(row = 1, column = 1, padx = 2, pady = 3, sticky = W + E)

        show_contacts_button = Button(button_frame, command = lambda: muestra_los_contactos(), text = 'Show all Contacts', width = 20)
        show_contacts_button.configure(bg = "#FFBB20", cursor = 'hand2', font = ("Comic Sans MS", "10", "normal"))
        show_contacts_button.grid(row = 0, column = 2, padx = 2, pady = 3, sticky = W + E)
        
        save_changes_button = Button(button_frame, command = lambda: limpialotood(), text = 'Clean window', width = 20)
        save_changes_button.configure(bg = "#FFBB20", cursor = 'hand2', font = ("Comic Sans MS", "10", "normal"))
        save_changes_button.grid(row = 1, column = 2, padx = 2, pady = 3, sticky = W + E)

        # -------------- COMBOBOX WIDGETS ZONE ----------------
        Label(button_frame, text = 'buscando/Modify Selection', bg = "#53CDB8", font = ("Comic Sans MS", "10", "normal")).grid(row = 0, column = 3, columnspan = 3)
        
        combo = ttk.Combobox(button_frame, state = 'readonly', width = 17, justify = 'center', font = ("Comic Sans MS", "10", "normal"))
        combo["values"] = ['nombre', 'telefono', 'Email']
        combo.grid(row = 1, column = 3, padx = 15)
        combo.current(0)

        # --------------- TREE DIRECTORY ZONE -----------------
        # Table for database
        self.tree = ttk.Treeview(three_frame, height = 20, columns = ("one", "two"))
        self.tree.grid(padx = 5, pady = 5, row = 0, column = 0, columnspan = 1)
        self.tree.heading("#0", text = 'nombre', anchor = CENTER)
        self.tree.heading("one", text = 'telefono', anchor = CENTER)
        self.tree.heading("two", text = 'Email', anchor = CENTER)

        #Scroll
        scrollVert = Scrollbar(three_frame, command = self.tree.yview)
        self.tree.configure(yscrollcommand = scrollVert.set)
        scrollVert.grid(row = 0, column = 1, sticky = "nsew")

        scroll_x = Scrollbar(three_frame, command = self.tree.xview, orient = HORIZONTAL)
        self.tree.configure(xscrollcommand = scroll_x.set)
        scroll_x.grid(row = 2, column = 0, columnspan = 1, sticky = "nsew")

# -------------------------- COMMAND FUNCTIONS DECLARATION -----------------------------

        # --------------- AUXILIAR FUNCTIONS ------------------
        def limpia_lainbox():
            inbox_nombre.delete(0, 'end')
            inbox_telefono.delete(0, 'end')
            inbox_Email.delete(0, 'end')

        def _clean_treeview():
            tree_list = self.tree.get_children()
            for item in tree_list:
                self.tree.delete(item)

        def _miraelarchivo_():
            contactos = ordenadalo.ordenalphabetico()
            for i, row in enumerate(contactos):
                nombre = str(row[0])
                telefono = str(row[1])
                email = str(row[2])
                self.tree.insert("", 0, text = nombre, values = (telefono, email))

        def guarda(nombre, telefono, email):
            s_nombre = nombre
            s_telefono = telefono
            s_email = email
            with open('contacts_list.csv', 'a') as f:
                writer = csv.writer(f, lineterminator ='\r', delimiter=',')
                writer.writerow( (s_nombre, s_telefono, s_email) )

        def _buscando(var_inbox, posicion):
            lalista = []
            s_var_inbox = str(var_inbox)
            var_posicion = int(posicion)
            with open('contacts_list.csv', 'r') as f:
                reader = csv.reader(f)
                for i, row in enumerate(reader):
                    if s_var_inbox == row[var_posicion]:
                        lalista = [row[0], row[1], row[2]]
                        break
                    else:
                        continue
            return lalista

        def _check(answer, var_buscando):
            list_answer = answer
            var_buscando = var_buscando
            if list_answer == []:
                nohay(var_buscando)
            else:
                nombre = str(list_answer[0])
                telefono = str(list_answer[1])
                email = str(list_answer[2])
                self.tree.insert("", 0, text = "------------------------------", values = ("------------------------------", "------------------------------"))
                self.tree.insert("", 0, text = nombre, values = (telefono, email))
                self.tree.insert("", 0, text = "buscando result of nombre", values = ("buscando result of telefono", "buscando result of email"))
                self.tree.insert("", 0, text = "------------------------------", values = ("------------------------------", "------------------------------"))

        def _check_1(answer,var_buscando):
            val_modify = answer
            var = var_buscando
            if val_modify == []:
                nohay(var)
            else:
                elpantallon(self.window, val_modify)

        # ----------------- BUTTON FUNCTIONS ------------------
        def añadir():
            nombre = inbox_nombre.get()
            telefono = inbox_telefono.get()
            email = inbox_Email.get()
            validador = [nombre, telefono, email]
            if validador == ['', '', '']:
                escribe_contacto()
            else:
                if nombre == '':
                    nombre = '<Default>'
                if telefono == '':
                    telefono = '<Default>'
                if email == '':
                    email = '<Default>'
                guarda(nombre, telefono, email)
                self.tree.insert("", 0, text = "------------------------------", values = ("------------------------------", "------------------------------"))
                self.tree.insert("", 0, text = str(nombre), values = (str(telefono), str(email)))
                self.tree.insert("", 0, text = "New nombre added", values = ("New telefono added", "New email added"))
                self.tree.insert("", 0, text = "------------------------------", values = ("------------------------------", "------------------------------"))
            validador = []
            limpia_lainbox()

        def buscando():
            lavuelta = []
            var_buscando = str(combo.get())
            if var_buscando == 'nombre':
                var_inbox = inbox_nombre.get()
                possition = 0
                lavuelta = _buscando(var_inbox, possition)
                _check(lavuelta, var_buscando)
            elif var_buscando == 'telefono':
                var_inbox = inbox_telefono.get()
                possition = 1
                lavuelta = _buscando(var_inbox, possition)
                _check(lavuelta, var_buscando)
            else:
                var_inbox = inbox_Email.get()
                possition = 2
                lavuelta = _buscando(var_inbox, possition)
                _check(lavuelta, var_buscando)
            limpia_lainbox()

        def modfica():
            answer = []
            var_buscando = str(combo.get())
            if var_buscando == 'nombre':
                var_inbox = inbox_nombre.get()
                posicion = 0
                answer = _buscando(var_inbox, posicion)
                _check_1(answer, var_buscando)
            elif var_buscando == 'telefono':
                var_inbox = inbox_telefono.get()
                posicion = 1
                answer = _buscando(var_inbox, posicion)
                _check_1(answer, var_buscando)
            else:
                var_inbox = inbox_Email.get()
                posicion = 2
                answer = _buscando(var_inbox, posicion)
                _check_1(answer, var_buscando)
            limpia_lainbox()
            
        def muestra_los_contactos():
            self.tree.insert("", 0, text = "------------------------------", values = ("------------------------------", "------------------------------"))
            _miraelarchivo_()
            self.tree.insert("", 0, text = "------------------------------", values = ("------------------------------", "------------------------------"))

        def borra():
            nombre = str(inbox_nombre.get())
            confirmador = delete_mesageBox(nombre)
            if confirmador == True:
                with open('contacts_list.csv', 'r') as f:
                    reader = list(csv.reader(f))
                with open('contacts_list.csv', 'w') as f:
                    writer = csv.writer(f, lineterminator ='\r', delimiter=',')
                    for i, row in enumerate(reader):
                        if nombre != row[0]:
                            writer.writerow(row)
            limpialotood()
            muestra_los_contactos()

        def limpialotood():
            limpia_lainbox()
            _clean_treeview()

# ------------------------- TOP LEVE WINDOW ----------------------------------------------

class elpantallon():
    def __init__(self, root, val_modify):
        self.root_window = root
        self.val_modify = val_modify
        self.nombre = str(self.val_modify[0])
        self.telefono = str(self.val_modify[1])
        self.email = str(self.val_modify[2])

        haceventanas = Toplevel(self.root_window)
        haceventanas.title("modifica el contacto")
        haceventanas.configure(bg = "#53CDB8")
        haceventanas.geometry("+400+100")
        haceventanas.resizable(0,0)

        # ---------------- FRAMES DECLARATION -----------------
        texto = LabelFrame(haceventanas, bg = "#53CDB8")
        texto.grid(row = 0, column = 0)

        botonc = LabelFrame(haceventanas, bg = "#53CDB8")
        botonc.grid(row = 2, column = 0)

        # --------------- LABELS WIDGETS ZONE -----------------
        Label(texto, text = "Do you want to modify this contact?", bg = "#53CDB8", font = ("Comic Sans MS", "11", "normal")).grid(row = 0, column = 0, columnspan = 3)
        Label(texto, text = self.nombre, bg = "#53CDB8", font = ("Comic Sans MS", "11", "bold")).grid(row = 1, column = 0)
        Label(texto, text = self.telefono, bg = "#53CDB8", font = ("Comic Sans MS", "11", "bold")).grid(row = 1, column = 1)
        Label(texto, text = self.email, bg = "#53CDB8", font = ("Comic Sans MS", "11", "bold")).grid(row = 1, column = 2)
        
        # --------------- INBOX WIDGETS ZONE ------------------
        Label(texto, text = 'Escribe un nuevo nombre', bg = "#53CDB8", font = ("Comic Sans MS", "11", "normal")).grid(row = 2, column = 0)
        n_inbox_nombre = Entry(texto, font = ("Comic Sans MS", "11", "normal"), width = 28)
        n_inbox_nombre.grid(row = 3, column = 0)
        n_inbox_nombre.focus()

        Label(texto, text = 'Escribe un nuevo telefono', bg = "#53CDB8", font = ("Comic Sans MS", "11", "normal")).grid(row = 2, column = 1)
        n_inbox_telefono = Entry(texto, font = ("Comic Sans MS", "11", "normal"), width = 20)
        n_inbox_telefono.grid(row = 3, column = 1)

        Label(texto, text = 'Escribe un nuevo Email', bg = "#53CDB8", font = ("Comic Sans MS", "11", "normal")).grid(row = 2, column = 2)
        n_inbox_Email = Entry(texto, font = ("Comic Sans MS", "11", "normal"), width = 30)
        n_inbox_Email.grid(row = 3, column = 2)

        # --------------- BUTTON WIDGETS ZONE -----------------
        Si_button = Button(botonc, command = lambda: Si(), text = 'Si', width = 20)
        Si_button.configure(bg = "#F26262", cursor = 'hand2', font = ("Comic Sans MS", "10", "normal"))
        Si_button.grid(row = 1, column = 0, padx = 2, pady = 3, sticky = W + E)

        no_button = Button(botonc, command = haceventanas.destroy, text = 'No', width = 20, bg = "yellow", cursor = 'hand2')
        no_button.configure(bg = "#FFBB20", cursor = 'hand2', font = ("Comic Sans MS", "10", "normal"))
        no_button.grid(row = 1, column = 1, padx = 2, pady = 3, sticky = W + E)

        cancelamos_button = Button(botonc, command = haceventanas.destroy, text = 'Cancel', width = 20, bg = "green", cursor = 'hand2')
        cancelamos_button.configure(bg = "#FFBB20", cursor = 'hand2', font = ("Comic Sans MS", "10", "normal"))
        cancelamos_button.grid(row = 1, column = 2, padx = 2, pady = 3, sticky = W + E)

        # ----------------- BUTTON FUNCTIONS ------------------
        def Si():
            contacto = self.val_modify
            new_nombre = n_inbox_nombre.get()
            new_telefono = n_inbox_telefono.get()
            new_email = n_inbox_Email.get()
            a = modifica_lacaja(contacto)
            if a == True:
                elanterior(contacto[0])
                añadeunonuevo(new_nombre, new_telefono, new_email)
            haceventanas.destroy()

        def añadeunonuevo(nombre, telefono, email):
            s_nombre = nombre
            s_telefono = telefono
            s_email = email
            with open('contacts_list.csv', 'a') as f:
                writer = csv.writer(f, lineterminator ='\r', delimiter=',')
                writer.writerow( (s_nombre, s_telefono, s_email) )

        def elanterior(aNombre):
            nombre = aNombre
            with open('contacts_list.csv', 'r') as f:
                reader = list(csv.reader(f))
            with open('contacts_list.csv', 'w') as f:
                writer = csv.writer(f, lineterminator ='\r', delimiter=',')
                for i, row in enumerate(reader):
                    if nombre != row[0]:
                        writer.writerow(row)