age = int(input("What is your age: "))

if age <= 12:
    print("\033[1mYour ticket cost is £5\033[0m")
elif age <= 17:
    print("\033[1mYour ticket cost is £7\033[0m")
elif age <= 64:
    print("\033[1mYour ticket cost is £10\033[0m")
else:
    print("\033[1mYour ticket cost is £6\033[0m")
