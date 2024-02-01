from sevo.counter_event import Counter_event
from sevo.counter import Counter


name = "Sevo"
print(f"Hallo {name}!")

def counter_start_handler(event):
    print(f"type: {event.type} count: {event.count}")

def counter_update_handler(event):
    print(f"type: {event.type} count: {event.count}")

def counter_finish_handler(event):
    print(f"type: {event.type} count: {event.count}")

counter = Counter()

""" counter.on(Counter_event.COUNTER_STARTED, counter_start_handler)
counter.on(Counter_event.COUNTER_UDATED, counter_start_handler)
counter.on(Counter_event.COUNTER_FINISHED, counter_start_handler) """

counter.on(Counter_event.COUNTER_STARTED, 
           lambda event: print(f"type: {event.type} count: {event.count}"))

counter.on(Counter_event.COUNTER_UDATED, 
           lambda event: print(f"type: {event.type} count: {event.count}"))

counter.on(Counter_event.COUNTER_FINISHED, 
           lambda event: print(f"type: {event.type} count: {event.count}"))

counter.run()





