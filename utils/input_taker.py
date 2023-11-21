# This file contains the class that will be used to take the sequence of page references
# The user will input the sequence of page references and the number of frames in physical memory
# The user will use notepad to input the sequence of page references
#
# The user will input the sequence of page references in the following format:
# 10 (process count)
# 1 2 3 4 5 6 7 8 9 10 (sequence of page references)
# 3 (number of frames in physical memory)
#
# The user will then save the file as a .txt file

# The program will then read the .txt file and take the sequence of page references
# and the number of frames in physical memory
# The class will then return the sequence of page references and the number of frames in physical memory

# The class will assume that the user will input the sequence of page references in the correct format
# The class will also assume that the user will input the correct number of frames in physical memory
# The class will also assume that the user will input the correct number of processes

class SequenceTaker:
    """
    Represents a class that will take the sequence of page references and the number of frames in physical memory.

    Attributes:
        sequence (list): The sequence of page references.
        frames (int): The number of frames in physical memory.
        process_count (int): The number of processes.
    """

    def __init__(self, file_name):
        self.sequence = []
        self.frames = 0
        self.process_count = 0
        self.file_name = file_name

    def take_sequence(self):
        """
        Takes the sequence of page references and the number of frames in physical memory.
        """
        # The program will read the .txt file
        # The program will take the sequence of page references and the number of frames in physical memory
        # The program will then return the sequence of page references and the number of frames in physical memory
        with open(self.file_name, "r") as file:
            self.process_count = int(file.readline())
            self.sequence = file.readline().split()
            self.frames = int(file.readline())
            self.sequence = [int(i) for i in self.sequence]
        return self.sequence, self.frames, self.process_count

    def take_sequence_from_user(self):
        """
        Takes the sequence of page references and the number of frames in physical memory.
        """
        # The program will take the sequence of page references and the number of frames in physical memory
        # The program will then return the sequence of page references and the number of frames in physical memory
        self.process_count = int(input("Enter the number of processes: "))
        self.sequence = input(
            "Enter the sequence of page references: ").split()
        self.frames = int(
            input("Enter the number of frames in physical memory: "))
        self.sequence = [int(i) for i in self.sequence]
        return self.sequence, self.frames, self.process_count

    def print_sequence(self):
        """
        Prints the sequence of page references and the number of frames in physical memory.
        """
        print(self.sequence)
        print(self.frames)
        print(self.process_count)
