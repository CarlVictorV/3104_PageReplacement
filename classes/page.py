import frames as f


class Page:
    def __init__(self, page_sequence, frame_count, page_count):
        self.page_sequence = page_sequence
        self.page_count = page_count
        self.frame_count = frame_count

        self.frames = []
        for i in range(frame_count):
            self.frames.append(f.Frame(i, page_count))

        self.page_faults = 0
        self.page_hits = 0
        self.page_fault_rate = 0.0
        self.page_hit_rate = 0.0

    # Getters
    def get_page_sequence(self):
        return self.page_sequence

    def get_page_count(self):
        return self.page_count

    def get_frame_count(self):
        return self.frame_count

    def get_page_faults(self):
        return self.page_faults

    def get_page_hits(self):
        return self.page_hits

    def get_page_fault_rate(self):
        return self.page_fault_rate

    def get_page_hit_rate(self):
        return self.page_hit_rate

    # Setters
    def set_page_sequence(self, page_sequence):
        self.page_sequence = page_sequence

    def set_page_count(self, page_count):
        self.page_count = page_count

    def set_frame_count(self, frame_count):
        self.frame_count = frame_count

    def set_page_faults(self, page_faults):
        self.page_faults = page_faults

    def set_page_hits(self, page_hits):
        self.page_hits = page_hits

    def set_page_fault_rate(self, page_fault_rate):
        self.page_fault_rate = page_fault_rate

    def set_page_hit_rate(self, page_hit_rate):
        self.page_hit_rate = page_hit_rate

    # Unique methods
    def increment_page_faults(self):
        self.page_faults += 1

    def increment_page_hits(self):
        self.page_hits += 1

    def calculate_rates(self):
        self.page_fault_rate = self.page_faults / len(self.page_sequence)
        self.page_hit_rate = self.page_hits / len(self.page_sequence)

    # Methods for Frames control

    # Check every frame for same page
    def check_for_page(self, page):
        for frame in self.frames:
            if frame.is_equal_to(page):
                return True
        return False

    # Check for empty frame
    def check_for_empty_frame(self):
        for frame in self.frames:
            if frame.is_empty():
                return True
        return False

    # Add page to empty frame
    def add_page_to_empty_frame(self, page, index):
        for frame in self.frames:
            if frame.is_empty():
                frame.replace_page(page, index)
                return

    # Page Hit
    def page_hit_events(self, index):
        for frame in self.frames:
            frame.page_hit(index)
        self.increment_page_hits()

    # Page Fault
    def page_fault_events(self, index):
        for frame in self.frames:
            frame.page_fault(index)
        self.increment_page_faults()

    # Page Replacement
    def page_replacement_event(self, index, page, frame_id):
        self.frames[frame_id].replace_page(page, index)

    # Find the oldest page from the frames and return its index
    def find_oldest_page(self):
        oldest_page = self.frames[0]
        for frame in self.frames:
            if frame.get_frame_current_page_birth() < oldest_page.get_frame_current_page_birth():
                oldest_page = frame
        return oldest_page.get_frame_id()

    # Print methods

    def print_sequence(self):
        print(f"+------------+", end="")
        for page in self.page_sequence:
            print("-----+", end="")
        print(f"\n| PCount: {self.page_count:<2} |", end="")
        for page in self.page_sequence:
            print(f"  {page:<3}|", end="")
        print(f"\n+------------+", end="")
        for page in self.page_sequence:
            print("-----+", end="")

    def print_frames(self):
        for frame in self.frames:
            print(f"\n| Frame {frame.get_frame_id()+1:<3}  |", end="")

            for event in frame.events:
                if (event.get_event_type() == f.EventType.NOT_USED or event.get_event_data() == -1):
                    print(f"     |", end="")
                else:
                    event_data = str(event.get_event_data())
                    print(f"  {event_data:<3}|", end="")
            print(f"\n+------------+", end="")
            for event in frame.events:
                print("-----+", end="")

        print(f"\n| Page F: {self.get_page_faults():<2} |", end="")
        for events in self.frames[0].events:
            if (events.get_event_type() == f.EventType.PAGE_FAULT or events.get_event_type() == f.EventType.PAGE_REPLACEMENT):
                print(f"  F  |", end="")
            else:
                print(f"     |", end="")
        print(f"\n+------------+", end="")
        for event in self.frames[0].events:
            print("-----+", end="")
        print(f"\n| Page H: {self.get_page_hits():<2} |", end="")
        for events in self.frames[0].events:
            if (events.get_event_type() == f.EventType.PAGE_HIT):
                print(f"  H  |", end="")
            else:
                print(f"     |", end="")
        print(f"\n+------------+", end="")
        for event in self.frames[0].events:
            print("-----+", end="")


    def print_rates(self):
        fault_rate = "{:.2f}%".format(self.get_page_fault_rate()*100)
        hits_rate = "{:.2f}%".format(self.get_page_hit_rate() * 100)
        print(f"\n| Fault Rate: {fault_rate:>10} |", end="")
        print(f"\n+------------------------+", end="")
        print(f"\n| Hits  Rate: {hits_rate:>10} |", end="")
        print(f"\n+------------------------+", end="")


    def print_table(self):
        print("TABLE")
        self.print_sequence()
        self.print_frames()
        self.print_rates()


def test_print_sequence():
    page_sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
    frame_count = 5
    page_count = 17
    page = Page(page_sequence, frame_count, page_count)
    page.set_page_faults(17)
    page.set_page_hits(0)
    page.calculate_rates()
    page.set_page_hit_rate(0.54536)
    page.print_table()
    


if __name__ == "__main__":
    test_print_sequence()
