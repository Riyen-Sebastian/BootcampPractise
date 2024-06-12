import tkinter as tk


root = tk.Tk()
root.title("Checkbutton ")

# Variable to store the state of the checkbutton
check_var = tk.IntVar()

# Function to be called when the checkbutton state changes
def on_checkbutton_change():
    print(f"Checkbutton state: {check_var.get()}")

# Create a checkbutton
checkbutton = tk.Checkbutton(root, text="Check me!", variable=check_var, command=on_checkbutton_change)
checkbutton.pack(pady=20)


root.mainloop()
