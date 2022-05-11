class Stack:
    def __init__(self):
        self._content = []
    
    def __len__(self):
        return len(self._content)
    
    def push(self, element):
        if len(self._content) <= 6:
            self._content.append(element)
        else:
            return
    
    def top(self):
        return self._content[-1]

    def isNotFull(self):
        return len(self._content) < 6