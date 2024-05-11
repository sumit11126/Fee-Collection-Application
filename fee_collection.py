
import getpass

# Simulated database for user credentials and fee status
user_db = {'admin': {'password': 'admin123', 'fee_due': 250000}}
payment_details_template = ['A/c number', 'Amount', 'Bank name', 'IFSC code']

def signup():
    username = input("Enter a new username: ")
    if username in user_db:
        print("Username already exists.")
        return False
    password = getpass.getpass("Enter a new password: ")
    # In a real application, the password should be hashed before storing
    user_db[username] = {'password': password, 'fee_due': 5000}
    print("Signup successful.")
    return True

def login():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    if username in user_db and user_db[username]['password'] == password:
        print("Login successful.")
        return username
    else:
        print("Invalid username or password.")
        return None

def view_fee_status(username):
    fee_due = user_db[username]['fee_due']
    print(f"Your current fee due is: ${fee_due}")

def make_payment(username):
    print("Enter payment details:")
    payment_details = {detail: input(f"{detail}: ") for detail in payment_details_template}
    amount = float(payment_details['Amount'])
    if amount > user_db[username]['fee_due']:
        print("Amount exceeds the due fee. Please enter a valid amount.")
        return
    user_db[username]['fee_due'] -= amount
    print(f"Payment of ${amount} successful. Your new fee due is ${user_db[username]['fee_due']}.")
    # Simulate sending email
    print("Email sent: Your payment was successful.")

def main_menu():
    while True:
        print("\nWelcome to the Fee Collection App")
        choice = input("Choose an option: \n1. Signup\n2. Login\n3. Exit\n> ")
        if choice == '1':
            signup()
        elif choice == '2':
            username = login()
            if username:
                logged_in_menu(username)
        elif choice == '3':
            print("Exiting...")
            break

def logged_in_menu(username):
    while True:
        choice = input(f"\nWelcome {username}, choose an option: \n1. View Fee Status\n2. Make Payment\n3. Logout\n> ")
        if choice == '1':
            view_fee_status(username)
        elif choice == '2':
            make_payment(username)
        elif choice == '3':
            break

if __name__ == "__main__":
    main_menu()
