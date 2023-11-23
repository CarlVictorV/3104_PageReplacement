import fifo as f
import lfu as lf
import lru as lr
import optimal as o
import input_taker as i
import os

test = i.SequenceTaker("temp")
def clear(): return os.system('cls' if os.name == 'nt' else 'clear')


def menu():
    print("MENU: ")
    print()
    print("[1] FIFO")
    print("[2] LRU")
    print("[3] LFU")
    print("[4] Optimal")
    print("[0] Exit")
    print()


def fifo():
    if os.name != 'nt':
        test.retake_sequence(r"inputs/fifo.txt")
    else:
        test.retake_sequence(r"inputs\fifo.txt")
    fifo = f.FIFO(test.sequence, test.frames, test.process_count)


def lru():
    if os.name != 'nt':
        test.retake_sequence(r"inputs/lru.txt")
    else:
        test.retake_sequence(r"inputs\lru.txt")
    lru = lr.LRU(test.sequence, test.frames, test.process_count)


def lfu():
    if os.name != 'nt':
        test.retake_sequence(r"inputs/lfu.txt")
    else:
        test.retake_sequence(r"inputs\lfu.txt")
    lfu = lf.LFU(test.sequence, test.frames, test.process_count)


def optimal():
    if os.name != 'nt':
        test.retake_sequence(r"inputs/optimal.txt")
    else:
        test.retake_sequence(r"inputs\optimal.txt")
    opt = o.Optimal(test.sequence, test.frames, test.process_count)


def main():
    while (True):
        menu()
        choice = input("Enter choice: ")
        print()
        if choice == "1":
            clear()
            fifo()
        elif choice == "2":
            clear()
            lru()
        elif choice == "3":
            clear()
            lfu()
        elif choice == "4":
            clear()
            optimal()
        elif choice == "0":
            clear()
            print("Exiting...")
            return
        else:
            clear()
            print("Invalid input. Please try again.")
            print()
            continue


if __name__ == "__main__":
    main()
