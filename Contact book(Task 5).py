from tkinter import *
from tkinter import ttk

def save_contact():
    name = name_entry.get()
    phone_number = phone_entry.get()

    if name and phone_number:
        names.append(name)
        phone_numbers.append(phone_number)
        update_display()
        clear_entries()

def update_display():
    display_text.config(state=NORMAL)
    display_text.delete(1.0, END)

    for i in range(len(names)):
        display_text.insert(END, f"{names[i]:<20}\t\t{phone_numbers[i]:<15}\n")

    display_text.config(state=DISABLED)

def clear_entries():
    name_entry.delete(0, END)
    phone_entry.delete(0, END)

def search_contact(event=None):
    search_term = search_entry.get()
    search_result_text.set("Search result:\n")

    if search_term:
        if search_term in names:
            index = names.index(search_term)
            phone_number = phone_numbers[index]
            search_result_text.set(f"Name: {search_term}, Phone Number: {phone_number}")
        else:
            search_result_text.set("Name Not Found")
    else:
        search_result_text.set("Enter a search term")


root = Tk()
root.title("Contact Management System")
root.geometry("600x500")  

style = ttk.Style()
style.configure("TButton", padding=5, font=('Arial', 10))
style.configure("TLabel", padding=5, font=('Arial', 12))
style.configure("TEntry", padding=5, font=('Arial', 12))

names = []
phone_numbers = []


ttk.Label(root, text="Name:", style="TLabel").grid(row=0, column=0, padx=10, pady=5, sticky=E)
name_entry = ttk.Entry(root, style="TEntry")
name_entry.grid(row=0, column=1, padx=10, pady=5)

ttk.Label(root, text="Phone Number:", style="TLabel").grid(row=1, column=0, padx=10, pady=5, sticky=E)
phone_entry = ttk.Entry(root, style="TEntry")
phone_entry.grid(row=1, column=1, padx=10, pady=5)


ttk.Button(root, text="Save Contact", command=save_contact, style="TButton").grid(row=2, column=0, columnspan=2, pady=10)
search_button = ttk.Button(root, text="Search Contact", command=search_contact, style="TButton")
search_button.grid(row=3, column=0, columnspan=2, pady=10)


display_text = Text(root, height=10, width=50, state=DISABLED)
display_text.grid(row=4, column=0, columnspan=2, pady=10)


search_result_text = StringVar()
search_result_label = ttk.Label(root, textvariable=search_result_text, style="TLabel")
search_result_label.grid(row=5, column=0, columnspan=2, pady=5)


ttk.Label(root, text="Enter search term:", style="TLabel").grid(row=6, column=0, padx=10, pady=5, sticky=E)
search_entry = ttk.Entry(root, style="TEntry")
search_entry.grid(row=6, column=1, padx=10, pady=5)


search_entry.bind("<Return>", lambda event=None: search_contact())


root.mainloop()
