class Command(object):
    
    def __init__(self, name, arguments = None):
        self.name = name
        self.arguments = arguments

    def reply(self):
        pass