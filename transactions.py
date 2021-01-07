import menu
import sqlite3
import datetime

def transactions():  # Transactions menu, redirects to the core application
    print()
    print("*** TRANSACTIONS MODULE ***")
    print()

    print("\n (1) Income (2) Expense (3) Main Menu (4) Exit")
    print()
    action = 0
    transactions.type = "type"
    while action < 1 or action > 4:
        action = int(input("Type the desired option: "))
        print()
        if action == 1:
            transactions.type = "I"
            main_transactions()
        elif action == 2:
            transactions.type = "E"
            main_transactions()
        elif action == 3:
            menu.menu()
        elif action == 4:
            print("Session closed.")
            exit()
        else:
            print("*** Choose one of the available options! ***")
            continue

if __name__ == "__main__":
    transactions()

#####

def main_transactions():  # Transactions application core
            conn = sqlite3.connect("database.db")
            cursor = conn.cursor()

            type = transactions.type
            name = "name"
            amount = 0.0
            date = 0000-00-00

            name = input("Name of the transaction: ")
            print()

            while amount < 0.1:
                amount = float(input("Amount (ie. 10.57): "))
                if amount < 0.1:
                    print("*** Type a valid amount! ***")
                    continue

            date = datetime.date.today()

            print()
            print("Confirm the information provided:")
            print()
            print(">>> Name: {}, Amount {}".format(name, amount))
            print()

            confirmation = "confirmation"
            while confirmation != "OK" or confirmation != "CANCEL":
                confirmation = input("To confirm type OK, to cancel type CANCEL: ")
                confirmation = confirmation.upper()
                print()
                if confirmation == "OK":
                    print("Confirmed.")
                    break
                elif confirmation == "CANCEL":
                    print("Canceled.")
                    conn.close()
                    transactions()
                else:
                    print("*** Type one option as instructed! ***")
                    print()
                    continue

            print("Saving...")
            cursor.execute("""INSERT INTO flow(type, name, amount, date) VALUES (?,?,?,?)""", (type, name, amount, date))
            conn.commit()
            conn.close()
            print("Transaction completed.")
            transactions()

if __name__ == "__main__":
    main_transactions()
