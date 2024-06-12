import tkinter as tk

# Function to display the selected option
def display_selection():
    selected_option = radio_var.get()
    label.config(text=f"Selected Option: {selected_option}")


root = tk.Tk()
root.title("Tkinter Radiobutton Example")

# Create an IntVar to store the value of the selected radiobutton
radio_var = tk.IntVar()

# Create Radiobutton widgets
radiobutton1 = tk.Radiobutton(root, text="Option 1", variable=radio_var, value=1)
radiobutton1.pack(anchor=tk.W)#aligns radiobuttons to the left side 

radiobutton2 = tk.Radiobutton(root, text="Option 2", variable=radio_var, value=2)
radiobutton2.pack(anchor=tk.W)

radiobutton3 = tk.Radiobutton(root, text="Option 3", variable=radio_var, value=3)
radiobutton3.pack(anchor=tk.W)

# Create a Button widget to display the selected option
button = tk.Button(root, text="Show Selection", command=display_selection)
button.pack(pady=5)

# Create a Label widget to display the selected option
label = tk.Label(root, text="Selected Option: None")
label.pack(pady=10)


root.mainloop()
