from classes import frames as f

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

    # Page Hit
    def page_hit_events(self, index):
        for frame in self.frames:
            frame.set_current_event_as_hit()
        self.increment_page_hits()

    # Page Fault
    def page_fault_events(self, index):
        for frame in self.frames:
            frame.set_current_event_as_fault()
        self.increment_page_faults()

    # Page Replacement
    def page_replacement_event(self, index, page, frame_id):
        self.frames[frame_id].replace_page(page, index)
