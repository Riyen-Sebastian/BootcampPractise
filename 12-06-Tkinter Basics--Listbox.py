import tkinter as tk

# Function to display the selected item from the listbox
def display_selection():
    selected_index = listbox.curselection()
    if selected_index:
        selected_item = listbox.get(selected_index)
        label.config(text=f"Selected Item: {selected_item}")
    else:
        label.config(text="No item selected")

# Creating the main window
root = tk.Tk()
root.title("Simple Listbox Example")

# Creating a Listbox widget
listbox = tk.Listbox(root)
listbox.pack(pady=10)

# Inserting items into the Listbox
items = ["Apple", "Mango", "Orange"]
for item in items:
    listbox.insert(tk.END, item)#tk.END referes tot the end position of the listbox

# Creating a Button widget to display the selected item
button = tk.Button(root, text="Show Selection", command=display_selection)
button.pack(pady=5)

# Creating a Label widget to display the selected item
label = tk.Label(root, text="Selected Item: None")
label.pack(pady=10)


root.mainloop()
