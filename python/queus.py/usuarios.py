import os
from datetime import date

# Lists
ids = []
firstnames = []
lastnames = []
mobile_phones = []
emails = []
statuses = []
genders = []
created_at = []


# Functions
def mainMenu():
    print("::: Main menu :::")
    print("[1]. Register a new user")
    print("[2]. List all users")
    print("[3]. Search user")
    print("[4]. Delete user")
    print("[5]. Update user")
    print("[6]. Show active users")
    print("[7]. Show inactive users")
    print("[8]. Exit")


# Main
while True:
    os.system("cls" if os.name == "nt" else "clear")
    mainMenu()

    opt = input("Press any option [1-8]: ")

    match opt:

        case "1":
            os.system("cls" if os.name == "nt" else "clear")
            print("::: Register form :::")

            id = input("Ident. number: ")

            if id in ids:
                print("User already registered.")
            else:
                firstname = input("Firstname: ")
                lastname = input("Lastname: ")
                mobile_phone = input("Mobile phone: ")
                email = input("E-mail: ")
                gender = input("Gender [M/F/O]: ").upper()

                ids.append(id)
                firstnames.append(firstname)
                lastnames.append(lastname)
                mobile_phones.append(mobile_phone)
                emails.append(email)
                statuses.append(True)
                genders.append(gender)
                created_at.append(date.today())

                print("User has been created successfully!!")

            any_key = input(
                "Press any key to back to Main Menu..."
            )

        case "2":
            print("::: List all registered users :::")

            for i in range(len(ids)):
                print(f"ID: {ids[i]}")
                print(f"Firstname: {firstnames[i]}")
                print(f"Lastname: {lastnames[i]}")
                print(f"Mobile phone: {mobile_phones[i]}")
                print(f"E-mail: {emails[i]}")
                print(f"Gender: {genders[i]}")
                print(f"Status: {statuses[i]}")
                print(f"Created at: {created_at[i]}")
                print("-------------------------")

            if len(ids) == 0:
                print("No registered users.")

            any_key = input("Press any key...")

        case "3":
            print("::: Search user :::")
            id = input("Ident. number: ")

            if id in ids:
                i = ids.index(id)
                print(f"ID: {ids[i]}")
                print(f"Firstname: {firstnames[i]}")
                print(f"Lastname: {lastnames[i]}")
                print(f"Mobile phone: {mobile_phones[i]}")
                print(f"E-mail: {emails[i]}")
                print(f"Gender: {genders[i]}")
                print(f"Status: {statuses[i]}")
                print(f"Created at: {created_at[i]}")
            else:
                print("User not found.")

            any_key = input("Press any key...")

        case "4":
            print("::: Delete user :::")
            id = input("Ident. number: ")

            if id in ids:
                i = ids.index(id)

                ids.pop(i)
                firstnames.pop(i)
                lastnames.pop(i)
                mobile_phones.pop(i)
                emails.pop(i)
                statuses.pop(i)
                genders.pop(i)
                created_at.pop(i)

                print("User deleted successfully.")
            else:
                print("User not found.")

            any_key = input("Press any key...")

        case "5":
            print("::: Update user :::")
            id = input("Ident. number: ")

            if id in ids:
                i = ids.index(id)

                firstnames[i] = input(
                    f"Firstname [{firstnames[i]}]: "
                ) or firstnames[i]

                lastnames[i] = input(
                    f"Lastname [{lastnames[i]}]: "
                ) or lastnames[i]

                mobile_phones[i] = input(
                    f"Mobile phone [{mobile_phones[i]}]: "
                ) or mobile_phones[i]

                emails[i] = input(
                    f"E-mail [{emails[i]}]: "
                ) or emails[i]

                genders[i] = (
                    input(f"Gender [{genders[i]}]: ").upper()
                    or genders[i]
                )

                print("User updated successfully.")
            else:
                print("User not found.")

            any_key = input("Press any key...")

        case "6":
            print("::: Active users :::")
            found = False

            for i in range(len(ids)):
                if statuses[i]:
                    print(
                        f"ID: {ids[i]} - "
                        f"{firstnames[i]} {lastnames[i]}"
                    )
                    found = True

            if not found:
                print("No active users.")

            any_key = input("Press any key...")

        case "7":
            print("::: Inactive users :::")
            found = False

            for i in range(len(ids)):
                if not statuses[i]:
                    print(
                        f"ID: {ids[i]} - "
                        f"{firstnames[i]} {lastnames[i]}"
                    )
                    found = True

            if not found:
                print("No inactive users.")

            any_key = input("Press any key...")

        case "8":
            any_key = input("Bye bye. Press any key...")
            break

        case _:
            any_key = input(
                "Invalid option. Press any key to try again..."
            )