from enum import Enum

class EventType(Enum):
    PAGE_FAULT = 1
    PAGE_HIT = 2
    NOT_USED = 3
    PAGE_REPLACEMENT = 4


# Check if enum is working

def test_event_type():
    assert EventType.PAGE_FAULT == EventType(1)
    assert EventType.PAGE_HIT == EventType(2)
    assert EventType.NOT_USED == EventType(3)
    assert EventType.PAGE_REPLACEMENT == EventType(4)

    event = EventType.PAGE_FAULT
    assert event == EventType(1)
    print("event = " + str(event))
    event = EventType.PAGE_HIT
    assert event == EventType(2)
    print("event = " + str(event))
    event = EventType.NOT_USED
    assert event == EventType(3)
    print("event = " + str(event))
    event = EventType.PAGE_REPLACEMENT
    assert event == EventType(4)
    print("event = " + str(event))
    

    print("Event Type tests passed")


if __name__ == "__main__":
    test_event_type()   