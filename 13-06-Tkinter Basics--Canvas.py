import tkinter as tk


root = tk.Tk()
root.title("Simple Canvas Example")

# to Create a Canvas widget
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack(pady=20)

#to Draw a rectangle
canvas.create_rectangle(50, 50, 150, 150, fill="blue")

#to Draw an oval
canvas.create_oval(200, 50, 300, 150, fill="red")

#to Draw a line
canvas.create_line(50, 200, 350, 200, fill="green", width=3)

#to Draw some text
canvas.create_text(200, 300, text="Hello, Canvas!", font=("Arial", 20), fill="purple")


root.mainloop()
