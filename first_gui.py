import tkinter as tk

# Create window
root = tk.Tk()
root.title("My First GUI")
# Set window size
root.geometry("400x300")

# create label
label = tk.Label(root, text="Hello, Tkinter!", font=("Helvetica", 16))
label.pack(pady=20)

# create an entry field
entry = tk.Entry(root, width=30)
entry.pack(pady=10)


# Create function for a button
def on_button_click():
    text = entry.get()
    label.config(text=f"You Entered {text}")


# create button
button = tk.Button(root, text="click me", command=on_button_click)
button.pack(pady=20)

root.mainloop()
