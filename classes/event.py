from EventType import EventType

class Event:
    def __init__(self, event_index):
        self.event_index = event_index
        self.event_data = -1
        self.event_type = EventType.NOT_USED

    # Getters
    def get_event_index(self):
        return self.event_index

    def get_event_data(self):
        return self.event_data

    def get_event_type(self):
        return self.event_type

    # Setters
    def set_event_data(self, event_data):
        self.event_data = event_data

    def set_event_type(self, event_type):
        self.event_type = event_type

    # Unique methods

    # Check if event is empty
    def is_empty(self):
        return self.event_data == -1

    # Check if event data is equal to a number
    def is_equal_to(self, number):
        return self.event_data == number

    # Copy previous event
    def copy_event(self, event):
        self.event_data = event.get_event_data()





## TESTS ##

def test_event():
    # Creation of Events
    events = []
    for i in range(10):
        events.append(Event(i))

    # Check events initialization
    for i in range(10):
        assert events[i].get_event_index() == i
        assert events[i].get_event_data() == -1
        assert events[i].get_event_type() == EventType.NOT_USED

    # Set event data
    for i in range(10):
        events[i].set_event_data(i)
        assert events[i].get_event_data() == i
    
    # Set event type
    b = 1
    for i in range(10):
        if b == 5:
            b = 1
        events[i].set_event_type(EventType(b))
        assert events[i].get_event_type() == EventType(b)
        b += 1

    print("Event tests passed")

def test_event_unique_methods():
    # Creation of Events
    events = []
    for i in range(10):
        events.append(Event(i))

    # Check events initialization
    for i in range(10):
        assert events[i].get_event_index() == i
        assert events[i].get_event_data() == -1
        assert events[i].get_event_type() == EventType.NOT_USED

    # Check if event is empty
    for i in range(10):
        assert events[i].is_empty() == True

    # Set event data
    for i in range(10):
        events[i].set_event_data(i)
        assert events[i].get_event_data() == i

    # Check if event is empty
    for i in range(10):
        assert events[i].is_empty() == False

    # Check if event data is equal to a number
    for i in range(10):
        assert events[i].is_equal_to(i) == True

    # Check if event data is equal to a number
    for i in range(10):
        assert events[i].is_equal_to(i+1) == False

    # Copy previous event
    for i in range(1, 10):
        events[i].copy_event(events[i-1])
        assert events[i].get_event_data() == events[i-1].get_event_data()

    print("Event unique methods tests passed")

if __name__ == '__main__':
    # test_event()
    test_event_unique_methods()
