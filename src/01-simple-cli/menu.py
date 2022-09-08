import sys
from notebook import Notebook

class Menu:
    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_note,
            "4": self.edit_note,
            "5": self.quit
        }
    
    def display_menu(self):
        print("""
Menú:
1. Ver todas las notas
2. Buscar nota
3. Agregar Nota
4. Modificar Nota
5. Salir
        """)
    def run(self):
        '''Display the menu and respond to choices'''
        while True:
            self.display_menu()
            choice = input("Selecciona una alternativa: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("La opcion seleccionada no es válida")
    
    def show_notes(self, notes=None):
        if not notes:
            notes = self.notebook.notes
            for note in notes:
                print(note.id, note.tags, note.content)
    
    def search_notes(self):
        filter = input("Buscar por: ")
        notes = self.notebook.search(filter)
        self.show_notes(notes)

    def add_note(self):
        content = input("Ingrese la nota: ")
        tags = input("Ingrese los tags: ").split(" ")
        self.notebook.add_note(content, *tags)
        print("La nota fue agregada")

    def edit_note(self):
        id = input("Ingrese el id de la nota ")
        content = input("Ingrese el nuevo vontenido: ")
        tags = input("Ingrese los tags: ").split(" ")
        if content:
            self.notebook.edit_content(id, content)
        if tags:
            self.notebook.edit_tags(id, tags)

    def quit(self):
        print("Gracias por usar el editor de notas.")
        sys.exit(0)
    
Menu().run()