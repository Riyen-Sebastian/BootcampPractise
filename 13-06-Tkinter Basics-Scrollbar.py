import tkinter as tk


root = tk.Tk()
root.title("Simple Listbox with Scrollbar")


listbox = tk.Listbox(root)
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Creating a Scrollbar widget
scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Configuring the Listbox to use the Scrollbar
listbox.config(yscrollcommand=scrollbar.set)#links the Scrollbar to the Listbox.
scrollbar.config(command=listbox.yview)#sets the Scrollbar to control the vertical view of the Listbox.


for i in range(1, 11):
    listbox.insert(tk.END, f"Item {i}")


root.mainloop()
