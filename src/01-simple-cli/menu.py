from notebook import Notebook
import sys


class Menu:
    def __init__(self):
        self.notebook = Notebook()


 

    def printMenu(self):
        print("""
            Bienvenido a la aplicación de notas
            Menú:
            1. Ver todas las notas
            2. Agregar Nota
            3. Modificar una nota
            4. Buscar Nota
            5. Salir
            """)       

        

    def start(self):
        while True:
            self.printMenu()
            save = input('Ingrese su opción: ')
            if save == '1':
                self.showNotes()
            elif save == '2':
                self.addNote()  
            elif save == '3':
                self.editNote()   
            elif save == '4':
                self.searchNote()       
            elif save == '5':
                sys.exit(0)    
            

    def showNotes(self):
        if self.notebook.notes == []:
            print('El notebook esta vacio')
        for note in self.notebook.notes:
            print(note.id, note.content, note.tags) 

    def addNote(self):
         content = input('Ingrese el contenido de la nota: ')
         tags = input('Ingrese los tags: ').split(' ')   
         self.notebook.add_note(content, *tags)
         print('Nota agregada.')

    def editNote(self):
        id = int(input('Ingrese el Id de la nota a editar: '))
        content = input('Ingrese el contenido de la nota: ')
        tags = input('Ingrese los tags: ').split(' ')                          
        if content:
            self.notebook.edit_content(id, content)
        if tags:    
            self.notebook.edit_tags(id, *tags) 

    def searchNote(self):
        check = input('Ingrese el Id de la nota a buscar: ')
        result = self.notebook.search(check)
        for note in result:
            print(note.id, note.content, note.tags) 
        

menu = Menu()
menu.start()    