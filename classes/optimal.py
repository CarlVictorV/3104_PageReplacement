import page as p
import frames as f
from EventType import EventType

class Optimal(p.Page):
    def __init__(self, page_sequence, frame_count, page_count):
        super().__init__(page_sequence, frame_count, page_count)
        self.frames = []
        for i in range(frame_count):
            self.frames.append(f.Frame(i, page_count))
        self.optimal()

    def optimal(self):
        """
        Simulates the Optimal algorithm.
        """
        index = 0
        for page in self.page_sequence:
            # Check if page is in a frame
            if self.check_for_page(page):
                self.page_hit_events(index)
            # Check if there is an empty frame
            elif self.check_for_empty_frame():
                self.page_fault_events(index)
                self.add_page_to_empty_frame(page, index)
            # If there is no empty frame and page is not in a frame
            # Find the oldest page and replace it
            else:
                self.page_fault_events(index)
                self.page_replacement_event(
                    index, page, self.find_optimal_page(index))

            index += 1

        self.calculate_rates()
        self.print_optimal_table()

    def find_optimal_page(self, current_index):
        """
        Finds the page that will not be used for the longest time.
        """
        frame_current_pages_next_use_index = []
        for frame in self.frames:
            frame_current_pages_next_use_index.append(
                self.find_next_use_index(frame.get_frame_current_page(), current_index))
            
        # If a page is not used again, it will be replaced
        if -1 in frame_current_pages_next_use_index:
            return frame_current_pages_next_use_index.index(-1)
        else:
            return frame_current_pages_next_use_index.index(max(frame_current_pages_next_use_index))

            
    def find_next_use_index(self, page, current_index):
        """
        Finds the next use index of a page.
        """
        for i in range(current_index, len(self.page_sequence)):
            if self.page_sequence[i] == page:
                return i
        return -1

    def print_optimal_table(self):
        """
        Prints the Optimal table.
        """
        print(f"+------------+")
        print(f"| OPTIMAL    |", )

        self.print_sequence()
        self.print_frames()
        self.print_rates()


def main():
    page_sequence = [7, 0, 1, 2, 0, 3, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7]
    frame_count = 3
    page_count = 17

    # page_sequence = [7, 0, 1, 2, 0, 3, 0, 4,
    #                  2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
    # frame_count = 3
    # page_count = 20
    opt = Optimal(page_sequence, frame_count, page_count)


if __name__ == "__main__":
    main()
