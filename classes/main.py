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
    print("[1] FIFO - First In First Out")
    print("[2] LRU - Least Recently Used")
    print("[3] LFU - Least Frequently Used")
    print("[4] Optimal\n")
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
        clear()
        menu()
        choice = input("Enter choice: ")
        print()

        if choice == "0":
            clear()
            print("Exiting...")
            return

        algorithm = algorithms.get(choice)
        if algorithm:
            try:
                clear()
                execute_algorithm(algorithm)
                input("\nPress Enter to return to the menu...")
            except Exception as e:
                clear()
                print(f"An error occurred: {str(e)}")
                input("\nPress Enter to continue...")
        else:
            clear()
            print("Invalid input. Please choose a valid option.")
            input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
