import sqlite3

# Connect to database (creates if not exists)
con = sqlite3.connect("bank.db")
cur = con.cursor()

# Create table for accounts
cur.execute("""
CREATE TABLE IF NOT EXISTS accounts (
    acc_no INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    balance REAL
)
""")
con.commit()


# ---------- FUNCTIONS ----------

def add_acc():
    name = input("Enter Name: ")
    bal = float(input("Enter Initial Deposit: "))
    cur.execute("INSERT INTO accounts (name, balance) VALUES (?, ?)", (name, bal))
    con.commit()
    print("✅ Account created successfully!\n")

def view_all():
    print("\n🏦 All Accounts:")
    for row in cur.execute("SELECT * FROM accounts"):
        print(f"Acc No: {row[0]} | Name: {row[1]} | Balance: ₹{row[2]}")
    print()

def deposit():
    acc = input("Enter Account Number: ")
    amount = float(input("Enter Amount to Deposit: "))
    cur.execute("UPDATE accounts SET balance = balance + ? WHERE acc_no = ?", (amount, acc))
    con.commit()
    print("✅ Deposit successful!\n")

def withdraw():
    acc = input("Enter Account Number: ")
    amount = float(input("Enter Amount to Withdraw: "))
    cur.execute("SELECT balance FROM accounts WHERE acc_no = ?", (acc,))
    bal = cur.fetchone()
    if bal:
        if bal[0] >= amount:
            cur.execute("UPDATE accounts SET balance = balance - ? WHERE acc_no = ?", (amount, acc))
            con.commit()
            print("✅ Withdrawal successful!\n")
        else:
            print("❌ Insufficient balance!\n")
    else:
        print("❌ Account not found!\n")

def check_balance():
    acc = input("Enter Account Number: ")
    cur.execute("SELECT name, balance FROM accounts WHERE acc_no = ?", (acc,))
    row = cur.fetchone()
    if row:
        print(f"👤 Name: {row[0]} | 💰 Balance: ₹{row[1]}\n")
    else:
        print("❌ Account not found!\n")


# ---------- MAIN MENU ----------

while True:
    print("🏦 --- BANK MANAGEMENT SYSTEM ---")
    print("1. Add Account")
    print("2. View All Accounts")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Check Balance")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        add_acc()
    elif choice == '2':
        view_all()
    elif choice == '3':
        deposit()
    elif choice == '4':
        withdraw()
    elif choice == '5':
        check_balance()
    elif choice == '6':
        print("👋 Thank you for using our bank system!")
        break
    else:
        print("❌ Invalid choice! Try again.\n")

