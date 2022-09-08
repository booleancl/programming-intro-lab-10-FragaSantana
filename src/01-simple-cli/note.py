import datetime

last_id = 0

class Note:
    '''
    Representation of a single note with two attributes: content and tags
    Has a match method to test against the content and tags
    '''
    def __init__(self,content = '', *tags):
        self.content = content
        self.tags = [*tags]
        self.created_at = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, target):
        ''' Test if this note has the target on the content or in tags'''
        return target in self.content or target in self.tags



