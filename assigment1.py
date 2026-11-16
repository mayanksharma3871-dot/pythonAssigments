print("===== SECURE EMPLOYEE ACCOUNT SYSTEM =====")

accounts = {}

n = int(input("Enter number of accounts to create: "))

for i in range(n):

    print("\n--- Account", i + 1, "---")

    username = input("Enter username: ")

    while True:

        password = input("Enter password: ")

        upper_case = 0
        lower_case = 0
        digit_count = 0
        special_char = 0
        space_count = 0

        for j in password:

            if j == " ":
                space_count += 1

            elif j.isupper():
                upper_case += 1

            elif j.islower():
                lower_case += 1

            elif j.isdigit():
                digit_count += 1

            else:
                special_char += 1

        if (len(password) >= 8 and
            upper_case > 0 and
            lower_case > 0 and
            digit_count > 0 and
            special_char > 0 and
            space_count == 0):

            print("Password accepted!")
            break

        else:

            print("Password rejected!")

            if len(password) < 8:
                print("Password must contain at least 8 characters.")

            if upper_case == 0:
                print("Password must contain an uppercase alphabet.")

            if lower_case == 0:
                print("Password must contain a lowercase alphabet.")

            if digit_count == 0:
                print("Password must contain a digit.")

            if special_char == 0:
                print("Password must contain a special character.")

            if space_count > 0:
                print("Password must not contain any space.")

            print("Please enter the password again.")

    while True:

        confirm = input("Confirm password: ")

        if confirm == password:

            accounts[username] = password
            print("Account created successfully!")
            break

        else:

            print("Passwords do not match.")
            print("Please enter the confirm password again.")


print("\n===== EMPLOYEE LOGIN =====")

for i in range(5):

    username = input("Enter username: ")
    pwd = input("Enter password: ")

    if username in accounts and accounts[username] == pwd:

        print("Login successful!")
        print("Welcome", username)
        break

    else:

        print("Invalid username or password.")

        if i < 4:
            print("Attempts remaining:", 4 - i)

else:

    print("Access Denied!")
    print("Maximum login attempts exceeded.")