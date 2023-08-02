import tkinter as tk

def on_button_click():
    name = entry.get()
    message = f"Hello, {name}!"
    label.config(text=message)

# Create the main application window
app = tk.Tk()
app.title("Simple Desktop App")

# Create a label and pack it into the window
label = tk.Label(app, text="Enter your name:")
label.pack(pady=10)

# Create an entry widget to get user input
entry = tk.Entry(app)
entry.pack(pady=5)

# Create a button to trigger the action
button = tk.Button(app, text="Say Hello", command=on_button_click)
button.pack(pady=10)

# Start the main event loop
app.mainloop()
