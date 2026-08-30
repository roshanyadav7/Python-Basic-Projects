while True:
    print("\n===== EMAIL SLICER =====")

    email = input("Enter your email: ")

    if email.count("@") != 1:
        print("Invalid email! Email must contain exactly one '@'.")
        continue

    username, domain_part = email.split("@")

    if "." not in domain_part:
        print("Invalid email! Domain must contain '.'.")
        continue

    domain, extension = domain_part.split(".", 1)

    if not username or not domain or not extension:
        print("Invalid email! Please enter a complete email address.")
        continue

    print("\n===== EMAIL DETAILS =====")
    print("Username:", username)
    print("Domain:", domain)
    print("Extension:", extension)

    again = input("\nDo you want to slice another email? (yes/no): ")

    if again.lower() != "yes":
        print("Goodbye! 👋")
        break