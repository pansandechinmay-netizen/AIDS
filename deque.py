
# Deque using a circular array

class Deque:
    def __init__(self, size):
        self.MAX = size
        self.arr = [None] * size
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.MAX == self.front

    # Add element at front
    def insert_front(self, value):
        if self.is_full():
            print("Deque is Full!")
            return

        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.front = (self.front - 1) % self.MAX

        self.arr[self.front] = value
        print(value, "inserted at front.")

    # Add element at rear
    def insert_rear(self, value):
        if self.is_full():
            print("Deque is Full!")
            return

        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.MAX

        self.arr[self.rear] = value
        print(value, "inserted at rear.")

    # Delete element from front
    def delete_front(self):
        if self.is_empty():
            print("Deque is Empty!")
            return

        value = self.arr[self.front]

        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.MAX

        print("Deleted from front:", value)

    # Delete element from rear
    def delete_rear(self):
        if self.is_empty():
            print("Deque is Empty!")
            return

        value = self.arr[self.rear]

        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.rear = (self.rear - 1) % self.MAX

        print("Deleted from rear:", value)

    # Display deque
    def display(self):
        if self.is_empty():
            print("Deque is Empty!")
            return

        print("Deque elements:", end=" ")
        i = self.front

        while True:
            print(self.arr[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.MAX

        print()


# Main program
size = int(input("Enter deque size: "))

if size <= 0:
    print("Size must be positive.")
else:
    dq = Deque(size)

    while True:
        print("\n--- DEQUE MENU ---")
        print("1. Insert at Front")
        print("2. Insert at Rear")
        print("3. Delete from Front")
        print("4. Delete from Rear")
        print("5. Display")
        print("6. Exit")

        try:
            choice = int(input("Enter choice: "))

            if choice == 1:
                value = int(input("Enter value: "))
                dq.insert_front(value)
            elif choice == 2:
                value = int(input("Enter value: "))
                dq.insert_rear(value)
            elif choice == 3:
                dq.delete_front()
            elif choice == 4:
                dq.delete_rear()
            elif choice == 5:
                dq.display()
            elif choice == 6:
                print("Program terminated.")
                break
            else:
                print("Invalid choice!")

        except ValueError:
            print("Please enter a valid integer.")
