import requests

API_URL = "https://cbu.uz/uz/arkhiv-kursov-valyut/json/" # Currency API of Uzbekistan Central Bank

def get_currency():
    response = requests.get(API_URL)
    for currencies in response.json():
        return float(currencies['Rate'])

def get_balance(balance):
    balance = balance * get_currency()
    print(f"Your balance is {balance.__round__(2)} UZS")


def check_balance(balance):
    print(f"Your balance is {balance.__round__(2)} UZS.\nChoose service if you want to continue ?")
    choice = input("1. Withdraw \n 2. Deposit \n 4. Exit \n")
    match choice:
        case "1":
            withdraw(balance)
        case "2":
            deposit(balance)
        case "3":
            exit

def withdraw(balance):
    amount = float(input("Enter the amount to withdraw in UZS: "))
    if amount > balance:
        print("Insufficient balance. Please try again.")
        withdraw(balance)
    else:
        balance -= amount
        print(f"Successfully withdrew {amount} UZS. Your new balance is {balance.__round__(2)} UZS.\nChoose service if you want to continue ?")
        choice = input("1. Withdraw \n 2. Deposit \n 3. Exit \n")
        match choice:
            case "1":
                withdraw(balance)
            case "2":
                deposit(balance)
            case "3":
                exit


def deposit(balance):
    amount = float(input("Enter the amount to deposit in UZS: "))
    new_balance = balance * get_currency() + amount
    print(f"Successfully deposited {amount} UZS. Your new balance is {new_balance.__round__(2)} UZS.\nChoose service if you want to continue ?")
    choice = input("1. Withdraw \n 3. Deposit \n 4. Exit \n")
    match choice:
        case "1":
            withdraw(new_balance)
        case "2":
            deposit(new_balance)
        case "3":
            exit


def main():
    balance = 1
    choice = input("Choose service: \n 1. Check balance \n 2. Withdraw \n 3. Deposit \n")
    match choice:
        case "1":
            get_balance(balance)
        case "2":
            withdraw(balance)
        case "3":
            deposit(balance)

if __name__ == "__main__":
    main()