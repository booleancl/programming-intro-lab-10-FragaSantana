from note import Note

class Notebook:
    '''
    Represent a collection of notes
    '''
    def __init__(self):
        '''Notes will be held on a list. The list is empty when created'''
        self.notes = []
    
    def add_note(self, content, *tags):
        ''' Creates a new Note and appends to notes list'''
        self.notes.append(Note(content, *tags))
    
    def edit_content(self,note_id,new_content):
        '''Find the note and change its content'''
        for note in self.notes:
            if str(note.id) == str(note_id):
                note.content = new_content
                break
    
    def edit_tags(self, note_id, *new_tags):
        '''Find the note and change its tags'''
        for note in self.notes:
            if str(note.id) == str(note_id):
                note.tags = [*new_tags]
                break
    
    def search(self, target):
        '''Find all notes that match thw given target'''
        result = []
        for note in self.notes:
            if note.match(target):
                result.append(note)
        return result

    
