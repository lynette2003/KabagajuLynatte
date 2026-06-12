 # KABAGAJU LYNETTE   24/U/O4951/EVE

def get_tip_percentage():
    print("\nSelect tip percentage:")
    print("1. 10%","\n2. 15%","\n3. 20%","\n4. Custom")

    
    while True:
        choice = input("Enter choice (1-4): ").strip()
        if choice == '1':
            return 10
        elif choice == '2':
            return 15
        elif choice == '3':
            return 20
        elif choice == '4':
            while True:
                try:
                    custom = float(input("Enter custom tip percentage: "))
                    if custom < 0:
                        print("Tip cannot be negative.")
                    else:
                        return custom
                except ValueError:
                    print("Invalid input. Enter a number.")
        else:
            print("Invalid choice. Please enter 1-4.")


def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Value must be greater than zero.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Value must be at least 1.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def main():
    print("=" * 40)
    print("      BILL SPLIT CALCULATOR")
    print("=" * 40)

    total_bill = get_positive_float("Enter total bill amount (UGX): ")
    num_people = get_positive_int("Enter number of people: ")
    tip_percent = get_tip_percentage()

    tip_amount = total_bill * (tip_percent / 100)
    total_with_tip = total_bill + tip_amount
    amount_per_person = total_with_tip / num_people

    print("\n" + "=" * 40)
    print("         RECEIPT SUMMARY")
    print("=" * 40)
    print(f"  Original Bill:      UGX {total_bill:,.2f}")
    print(f"  Tip ({tip_percent}%):          UGX {tip_amount:,.2f}")
    print(f"  Total Bill:         UGX {total_with_tip:,.2f}")
    print(f"  Number of People:   {num_people}")
    print("-" * 40)
    print(f"  Each Person Pays:   UGX {amount_per_person:,.2f}")
    print("=" * 40)


if __name__ == "__main__":
    main()