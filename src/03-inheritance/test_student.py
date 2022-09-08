from student import Student
from person import Person

class TestStudent:
    def test_is_a_student(self):
        student = Student('Winston', 'Davis')
        assert isinstance(student, Person)