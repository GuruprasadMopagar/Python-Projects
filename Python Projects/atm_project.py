correct_pin = 2004
balance = 2000
flag = False
mini_statement = []

print("Welcome to the ATM")
atempts = 3
while True:
    PIN = int(input("Enter the PIN to continue: "))

    if PIN != correct_pin and atempts>1:
        print("Invalid PIN, Please re enter the PIN")
        atempts-=1
        print(f"You have only {atempts} attempts")

    elif PIN == correct_pin:
        print("Login Successful")
        flag = True
        break

    else:
        print("You have entered wrong PIN 3 times. So your account has been blocked for 24 hours")
        break


if flag:
    while True:
            print("="*40)
            print("              ATM MENU")
            print("="*40)
            print("1.Check Balance")
            print("2. Deposit Money")
            print("3.Withdraw money")
            print("4.Mini Statement")
            print("5. Exit")
            choice = int(input("Choose any one operation to perform:"))

            if choice == 1:
                print('='*40)
                print(f"Your current balance: {balance}")

            elif choice == 2:
                print('='*40)
                amt = int(input("Enter the amount for deposit: Rs."))
                if amt >0:
                    balance+=amt
                    print(f"You have successfully deposited Rs.{amt}")
                    mini_statement.insert(0, f"credited:{amt}")
                else:
                    print("Invalid amount")

            elif choice == 3:
                print('='*40)
                amt = int(input("Enter the amount for withdraw: Rs."))
                if amt >0 and amt%100==0:
                    if amt<balance:
                        balance-=amt
                        print(f"You have successfully debited Rs.{amt}")
                        mini_statement.insert(0,f"debited:{amt}")
                    else:
                        print("Insufficient Balance")
                else:
                    print("Invalid amount, amount must be multiples of 100")

            elif choice == 4:
                print('='*40)
                for i in mini_statement:
                    print(i)


            elif choice == 5:
                print('='*40)
                break

            else:
                print("Invalid Operation")

        