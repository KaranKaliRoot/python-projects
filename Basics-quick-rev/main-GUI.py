import tkinter as tk
from tkinter import messagebox
def palindrome():
    input_string = entry.get()
    second_string = input_string.replace(" ", "").lower()
    reversed_string = second_string[::-1]
    if second_string == reversed_string:
        messagebox.showinfo("Result", f"The input string is a palindrome.\nReversed string: '{reversed_string}'")
    else:
        messagebox.showinfo("Result", f"The input string is not a palindrome.\nReversed string: '{reversed_string}'")

shit_logic = tk.Tk()
shit_logic.title("Palindrome Checker")
entry_label = tk.Label(shit_logic, text="Enter a goddamn string:")
entry_label.pack(pady=10)
entry = tk.Entry(shit_logic, width=50)
entry.pack(pady=10)
check_button = tk.Button(shit_logic, text="確認する", command=palindrome)
check_button.pack(pady=10)



shit_logic.mainloop()
