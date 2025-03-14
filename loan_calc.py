1#! /usr/bin/python3

from loan import Loan

ln = Loan()
active = True

while active:
    print(ln.print_header())

    while True:
        try:
            prompt = f"\nEnter present value (e.g., 19366)\n"
            PV = input(prompt)
            PV = float(PV)
            break
        except ValueError:
            print(f"{PV} is not valid. Must be a number(float).")
    while True:
        try:
            prompt = f"Enter rate per period (e.g., 4.59)\n"
            r = input(prompt)
            r = float(r)
            break
        except ValueError:
            print(f"{r} is not valid. Must be a number(float).")
    while True:
        try:
            prompt = f"Enter number of periods in months (e.g., 60)\n"
            n = input(prompt)
            n = int(n)
            break
        except ValueError:
            print(f"{n} is not valid. Must be a number(integer).")

    P = ln.calculate_payment(PV, r, n)
    ln.present_payment(P, PV, r, n)
    plot = input(f"\nPlot loan?\n (y or n)")
    if plot == 'y':
        ln.plot_loan(P, PV, r, n)
        more = input(f"\nCalculate another payment?\n (y or n)")
    else:
        more = input(f"\nCalculate another payment?\n (y or n)")

    if more == 'n':
        active = False
        print("\nGOODBYE!")
    else:
        ln.clear()
