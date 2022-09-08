from person import Person

class TestPerson:
    def test_is_a_person(self):
        person = Person('Winston', 'Davis')
        assert isinstance(person, Person)