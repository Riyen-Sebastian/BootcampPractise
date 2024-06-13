import tkinter as tk


def display_selection(selection):
    label.config(text=f"Selected: {selection}")


root = tk.Tk()
root.title("Simple Menu Example")

# Creating a menu bar
menu_bar = tk.Menu(root)

# Creating a "File" menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Option 1", command=lambda: display_selection("Option 1"))
file_menu.add_command(label="Option 2", command=lambda: display_selection("Option 2"))

# Addding the File menu to the menu bar
menu_bar.add_cascade(label="File", menu=file_menu)

# Configuring the main window to use the menu bar
root.config(menu=menu_bar)

# Creating a Label widget to display the selected option
label = tk.Label(root, text="Select an option from the menu")
label.pack(pady=20)


root.mainloop()
