import tkinter as tk

def filter_data(event):
    # Get the search query from the entry field
    search_query = entry.get().lower()

    # Clear the listbox
    listbox.delete(0, tk.END)

    # Filter and display matching items
    for item in data:
        if search_query in item.lower():
            listbox.insert(tk.END, item)

# Sample data
data = ['Apple', 'Banana', 'Cherry', 'Date', 'Fig', 'Grapes', 'Lemon']

# Create the main window
root = tk.Tk()
root.title('Search Filter')

# Create an entry field for search
entry = tk.Entry(root)
entry.pack(pady=10)
entry.bind('<KeyRelease>', filter_data)

# Create a listbox to display filtered results
listbox = tk.Listbox(root)
listbox.pack()

# Initialize the listbox with all data
for item in data:
    listbox.insert(tk.END, item)

root.mainloop()