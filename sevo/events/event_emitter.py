class Event_emitter():
    def __init__(self):
        self._listeners = {}

    def has(self, type):
        if type in self._listeners:
            return True
        return False


    def on(self, type, listener):
        if not self.has(type):
            self._listeners[type] = listener
            return True
        return False

    def off(self, type):
        if type in self._listeners:
            del self._listeners[type]
            return True
        return False
        

    def emit(self, event):
        if self.has(event.type):
            self._listeners[event.type](event)
        return False
    
    def get_listeners(self):
        return self._listeners