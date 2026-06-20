
class ContactManager:
    def __init__(self):
        # This list will hold all our contacts.
        # Each contact is a tuple: (name, phone, email)
        self.contacts = []

    # ------------------------------------------------------------------
    # TASK 1: VALIDATION HELPER METHODS
    # ------------------------------------------------------------------

    def is_valid_phone(self, phone):
        """
        A phone number is valid if it ONLY contains digits and hyphens.
        Example of valid phone numbers: "0701234567", "+256-701-234567"
        Note: '+' is allowed too since phone numbers often start with it.
        """
        for character in phone:
            if not (character.isdigit() or character == "-" or character == "+"):
                return False
        return True

    def is_valid_email(self, email):
        """
        An email is valid if it contains an '@' AND a '.' (period).
        Example: lynette@gmail.com
        """
        if "@" in email and "." in email:
            return True
        return False

    # ------------------------------------------------------------------
    # CREATE - Add Contact (with validation added for Task 1)
    # ------------------------------------------------------------------

    def add_contact(self, name, phone, email=""):
        # Validate phone number first
        if not self.is_valid_phone(phone):
            print("Error: Phone number can only contain digits, '+' and '-'. Contact not added.")
            return

        # Validate email ONLY if the user actually typed one
        if email != "" and not self.is_valid_email(email):
            print("Error: Email must contain '@' and '.'. Contact not added.")
            return

        # If validation passes, save the contact
        new_contact = (name, phone, email)
        self.contacts.append(new_contact)
        print(f"Contact '{name}' added successfully!")

    # ------------------------------------------------------------------
    # READ - View a single contact by name
    # ------------------------------------------------------------------

    def view_contact(self, name):
        found = False
        for contact in self.contacts:
            if contact[0].lower() == name.lower():
                self.print_contact(contact)
                found = True
        if not found:
            print(f"No contact found with the name '{name}'.")

    # ------------------------------------------------------------------
    # UPDATE - Update an existing contact (with validation added for Task 1)
    # ------------------------------------------------------------------

    def update_contact(self, name, new_phone=None, new_email=None):
        for index in range(len(self.contacts)):
            current_name, current_phone, current_email = self.contacts[index]

            if current_name.lower() == name.lower():
                # Validate new phone (if the user wants to change it)
                if new_phone:
                    if not self.is_valid_phone(new_phone):
                        print("Error: Phone number can only contain digits, '+' and '-'. Update cancelled.")
                        return
                    current_phone = new_phone

                # Validate new email (if the user wants to change it)
                if new_email:
                    if not self.is_valid_email(new_email):
                        print("Error: Email must contain '@' and '.'. Update cancelled.")
                        return
                    current_email = new_email

                # Save the updated contact back into the list
                self.contacts[index] = (current_name, current_phone, current_email)
                print(f"Contact '{name}' updated successfully!")
                return

        print(f"No contact found with the name '{name}'.")

    # ------------------------------------------------------------------
    # DELETE - Remove a contact by name
    # ------------------------------------------------------------------

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact[0].lower() == name.lower():
                self.contacts.remove(contact)
                print(f"Contact '{name}' deleted successfully!")
                return
        print(f"No contact found with the name '{name}'.")

    # ------------------------------------------------------------------
    # TASK 2: ADVANCED SEARCH (name, phone, OR email) + clean printout
    # ------------------------------------------------------------------

    def search_contacts(self, keyword):
        """
        Searches contacts by name, phone number, OR email.
        The keyword just needs to appear somewhere inside any of those
        three fields (case-insensitive search).
        """
        keyword = keyword.lower()
        results = []

        for contact in self.contacts:
            name, phone, email = contact
            if (keyword in name.lower()) or (keyword in phone.lower()) or (keyword in email.lower()):
                results.append(contact)

        self.print_search_results(results, keyword)

    # ------------------------------------------------------------------
    # READ - List every contact
    # ------------------------------------------------------------------

    def list_all_contacts(self):
        if len(self.contacts) == 0:
            print("Your contact list is empty.")
            return

        print("\n=== All Contacts ===")
        for contact in self.contacts:
            self.print_contact(contact)

    # ------------------------------------------------------------------
    # HELPER METHODS FOR CLEAN, USER-FRIENDLY OUTPUT (Task 2)
    # ------------------------------------------------------------------

    def print_contact(self, contact):
        """Nicely prints a single contact tuple."""
        name, phone, email = contact
        print("-----------------------------")
        print(f"Name : {name}")
        print(f"Phone: {phone}")
        if email == "":
            print("Email: (not provided)")
        else:
            print(f"Email: {email}")
        print("-----------------------------")

    def print_search_results(self, results, keyword):
        """Nicely prints the list of search results."""
        if len(results) == 0:
            print(f"No contacts matched '{keyword}'.")
            return

        print(f"\nFound {len(results)} contact(s) matching '{keyword}':")
        for contact in results:
            self.print_contact(contact)


# ----------------------------------------------------------------------
# TASK 3: INTERACTIVE CLI MENU
# ----------------------------------------------------------------------

def print_menu():
    print("\n=== Contact Manager Menu ===")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Search Contacts")
    print("6. List All Contacts")
    print("7. Exit")


def main():
    manager = ContactManager()

    while True:
        print_menu()
        choice = input("Choose an option (1-7): ")

        # ---------------- 1. ADD CONTACT ----------------
        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email (optional, press Enter to skip): ")
            manager.add_contact(name, phone, email)

        # ---------------- 2. VIEW CONTACT ----------------
        elif choice == "2":
            name = input("Enter the name of the contact to view: ")
            manager.view_contact(name)

        # ---------------- 3. UPDATE CONTACT ----------------
        elif choice == "3":
            name = input("Enter the name of the contact to update: ")
            new_phone = input("Enter new phone number (press Enter to keep unchanged): ")
            new_email = input("Enter new email (press Enter to keep unchanged): ")

            # If the user just pressed Enter, treat it as "no change"
            if new_phone == "":
                new_phone = None
            if new_email == "":
                new_email = None

            manager.update_contact(name, new_phone, new_email)

        # ---------------- 4. DELETE CONTACT ----------------
        elif choice == "4":
            name = input("Enter the name of the contact to delete: ")
            manager.delete_contact(name)

        # ---------------- 5. SEARCH CONTACTS ----------------
        elif choice == "5":
            keyword = input("Enter a name, phone number, or email to search for: ")
            manager.search_contacts(keyword)

        # ---------------- 6. LIST ALL CONTACTS ----------------
        elif choice == "6":
            manager.list_all_contacts()

        # ---------------- 7. EXIT ----------------
        elif choice == "7":
            print("Goodbye!")
            break

        # ---------------- INVALID CHOICE ----------------
        else:
            print("Invalid option. Please choose a number between 1 and 7.")


# This makes sure main() only runs when this file is executed directly
if __name__ == "__main__":
    main()