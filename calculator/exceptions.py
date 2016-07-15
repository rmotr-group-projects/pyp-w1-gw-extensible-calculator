
class InvalidOperation(Exception):
    def __init__(self, msg):
        self.msg = 'Given operation is invalid.'

    def __str__(self):
        return repr(self.msg)


class InvalidParams(Exception):
    def __init__(self, msg):
        self.msg = "Given params are invalid."

    def __str__(self):
        return repr(self.msg)
 
    
