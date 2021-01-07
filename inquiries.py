import menu
import sqlite3


def convertTuple(tup):  # Tuple to String converter
    str = ''.join(tup)
    return str


def inquiries():  # Inquiries menu

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    action = 0
    while action < 1 or action > 7:
        print("\n (1) Account Balance (2) All Incomes (3) Latest Income (4) All Expenses")
        print("\n (5) Latest Expense (6) Main Menu (7) Exit")
        print()
        action = int(input("Type the desired option: "))
        print()

        if action == 1:  # Account Balance

            for incomes in cursor.execute("SELECT SUM(amount) FROM flow WHERE type='I'"):
                incomes = incomes[0]  # Converts from Real to Float

            for expenses in cursor.execute("SELECT SUM(amount) FROM flow WHERE type='E'"):
                expenses = expenses[0]

            print(" Incomes: $ {0:,.2f}".format(incomes))
            print("Expenses: $ {0:,.2f}".format(expenses))
            balance = incomes - expenses
            print(" Balance: $ {0:,.2f}".format(balance))
            print()
            wait = input("** PRESS ENTER TO CONTINUE **")
            inquiries()

        elif action == 2:  # All Incomes
            print(">> All Incomes:")
            print()

            for row in cursor.execute("SELECT name, amount, date FROM flow WHERE type='I'"):
                print(row)
            print()

            for incomes in cursor.execute("SELECT SUM(amount) FROM flow WHERE type='I'"):
                incomes = incomes[0]
            print("TOTAL: $ {0:,.2f}".format(incomes))
            print()
            wait = input("** PRESS ENTER TO CONTINUE **")
            inquiries()

        elif action == 3:  # Lastest Income

            # Optional (unedited)
            #income = "SELECT name, amount, date FROM flow WHERE type=? ORDER BY rowid DESC LIMIT 1"
            #cursor.execute(income, [("I")])
            #print(cursor.fetchone())
            #print()

            print(">> Latest Income:")
            print()
            for name in cursor.execute("SELECT name FROM flow WHERE type='I'"):
                tuple = name
                str = convertTuple(tuple)
                new_name = str
            for amount in cursor.execute("SELECT amount FROM flow WHERE type='I'"):
                amount = amount[0]
            for date in cursor.execute("SELECT date FROM flow WHERE type='I'"):
                tuple = date
                str = convertTuple(tuple)
                new_date = str
            print(new_name, "- $ {0:,.2f}".format(amount), "-", new_date)
            print()

            wait = input("** PRESS ENTER TO CONTINUE **")
            inquiries()

        elif action == 4:  # All Expenses
            print(">> All Expenses:")
            print()

            for row in cursor.execute("SELECT name, amount, date FROM flow WHERE type='E'"):
                print(row)
            print()

            for expenses in cursor.execute("SELECT SUM(amount) FROM flow WHERE type='E'"):
                expenses = expenses[0]
            print("TOTAL: $ {0:,.2f}".format(expenses))

            print()
            wait = input("** PRESS ENTER TO CONTINUE **")
            inquiries()

        elif action == 5:  # Latest Expense

            # Optional (unedited)
            #expense = "SELECT name, amount, date FROM flow WHERE type=? ORDER BY rowid DESC LIMIT 1"
            #cursor.execute(expense, [("E")])
            #print(cursor.fetchone())
            #print()

            print(">> Latest Expense:")
            print()
            for name in cursor.execute("SELECT name FROM flow WHERE type='E'"):
                tuple = name
                str = convertTuple(tuple)
                new_name = str
            for amount in cursor.execute("SELECT amount FROM flow WHERE type='E'"):
                amount = amount[0]
            for date in cursor.execute("SELECT date FROM flow WHERE type='E'"):
                tuple = date
                str = convertTuple(tuple)
                new_date = str
            print(new_name, "- $ {0:,.2f}".format(amount), "-", new_date)
            print()

            wait = input("** PRESS ENTER TO CONTINUE **")
            inquiries()

        elif action == 6:  # Returns to the main menu
            conn.close()
            menu.menu()

        elif action == 7:  # Closes the application
            conn.close()
            print("Session closed.")
            exit()

        else:  # Restarts the loop
            print("*** Choose one of the available options! ***")
            print()
            continue

if __name__ == "__main__":
    inquiries()
