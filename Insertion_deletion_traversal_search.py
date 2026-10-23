
# Array Operations

arr = [10, 20, 30, 40, 50]

# Traversal
def traversal():
    print("Array elements:", arr)

# Insertion
def insertion():
    value = int(input("Enter value to insert: "))
    pos = int(input("Enter position (1-based): "))

    if 1 <= pos <= len(arr) + 1:
        arr.insert(pos - 1, value)
        print("Element inserted successfully.")
    else:
        print("Invalid position!")

# Deletion
def deletion():
    pos = int(input("Enter position to delete (1-based): "))

    if 1 <= pos <= len(arr):
        arr.pop(pos - 1)
        print("Element deleted successfully.")
    else:
        print("Invalid position!")

# Searching
def searching():
    value = int(input("Enter value to search: "))

    for i in range(len(arr)):
        if arr[i] == value:
            print("Element found at position", i + 1)
            return

    print("Element not found.")

# Main menu
while True:
    print("\n1. Traversal")
    print("2. Insertion")
    print("3. Deletion")
    print("4. Searching")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        traversal()
    elif choice == 2:
        insertion()
    elif choice == 3:
        deletion()
    elif choice == 4:
        searching()
    elif choice == 5:
        print("Program terminated.")
        break
    else:
        print("Invalid choice!")
