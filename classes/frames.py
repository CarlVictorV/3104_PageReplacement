from event import Event
from EventType import EventType

class Frame:
    def __init__(self, frame_id, event_count):
        self.frame_id = frame_id
        self.event_count = event_count
        self.events = []
        for i in range(event_count):
            self.events.append(Event(i))
        
        #Experimental variables
        self.frame_current_page = -1
        self.frame_current_page_age = -1
        self.frame_current_page_birth = -1

    # Getters
    def get_frame_id(self):
        return self.frame_id
    
    def get_event_count(self):
        return self.event_count
    
    def get_events(self):
        return self.events
    
    def get_frame_current_page(self):
        return self.frame_current_page
    
    def get_frame_current_page_age(self):
        return self.frame_current_page_age
    
    def get_frame_current_page_birth(self):
        return self.frame_current_page_birth
    
    # Setters
    def set_frame_id(self, frame_id):
        self.frame_id = frame_id

    def set_event_count(self, event_count):
        self.event_count = event_count

    def set_events(self, events):
        self.events = events

    def set_frame_current_page(self, frame_current_page):
        self.frame_current_page = frame_current_page

    def set_frame_current_page_age(self, frame_current_page_age):
        self.frame_current_page_age = frame_current_page_age

    def set_frame_current_page_birth(self, frame_current_page_birth):
        self.frame_current_page_birth = frame_current_page_birth

    # Unique methods
    # Check if frame is empty
    def is_empty(self):
        return self.frame_current_page == -1
    
    # Check if frame is equal to a page
    def is_equal_to(self, page):
        return self.frame_current_page == page
    
    # Check if frame is equal to a page
    def is_equal_to_page_number(self, page_number):
        return self.frame_current_page == page_number
    
    # increment current page age
    def increment_current_page_age(self):
        self.frame_current_page_age += 1

    # Page Replacement (This situation means this frame's page is being replaced)
    def replace_page(self, page, index):
        self.frame_current_page = page
        self.frame_current_page_age = 0
        self.frame_current_page_birth = index
        self.set_current_event(index, Event.EventType.PAGE_REPLACEMENT, page)

    # Page Hit (This situation means this frame's page or a different frame's page is being hit)
    def page_hit(self, index):
        self.set_current_event(index, Event.EventType.PAGE_HIT, self.get_frame_current_page)
        self.increment_current_page_age()

    # Page Fault (This situation means a different frame is being replaced but this frame's page is not being replaced)
    def page_fault(self, index):
        self.set_current_event(index, Event.EventType.PAGE_FAULT, self.get_frame_current_page)
        self.increment_current_page_age()

    
    # Methods associated with events
    # Set Next Event
    def setup_next_event(self, index):
        self.events[index+1].copy_event(self.events[index])

    # Set Current Event Type
    def set_current_event_type(self, index, event_type):
        self.events[index].set_event_type(event_type)
    
    # Set current event data
    def set_current_event_data(self, index, event_data):
        self.events[index].set_event_data(event_data)

    # Set Current Event 
    def set_current_event(self, index, event_type, event_data):
        self.set_current_event_type(index, event_type)
        self.set_current_event_data(index, event_data)


## TESTS ##
def test_frame():
    # Creation of Frames
    frames = []
    for i in range(10):
        frames.append(Frame(i, 10))

    # Check frames initialization
    for i in range(10):
        assert frames[i].get_frame_id() == i
        assert frames[i].get_event_count() == 10
        assert frames[i].get_frame_current_page() == -1
        assert frames[i].get_frame_current_page_age() == -1
        assert frames[i].get_frame_current_page_birth() == -1
        for j in range(10):
            assert frames[i].get_events()[j].get_event_index() == j
            assert frames[i].get_events()[j].get_event_data() == -1
            assert frames[i].get_events()[j].get_event_type() == EventType.NOT_USED

    # Set frame current page
    for i in range(10):
        frames[i].set_frame_current_page(i)
        assert frames[i].get_frame_current_page() == i

    # Set frame current page age
    for i in range(10):
        frames[i].set_frame_current_page_age(i)
        assert frames[i].get_frame_current_page_age() == i

    # Set frame current page birth
    for i in range(10):
        frames[i].set_frame_current_page_birth(i)
        assert frames[i].get_frame_current_page_birth() == i

    # Set frame current page
    for i in range(10):
        frames[i].set_frame_current_page(i)
        assert frames[i].get_frame_current_page() == i

    # Set frame current page age
    for i in range(10):
        frames[i].set_frame_current_page_age(i)
        assert frames[i].get_frame_current_page_age() == i

    # Set frame current page birth
    for i in range(10):
        frames[i].set_frame_current_page_birth(i)
        assert frames[i].get_frame_current_page_birth() == i

    # Check if frame is empty
    for i in range(10):
        assert frames[i].is_empty() == False

    # Check if frame is equal to a page
    for i in range(10):
        assert frames[i].is_equal_to(i) == True

    # Check if frame is equal to a page number
    for i in range(10):
        assert frames[i].is_equal_to_page_number(i) == True

    # Check increment current page age
    for i in range(10):
        frames[i].increment_current_page_age()
        assert frames[i].get_frame_current_page_age() == i+1


    print("Frame tests passed")


if __name__ == "__main__":
    test_frame()