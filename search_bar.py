# Import the Tkinter module
import tkinter as tk

# Create a root window
root = tk.Tk()
root.title("Search Bar Example")

# Create a frame to hold the search bar components
frame = tk.Frame(root, bg="purple")
frame.pack(fill=tk.BOTH, expand=True)

# Create a StringVar object to store and trace the input value
input_var = tk.StringVar()

# Create an Entry widget to accept the user input
entry = tk.Entry(frame, textvariable=input_var, font=("Arial", 14))
entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10, pady=10)

# Create a Button widget to trigger the search function
button = tk.Button(frame, text="Search", font=("Arial", 14), command=lambda: search(input_var.get()))
button.pack(side=tk.RIGHT, padx=10, pady=10)

# Create a Listbox widget to display the matching results from a list of items
listbox = tk.Listbox(root, font=("Arial", 14))
listbox.pack(fill=tk.BOTH, expand=True)

# Create a list of items to search from
items = ["Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grape", "Honeydew", "Iceberg lettuce", "Jackfruit"]

# Add the items to the listbox
for item in items:
    listbox.insert(tk.END, item)


# Create a function to search for the input value in the list of items
def search(value):
    # Clear the listbox
    listbox.delete(0, tk.END)

    # Loop through the items
    for item in items:
        # Check if the input value is a substring of the item
        if value.lower() in item.lower():
            # Add the item to the listbox
            listbox.insert(tk.END, item)


# Create a function to handle the selection of an item from the listbox
def select(event):
    # Get the index of the selected item
    index = listbox.curselection()[0]

    # Get the value of the selected item
    value = listbox.get(index)

    # Update the entry value with the selected item
    input_var.set(value)


# Bind the select function to the double-click event on the listbox
listbox.bind("<Double-Button-1>", select)

# Run the main loop
root.mainloop()
