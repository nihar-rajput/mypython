# python banking program

def show_balance(balance):
    print(f"your balance is ${balance}")

def deposite():
    amount = float(input("enter the amount to be deposited : "))

    if amount < 0:
        print("that is not a valid amount")
        return 0
    else:
        print(f"you deposited ${amount}")
        return  amount

def withdraw():
    amount = float(input("Enter the amount to be withdraw : "))

    if amount < 0:
        print("insufficient balance!")
        return 0

    else:
        print(f"you withdraw ${amount}")
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print()
        print("banking program")
        print("1.show balance")
        print("2.deposite ")
        print("3.withdraw")
        print("4.exit")
        print()

        choice = input("Enter your choice (1-4) : ")

        match choice :
            case '1':
                show_balance(balance)
            case '2':
                balance += deposite()
            case '3':
                balance -= withdraw()
            case '4':
                is_running = False
            case _:
                print()
                print("enter a valid choice ")
                print()

    print("thank you have a nice day")

if __name__ == "__main__":
    main()