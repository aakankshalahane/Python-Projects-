expenses = []

while True:
    print("\n1. Add Expense  2. View  3. Total  4. Exit")
    ch = input("Choose: ")
    if ch == '1':
        item = input("Item: ")
        amt = float(input("Amount: "))
        expenses.append((item, amt))
    elif ch == '2':
        for i, (item, amt) in enumerate(expenses, 1):
            print(f"{i}. {item} - ₹{amt}")
    elif ch == '3':
        print("Total:", sum(a for _, a in expenses))
    elif ch == '4':
        break
