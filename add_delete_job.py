
# Pizza Parlor Queue using Python

class PizzaQueue:
    def __init__(self, M):
        self.M = M
        self.queue = []

    # Add a new order
    def add_order(self, order):
        if len(self.queue) == self.M:
            print("Queue is full! Cannot accept more orders.")
        else:
            self.queue.append(order)
            print("Order added:", order)

    # Serve (delete) the first order
    def delete_order(self):
        if not self.queue:
            print("Queue is empty! No orders to serve.")
        else:
            order = self.queue.pop(0)
            print("Order served:", order)

    # Display pending orders
    def display(self):
        if not self.queue:
            print("No pending orders.")
        else:
            print("Pending orders:", self.queue)


# Main program
M = int(input("Enter maximum number of orders: "))

if M <= 0:
    print("Maximum orders must be positive.")
else:
    pizza = PizzaQueue(M)

    while True:
        print("\n--- PIZZA PARLOR MENU ---")
        print("1. Add Order")
        print("2. Serve Order")
        print("3. Display Orders")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                order = input("Enter pizza order: ").strip()
                if order:
                    pizza.add_order(order)
                else:
                    print("Order cannot be empty.")

            elif choice == 2:
                pizza.delete_order()

            elif choice == 3:
                pizza.display()

            elif choice == 4:
                print("Thank you!")
                break

            else:
                print("Invalid choice!")

        except ValueError:
            print("Please enter a valid choice.")
