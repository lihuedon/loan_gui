from guizero import App, Box, Text, TextBox, PushButton, error  # , Window
import tkinter as tk
from loan import Loan

ln = Loan()
header = "%s" % ln.print_header()

gui = App("Loan Calculator", width=1000, height=600, bg="#CCFFFF")

# Load the icon image
try:
    icon_img = tk.PhotoImage(file="~/PycharmProjects/loan_gui/loan.png")
    gui.tk.iconphoto(False, icon_img)
except tk.TclError:
    print("icon.png not found. Using default icon.")

def calculate_payment():
    """Validate input, calculate payment, and return formatted results."""
    while True:
        if not input_present_value.value.replace(".", "").isdigit():
            error("Input error", "You must type a valid loan amount.")
            break
        elif not input_rate.value.replace(".", "").isdigit():
            error("Input error", "You must type a valid interest rate.")
            break
        elif not input_period.value.isdigit():
            error("Input error", "You must type a valid number of months.")
            break
        else:
            PV = float(input_present_value.value)
            r = float(input_rate.value)
            n = int(input_period.value)
            P = ln.calculate_payment(PV, r, n)
            display.value = "%s" % ln.prepare_plot_title(P, PV, r, n)
            plot_button.update_command(_plot, args=[P, PV, r, n])
            plot_button.show()
            plot_button.focus()
            break


def _set():
    """Set input fields."""
    input_present_value.value = ""
    input_rate.value = ""
    input_period.value = ""
    input_present_value.bg = "white"
    input_rate.bg = "white"
    input_period.bg = "white"
    display.value = ""
    plot_button.hide()
    input_present_value.focus()


def _plot(P, PV, r, n):
    """Plot the loan payment, amortization, etc."""
    ln.plot_loan(P, PV, r, n)


def _key_event(event_data):
    """Listen for enter/esc keys and submit/reset form."""
    # enter key submits form
    if 13 == ord(event_data.key):
        calculate_payment()
    # esc key resets form
    elif 27 == ord(event_data.key):
        _set()


def _quit():
    """Quit app."""
    gui.destroy()


title_box = Box(gui, width="fill", height="100", align="top", border=False)
title_text = Text(title_box, header, font="NouveauFLF", size=12, color="violet")

content_box = Box(gui, layout="grid", width="fill", height="fill", align="top", border=True)
label_present_value = Text(content_box, "Present Value", align="left", font="Arial", size=16, color="black",
                           grid=[0, 0])
input_present_value = TextBox(content_box, align="left", width=20, grid=[1, 0])
label_rate = Text(content_box, "Interest Rate", align="left", font="Arial", size=16, color="black", grid=[0, 1])
input_rate = TextBox(content_box, align="left", width=10, grid=[1, 1])
label_period = Text(content_box, "Number of Months", align="left", font="Arial", size=16, color="black", grid=[0, 2])
input_period = TextBox(content_box, align="left", width=5, grid=[1, 2])

display = Text(content_box, "any", font="Arial", size=16, color="violet", bg="#99FFFF", grid=[1, 3])
submit_button = PushButton(gui, command=calculate_payment, align="left", text="Submit")
clear_button = PushButton(gui, command=_set, align="left", text="Reset")
plot_button = PushButton(gui, command=_plot, align="right", text="Plot")
quit_button = PushButton(gui, command=_quit, align="left", text="Quit")
_set()

gui.when_key_pressed = _key_event

gui.display()
