database = {}

class Budget():
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

    def deposit(amount, bal):
        bal += amount
        return bal

    def withdraw(user, amount, bal):
        bal -= amount
        return bal

    def balance(db):
        for categ, bal in db.items():
            print(categ, bal)

    def transfer(db, option1, amount, option2):
        value1 = db[option1]
        value2 = db[option2]


        db[option1] = int(value1) - amount
        db[option2] = int(value2) + amount
        return db

def init():
    print("=====Welcome to your Budget App=====")
    menu()


def menu():
    try:
        user = int(input("======What would you like to do?====== \n Press \n (1) to create new budget \n (2) to deposit"))

    except:
        print("Invald input, please try again.")
        menu()
    if (user == 1):
        new_budget()
    elif (user == 2):
        deposit()
    elif (user == 3):
        debit()
    elif (user == 4):
        balance()
    elif (user == 5):
        transfer()
    elif (user == 6):
        out()
    else:
        print("Invald input, please try again.")
        menu()
def new_budget():
    print("=====Creating a New Budget===== \n")

    budget_title = input("Enter budget name \n")
    try:
        amount = int(input("Enter your budget amount \n"))
    except:
        print("Invald input, please try again.")
        new_budget()
    budget = Budget(budget_title, amount)
    database[budget_title] = amount

    print(f"Budget %s was setup with %d" %(budget_title, amount))
    menu()

def debit():
    print("======Withdraw from a created budget======")
    print("*********Choose from Available Budgets.********")
    for key, value in database.items():
        print(f"-   {key}")


    pick = int(input("Press \n (1) To continue with your debit transaction. \n (2) To stop debit transaction \n"))
    if (pick == 1):
        user = input("****Select one of budget(s) mmentioned Above. \n")
        if user in database:
            print("Note: You can not withdraw all your budget.")
            amt = int(input("Enter amount \n"))
            if amt <= database[user]:
                balance = int(database[user])
                new_balance = Budget.withdraw(user, amt, balance)
                database[user] = new_balance
                print(f"${amt} has been debited from Budget-{user} \n Budget amount remaining ${new_balance}")
                menu()
            else:
                print(f"Budget {user} is insufficient of the {amt} \n the actual amount is {database[user]}. \n  \n So please try again.")
    elif (pick == 2):
        print("You have terminated the debit transaction.")
        menu()
    else:
        print("Invald input, please try again.")
        debit()


def deposit():
    print("****Deposit into a Budget******")
    print("***** Available Budgets *******")
    for key, value in database.items():
        print(f"-   {key}")

    pick = int(input("Press \n (1) To continue with your Deposit transaction. \n (2) To stop Deposit transaction \n"))
    if (pick == 1):
        user = input("****Select one of budget(s) mmentioned Above. \n")
        if user in database:
            
            amt = int(input("Enter amount \n"))
            balance = int(database[user])
            new_balance = Budget.deposit(amt, balance)
            database[user] = new_balance
            print(f"${amt} has been credited with ${amt} \n Total Budget amount is now ${new_balance}")
            menu()

        else:
            print("  ")
            pick = int(input(f"Budget {user} does not exist! \n Press \n (1) To create new budget \n (2) To choose right budget"))

            if (pick == 1):
                new_budget()

            elif (pick == 2):
                credit()
            else:
                print("Invald input, please try again.")
                credit()
    elif (pick == 2):
        print("You have terminated the deposit transaction.")
        menu()
    else:
        print("Invald input, please try again.")
        deposit()
def balance():
    print("******Getting your budget balance******** \n")
    check_bal = Budget.balance(database)
    if (check_bal == None):
        print("  ")
        menu()
    else:
        print(f"${check_bal}")
        menu()


def transfer():
    print("******Transfer Operations******")
    print("Note: You can not withdraw all your budget. \n")
    from_budget = input("Enter the budget you are transfering from \n")
    if from_budget in database:
        from_amount = int(input("Enter amount you want to transfer \n"))
        if from_amount <= database[from_budget]:
            to_budget = input("Enter destination of funds \n")
            if to_budget in database:
                db = Budget.transfer(database, from_budget, from_amount, to_budget)
                print("  ")
                print(f"You transfered ${from_amount} from {from_budget} to {to_budget}")
                for key, value in db.items():
                    print(key, value)
                menu()
            else:
                print(f'{from_budget} Budget does not exist, Please choose from the valid budget below \n')
                transfer()
        else:
            print(f'You do not have such amount-${from_amount} in {from_budget} budget')
            transfer
    else:
        print(f'Budget {from_budget} does not exist \n')
        transfer()

def out():
    try:
        pick = int(input("Are you sure you want to quit? \n Press: \n (1) to quit \n (2) to continue \n"))
    except:
        print("Invalid input \n")
        out()

    if (pick == 1):
        print("We hope you had a good budgeting experience.")
        quit()
    elif (pick == 2):
        menu()
    else:
        print("invalid input \n")
        out()



init()
