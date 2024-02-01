from sevo.events.event import Event

class Counter_event(Event):
    COUNTER_STARTED = "counter-started"
    COUNTER_UDATED = "counter-updated"
    COUNTER_FINISHED = "counter-finished"
    
    def __init__(self, type, sender, count):
        super().__init__(type, sender)
        self.count = count