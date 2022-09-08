from note import Note

class TestNote:
    def test_is_a_note(self):
        note = Note('Hola mundo')
        assert isinstance(note, Note)

    def test_init(self):
        note_one = Note('Hola Mundo', 'salute')
        assert note_one.content == 'Hola Mundo'
        assert note_one.tags == ['salute']
    
    def test_id(self):
        note_one = Note('Hola Mundo', 'salute')
        note_two = Note('Chao Mundo', 'salute')
        assert note_one.id == 3
        assert note_two.id == 4
    
    def test_match(self):
        note_one = Note('Hola Mundo', 'salute')
        assert note_one.match('Hola') == True
        assert note_one.match('salute') == True
        assert note_one.match('Chao') == False
    