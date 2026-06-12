# Login System

def check_access(role, feature):
    access_levels = {
        "admin": ["calculator", "users", "reports"],
        "cashier": ["calculator"],
        "customer": ["calculator"]
    }
    return feature in access_levels.get(role, [])


users = {
    "admin": {"password": "1234", "role": "admin"},
    "cashier1": {"password": "5678", "role": "cashier"},
    "customer1": {"password": "9012", "role": "customer"}
}

attempts = 3

while attempts > 0:
    username = input("Enter Username: ").strip()
    password = input("Enter Password: ").strip()

    if username in users and users[username]["password"] == password:
        role = users[username]["role"]

        print("Login successful!")
        print(f"Role: {role}")

        if check_access(role, "calculator"):

            # Product Purchase Section
            subtotal = float(input("Enter product subtotal: "))

            coupon = input("Enter coupon code: ").upper()

            # Discount Logic
            if coupon == "SAVE10":
                discount = subtotal * 0.10
                print("10% discount applied")

            elif coupon == "SAVE20" and subtotal >= 100:
                discount = subtotal * 0.20
                print("20% discount applied")

            else:
                discount = 0
                print("Invalid coupon or conditions not met")

            # Tax by Location
            location = input("Enter location: ").lower()

            if location == "Kampala":
                tax_rate = 0.02
            elif location == "Mukono":
                tax_rate = 0.15
            elif location == "Mbrara":
                tax_rate = 0.10
            else:
                tax_rate = 0.05

            discounted_price = subtotal - discount
            tax = discounted_price * tax_rate
            final_price = discounted_price + tax

            print("----- RECEIPT -----")
            print(f"Subtotal: {subtotal:.2f}")
            print(f"Discount: {discount:.2f}")
            print(f"Tax: {tax:.2f}")
            print(f"Final Price: {final_price:.2f}")

        # Extra admin features
        if check_access(role, "users"):
            print("\nAdmin Access: User Management")

        if check_access(role, "reports"):
            print("Admin Access: Reports")

        break

    else:
        attempts -= 1
        print(f"Invalid login. Attempts left: {attempts}")

if attempts == 0:
    print("Too many failed attempts.Access denied.")