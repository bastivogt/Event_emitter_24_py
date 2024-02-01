from sevo.events.event_emitter import Event_emitter
from sevo.counter_event import Counter_event


class Counter(Event_emitter):
    def __init__(self, start = 0, end = 10, step = 1):
        super().__init__()
        self._start = start
        self._end = end
        self._step = step
        self._count = self._start

    def run(self):
        self._count = self._start
        self.emit(Counter_event(Counter_event.COUNTER_STARTED, self, self._count))
        for i in range(self._start, self._end, self._step):
            self._count = i
            self.emit(Counter_event(Counter_event.COUNTER_UDATED, self, self._count))
        self.emit(Counter_event(Counter_event.COUNTER_FINISHED, self, self._count))

    def get_count(self):
        return self._count
        