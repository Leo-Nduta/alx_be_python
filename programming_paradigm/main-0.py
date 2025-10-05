import sys
from programming_paradigm.bank_account import BankAccount

def main():
    account = BankAccount(100)  # Example starting balance
    
    print("Usage: python main.py <command>:<amount>")
    print("Commands: deposit, withdraw, display")

    while True:
        command = input("Enter command: ").lower()
        if command in ["deposit", "withdraw"]:
            try:
                amount = float(input("Enter an amount: "))
            except ValueError:
                print("Please enter a valid number.")
                continue
        else:
            amount = None

        
        if command == "deposit" and amount is not None:
            account.deposit(amount)
            print(f"Deposited: ${amount}")
        elif command == "withdraw" and amount is not None:
            if account.withdraw(amount):
                print(f"Withdrew: ${amount}")
            else:
                print("Insufficient funds.")
        elif command == "display":
            print(account.display_balance())
        elif command == "exit":
            print("Goodbye")
            break
        else:
            print("Invalid command.")

if __name__ == "_main_":
    main()