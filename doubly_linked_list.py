
class Node:
    def __init__(self, time, name=None):
        self.time = time
        self.name = name
        self.prev = None
        self.next = None


class AppointmentList:
    def __init__(self):
        self.head = None
        self.start_time = 9
        self.end_time = 17

    def find(self, time):
        current = self.head
        while current:
            if current.time == time:
                return current
            current = current.next
        return None

    # Insert appointment in the list
    def insert(self, time, name):
        node = Node(time, name)

        if self.head is None:
            self.head = node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = node
        node.prev = current

    # a) Display free slots
    def display_free_slots(self):
        print("\nAvailable appointment slots:")
        found = False

        for hour in range(self.start_time, self.end_time):
            if self.find(hour) is None:
                print(f"{hour:02d}:00")
                found = True

        if not found:
            print("No free slots available.")

    # b) Book appointment
    def book(self):
        try:
            time = int(input("Enter appointment hour (9-16): "))
        except ValueError:
            print("Invalid time!")
            return

        if not self.start_time <= time < self.end_time:
            print("Time is outside working hours (09:00-17:00).")
            return

        if self.find(time):
            print("This slot is already booked!")
            return

        name = input("Enter patient name: ").strip()
        if not name:
            print("Name cannot be empty.")
            return

        self.insert(time, name)
        self.sort_by_time()
        print("Appointment booked successfully.")

    # c) Sort list based on time
    def sort_by_time(self):
        if self.head is None:
            return

        values = []
        current = self.head

        while current:
            values.append((current.time, current.name))
            current = current.next

        values.sort(key=lambda item: item[0])

        current = self.head
        for time, name in values:
            current.time = time
            current.name = name
            current = current.next

    # d) Cancel appointment with validation
    def cancel(self):
        try:
            time = int(input("Enter appointment hour to cancel: "))
        except ValueError:
            print("Invalid time!")
            return

        if not self.start_time <= time < self.end_time:
            print("Invalid time. Use 09:00-16:00.")
            return

        node = self.find(time)

        if node is None:
            print("No appointment booked at this time.")
            return

        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev

        print(f"Appointment for {node.name} cancelled.")

    # e) Sort using pointer manipulation
    def sort_by_pointers(self):
        if self.head is None or self.head.next is None:
            print("List is already sorted.")
            return

        current = self.head.next

        while current:
            key_node = current
            current = current.next

            scan = key_node.prev

            while scan and scan.time > key_node.time:
                scan = scan.prev

            if scan != key_node.prev:
                # Detach key_node
                if key_node.prev:
                    key_node.prev.next = key_node.next

                if key_node.next:
                    key_node.next.prev = key_node.prev

                # Insert at head or after scan
                if scan is None:
                    key_node.prev = None
                    key_node.next = self.head
                    self.head.prev = key_node
                    self.head = key_node
                else:
                    key_node.prev = scan
                    key_node.next = scan.next

                    if scan.next:
                        scan.next.prev = key_node

                    scan.next = key_node

        print("List sorted using pointer manipulation.")

    # Display appointments
    def display(self):
        if self.head is None:
            print("No appointments booked.")
            return

        print("\nBooked Appointments:")
        current = self.head

        while current:
            print(f"{current.time:02d}:00 - {current.name}")
            current = current.next


# Main program
appointments = AppointmentList()

while True:
    print("\n===== APPOINTMENT SYSTEM =====")
    print("1. Display free slots")
    print("2. Book appointment")
    print("3. Sort list by time")
    print("4. Cancel appointment")
    print("5. Sort using pointer manipulation")
    print("6. Display booked appointments")
    print("7. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid menu number.")
        continue

    if choice == 1:
        appointments.display_free_slots()
    elif choice == 2:
        appointments.book()
    elif choice == 3:
        appointments.sort_by_time()
        print("List sorted by time.")
    elif choice == 4:
        appointments.cancel()
    elif choice == 5:
        appointments.sort_by_pointers()
    elif choice == 6:
        appointments.display()
    elif choice == 7:
        print("Thank you!")
        break
    else:
        print("Invalid choice!")
