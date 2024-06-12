import tkinter as tk

# Function to get the text from the entry widget and store it in a variable
def store_input():
    user_input = entry.get()
    label.config(text=f"Stored Text: {user_input}")


root = tk.Tk()
root.title("Tkinter Frame Example")

# Create a Frame widget
frame = tk.Frame(root, padx=10, pady=10, borderwidth=2, relief="sunken")
frame.pack(padx=10, pady=10)

#creating an entry and button widget inside the frame
entry = tk.Entry(frame, width=40)
entry.pack(pady=5)
button = tk.Button(frame, text="Store Input", command=store_input)
button.pack(pady=5)

# Create a Label widget outside the Frame 
label = tk.Label(root, text="Stored Text: ")
label.pack(pady=10)


root.mainloop()
