password_input = str(input("Enter password: "))

if len(password_input) >= 8 and len(password_input) <=16:
    contain_letter = False
    contain_number = False
    for char in password_input:
        if char.isalpha():
            contain_letter = True
        elif char.isdigit():
            contain_number = True
    if contain_number and contain_number:
        print(f"\nPassword is valid.")
    else:
        print(f"\nPassword invalid, must contain both letters and numbers")
else:
    print(f"\nPassword invalid, must be between 8 and 16 characters long.")
