from tkinter import *
from tkinter import messagebox
import random as rd
import pyperclip
import json
FONT = ("Times New Roman", 10, "bold")
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p' 
           'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', "A", "B", "C", "D", "E", "F",
           "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R"
           "S", "T", "U", "V", "W", "X", "Y", "Z"]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_list = [rd.choice(letters) for _ in range(0, (rd.randint(8, 10)))]
    password_list.extend(str(rd.choice(numbers)) for _ in range(0, (rd.randint(2, 4))))
    password_list.extend(rd.choice(special_characters) for _ in range(0, (rd.randint(2, 4))))
    rd.shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(END, f"{password}")
    pyperclip.copy(password)
    messagebox.showinfo(message="Your password has been saved to clipboard")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    if website_entry.get() != "" and password_entry.get() != "":
        is_ok = messagebox.askokcancel(title=website_entry.get(), message=f"Email:{email_entry.get()}\n"
                                                                          f"Password: {password_entry.get()}\n"
                                                                          f"is this ok?")
        if is_ok == True:
            new_data = {website_entry.get().lower():
                            {"email": email_entry.get(),
                             "password": password_entry.get()}}
            try:
                with open("websites_passwords.json", mode="r") as password_file:
                    data = json.load(password_file)
                    data.update(new_data)
            except FileNotFoundError:
                with open("websites_passwords.json", "w") as password_file:
                    json.dump(new_data, password_file, indent=4)
            except json.decoder.JSONDecodeError:
                with open("websites_passwords.json", "w") as password_file:
                    json.dump(new_data, password_file, indent=4)
            else:
                with open("websites_passwords.json", "w") as password_file:
                    json.dump(data, password_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
    else:
        messagebox.showerror(title="Error message", message="You must fill all fields")

def find_password():
    try:
        with open("websites_passwords.json", "r") as passwords_file:
            data = json.load(passwords_file)
    except FileNotFoundError:
        messagebox.showinfo(message="This file does not exist")
    except json.decoder.JSONDecodeError:
        messagebox.showinfo(title="Error", message="There are no details saved in the database")
    else:
        if website_entry.get().lower() not in data:
            messagebox.showerror(title="Error", message="This websites details are not saved in the database")
        else:
            messagebox.showinfo(title="details", message=f"email: {data[website_entry.get().lower()]['email']}\n"
                                                         f"password: {data[website_entry.get().lower()]['password']}")
# ---------------------------- UI SETUP ------------------------------- #
# window
window = Tk()
window.title("Password manager")
window.config(pady=70, padx=70, background="white")

# canvas
canvas = Canvas(height=200, width=200, background="white", highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image = logo)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:", font=FONT, background="white")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:", font=FONT, background="white")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:", font=FONT , background="white")
password_label.grid(column=0, row=3)


# Entries
website_entry = Entry(width=32,  background="white")
website_entry.focus()
website_entry.grid(column=1, row=1)

email_entry = Entry(width=50, background="white")
email_entry.insert(END, "blaizemuna@gmail.com")
email_entry.grid(column=1, row=2,columnspan=2)

password_entry = Entry(width=32, background="white")
password_entry.grid(column=1, row=3)


# Buttons
pass_generator_button = Button(text="Generate password", width=14, background="white", command=generate_password)
pass_generator_button.grid(column=2, row=3)

add_button = Button(text="Add",width=43, background="white", highlightthickness=0, command=add_password)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="search", width=14, command=find_password, background="white")
search_button.grid(column=2, row=1)
window.mainloop()