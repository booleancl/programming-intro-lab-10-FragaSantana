from readline import append_history_file
from note import Note

class Notebook:
    def __init__(self):                   #aqui inicimos un constructor
        self.notes = []                   #arreglo vacio, con el fin de agregar muchas notas

    def add_note(self, content, *tags):   #esto es un metodo, agrega una nota
        note = Note(content, *tags)       #agregando una instancia a la class Note
        self.notes.append(note)           #con esto permitimos agrgar las notas en el arreglo que declaramos arrioba y est vacio []
        
    def edit_content(self, id, new_content):
        for note in self.notes:
            if note.id == id:
                note.content = new_content

    def edit_tags(self, id, *new_tags):
        for note in self.notes:
            if note.id == id:        
                note.tags = [*new_tags]    

    def search(self, check):       
        result = []     
        for note in self.notes:
            if note.match(check):
                result.append(note)
        return result        


#noteBook = Notebook()                     #asi se crea una instancia. Validar lo que significa
##print(noteBook.notes)
#noteBook.add_note('Hellow','Salute')      #añadir la primera nota al notebook
#noteBook.add_note('Hi','Saludeishon')     #añadir la segunda nota al notebook
#noteBook.add_note('Hola','saludo')        #añadir la tercera nota al notebook

#print(noteBook.notes[0].content)
#noteBook.edit_content(1,'Hello')          #Editar contente la primera nota
#print(noteBook.notes[0].content)

#
#print(noteBook.notes[0].tags)
#noteBook.edit_tags(1,'Saludo en Ingles','saludarse','saludito')          #Editar tags la primera nota
#print(noteBook.notes[0].tags)
#
#print(noteBook.search('Saludo'))
#print(noteBook.notes[0].tags)

#print(noteBook.notes[1].content)
#print(noteBook.notes[2].content)
#print(noteBook.notes[0].tags)
#print(noteBook.notes[1].tags)
#print(noteBook.notes[2].tags)
#print(len(noteBook.notes))