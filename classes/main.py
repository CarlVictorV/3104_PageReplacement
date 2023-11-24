import fifo as f
import lfu as lf
import lru as lr
import optimal as o
import input_taker as i
import os

test = i.SequenceTaker("temp")


def clear(): return os.system('cls' if os.name == 'nt' else 'clear')


def menu():
    print('+-------------------------------------+')
    print('|--- *Page Replacement Simulation* ---|')
    print('+-------------------------------------+\n')
    print("[1] FIFO")
    print("[2] LRU")
    print("[3] LFU")
    print("[4] Optimal")
    print("[0] Exit")
    print()


def execute_algorithm(algorithm):
    if os.name != 'nt':
        test.retake_sequence(f"inputs/{algorithm.lower()}.txt")
    else:
        test.retake_sequence(f"inputs\\{algorithm.lower()}.txt")

    if algorithm == "FIFO":
        f.FIFO(test.sequence, test.frames, test.process_count)
    elif algorithm == "LRU":
        lr.LRU(test.sequence, test.frames, test.process_count)
    elif algorithm == "LFU":
        lf.LFU(test.sequence, test.frames, test.process_count)
    elif algorithm == "Optimal":
        o.Optimal(test.sequence, test.frames, test.process_count)


def main():
    algorithms = {
        "1": "FIFO",
        "2": "LRU",
        "3": "LFU",
        "4": "Optimal"
    }

    while True:
        menu()
        choice = input("Enter choice: ")
        print()

        if choice == "0":
            clear()
            print("Exiting...")
            return

        algorithm = algorithms.get(choice)
        if algorithm:
            clear()
            execute_algorithm(algorithm)
        else:
            clear()
            print("Invalid input. Please try again.")
            print()


if __name__ == "__main__":
    main()
