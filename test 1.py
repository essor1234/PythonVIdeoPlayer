import tkinter as tk
from tkinter import ttk

# Create a root window
root = tk.Tk()
root.title("My Application")

# Create a frame for the feature buttons
button_frame = ttk.Frame(root)
button_frame.pack(side=tk.TOP, fill=tk.X)

# Create 8 feature buttons and pack them in the button frame
buttons = []
for i in range(8):
    button = ttk.Button(button_frame, text=f"Feature {i+1}")
    button.pack(side=tk.LEFT, padx=5, pady=5)
    buttons.append(button)

# Create a frame for the search bar and refresh button
search_frame = ttk.Frame(root)
search_frame.pack(side=tk.TOP, fill=tk.X)

# Create a search entry and pack it in the search frame
search_entry = ttk.Entry(search_frame)
search_entry.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5, pady=5)

# Create a refresh button and pack it in the search frame
refresh_button = ttk.Button(search_frame, text="Refresh")
refresh_button.pack(side=tk.RIGHT, padx=5, pady=5)

# Create a notebook for the main screens
notebook = ttk.Notebook(root)
notebook.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

# Create two main screens and add them to the notebook
main_screen1 = ttk.Frame(notebook)
main_screen2 = ttk.Frame(notebook)
notebook.add(main_screen1, text="Main Screen 1")
notebook.add(main_screen2, text="Main Screen 2")

# Create a label for the sub screen and pack it in the first main screen
sub_screen_label = ttk.Label(main_screen1, text="Sub Screen")
sub_screen_label.pack(side=tk.TOP, padx=5, pady=5)

# Create a sub screen and pack it in the first main screen
sub_screen = ttk.Frame(main_screen1, borderwidth=1, relief=tk.SUNKEN)
sub_screen.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

# Start the main loop
root.mainloop()