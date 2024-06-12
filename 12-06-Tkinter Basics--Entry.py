import tkinter as tk

# Function to get the text from the entry widget and store it in a variable
def store_input():
    user_input = entry.get()
    label.config(text=f"Stored Text: {user_input}")


root = tk.Tk()
root.title("Tkinter Entry Example")


entry = tk.Entry(root, width=40)
entry.pack(pady=10)


button = tk.Button(root, text="Store Input", command=store_input)
button.pack(pady=5)


label = tk.Label(root, text="Stored Text: ")
label.pack(pady=5)


root.mainloop()
