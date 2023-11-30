from change_calculator import *


def prog_start():
    while True:
        control = user_input()
        if not control:
            break


def user_input():
    userInput = input("Enter 1 to do calculations, 2 to quit: ")

    if userInput == "1":
        calculate_change()
        return True
    elif userInput == "2":
        print("Exiting.")
        return False
    else:
        print("Invalid option. Must be 1 or 2.")
        return False


def calculate_change():
    ctr = 0
    amount = input("Enter the amount to be calculated for change: ")
    calc = ChangeCalculator(amount)
    bills = calc.bills
    verify = calc.verify_input()
    if verify == "Valid option.":
        change = calc.calc_change()
        for amount in change:
            if amount != 0:
                if bills[ctr] == 0.25:
                    print(f"Quarters: {amount}")
                elif bills[ctr] == 0.1:
                    print(f"Dimes: {amount}")
                elif bills[ctr] == 0.05:
                    print(f"Nickels: {amount}")
                elif bills[ctr] == 0.01:
                    print(f"Pennies: {amount}")
                else:
                    print(f"${bills[ctr]} bills: {amount}")
            ctr += 1
    else:
        print(verify)


if __name__ == "__main__":
    prog_start()
