class ATM:
    def __init__(self, pin, balance=1000):
        self.__pin = pin
        self.__balance = balance

    def validate_pin(self, entered_pin):
        return entered_pin == self.__pin 

    def check_balance(self):
        return f"Current balance: {self.__balance}"
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposit successful! New balance: {self.__balance}"
        else:
            return "Invalid deposit amount!"

    def withdraw(self, amount):
        if amount > self.__balance:
            return "Insufficient funds!"
        elif amount <= 0:
            return "Invalid withdrawal amount!"
        else:
            self.__balance -= amount
            return f"Withdrawal successful! Remaining balance: {self.__balance}"

def atm_menu():
    print("\n----- Welcome to ATM -----")
    print("1. Check Balance              2. Deposit")               
    print("3. Withdraw Money             4. Exit")

if __name__ == "__main__":
    atm = ATM(pin=1234) 
    attempts = 3

    while attempts > 0:
        try:
            entered_pin = int(input("Enter your 4-digit PIN: "))
            if atm.validate_pin(entered_pin): 
                while True:
                    atm_menu()
                    choice = input("Select an option: ")

                    if choice == "1":
                        print(atm.check_balance())
                    elif choice == "2":
                        amount = float(input("Enter deposit amount -> "))
                        print(atm.deposit(amount))
                    elif choice == "3":
                        amount = float(input("Enter withdrawal amount -> "))
                        print(atm.withdraw(amount))
                    elif choice == "4":
                        print("Thank you for using our ATM")
                        exit()
                    else:
                        print("Invalid option! Please try again.")
            else:
                attempts -= 1
                print(f"Incorrect PIN! Attempts left: {attempts}")
                if attempts == 0:
                    print("Too many incorrect attempts. Card blocked!")
        except ValueError:
            print("Invalid input! Please enter numbers only.")
