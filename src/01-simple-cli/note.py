counter = 0

class Note:
    def __init__(self, content, *tags):
        self.content = content
        self.tags = [*tags]
        global counter
        counter += 1
        self.id = counter

    def match(self, check):
        if check in self.content:
            return True
        elif check in self.tags:
            return True
        else:
            return False    


#note_one = Note('Hola Mundo','Saludo','Español')
#answer = note_one.match('español')
#print(answer)
#print(note_one.id)
#print(note_one.content)
#print(note_one.tags)


#note_two = Note('Despedida','Hola','Bienvenido','Chao','Hasta Luego')
#print(note_two.id)
#print(note_two.tags)
