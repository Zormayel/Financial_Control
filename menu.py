import transactions
import inquiries


def menu():  # Main menu of the application, redirects to the specific applications

    print()
    print("*** MAIN MENU ***")

    action = 0
    while action < 1 or action > 3:
        print("\n (1) Transactions (2) Inquiries (3) Exit")
        print()
        action = int(input("Type the desired option: "))
        if action == 1:
            transactions.transactions()
        elif action == 2:
            inquiries.inquiries()
        elif action == 3:
            print()
            print("Session closed.")
            exit()
        else:
            print()
            print("*** Choose one of the available options! ***")
            continue

if __name__ == "__main__":
    menu()
