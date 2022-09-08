from notebook import Notebook

class TestNote:
    def test_is_a_notebook(self):
        note = Notebook()
        assert isinstance(note, Notebook)

    def test_init(self):
        notebook = Notebook()
        assert notebook.notes == []
        
    def test_add_note(self):
        notebook = Notebook()
        notebook.add_note("Hello World", "salute","hi")
        assert len(notebook.notes) == 1
    
    def test_edit_content(self):
        notebook = Notebook()
        notebook.add_note("Hello World", "salute","hi")
        notebook.edit_content(7,"Chao World")
        assert notebook.notes[0].content == "Chao World"
    
    def test_edit_tags(self):
        notebook = Notebook()
        notebook.add_note("Hello World", "salute","hi")
        notebook.edit_tags(8,"hola", "chao")
        assert notebook.notes[0].tags == ['hola', 'chao']
