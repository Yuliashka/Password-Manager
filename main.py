
# https://tkdocs.com/tutorial/widgets.html#entry
from tkinter import*
# we need to import the message box to use it:
# messagebox is not a class. it is another module of code:
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # WE CAN USE COMPREHENSION:
    # we generate a range between 0 and nr_letters number - 1
    # password_letters = [random.choice(letters) for item in range(nr_letters)]
    password_letters = [random.choice(letters) for item in range(nr_letters)]
    password_numbers = [random.choice(numbers) for item in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for item in range(nr_symbols)]
    password_list = password_symbols + password_letters + password_numbers
    random.shuffle(password_list)

    # we can create a string join all elements from our list using join()method:
    # the "" we are using to have nothing between joined symbols, but we can use anything, like "%"
    password = "".join(password_list)
    print(password)

    # we add our password to our entry:
    entry3.insert(0, f"{password}")
    # to have the password already copied from out interface we can use this python module:
    pyperclip.copy(password)

# # OR WE CAN USE A FOR LOOP:
# password_list = []
# for char in range(nr_letters):
#   password_list.append(random.choice(letters))
#
# for char in range(nr_symbols):
#   password_list.append(random.choice(symbols))
#
# for char in range(nr_numbers):
#   password_list.append(random.choice(numbers))
#
# random.shuffle(password_list)

# password = ""
# for char in password_list:
#   password += char
#
# print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    # to show our messagebox use method:
    if len(entry1.get()) == 0 or len(entry2.get()) == 0 or len(entry3.get()) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any field empty!")
    else:
        is_ok = messagebox.askokcancel(title=entry1.get(), message=f"These are the details entered: \n Email: {entry2.get()} \n "
        f"Password: {entry3.get()} \n Is it ok to save?")

        # if customer is saying: ok and our is_ok == True:
        if is_ok:
            with open("data.txt", mode="a") as file:
                file.write(f"{entry1.get()} | {entry2.get()} | {entry3.get()} \n")
                # to clean the entry after we pushed the Add button
                entry1.delete(0, END)
                entry3.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #
# CREATING WINDOW:
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


# CREATING CANVAS:
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# CREATING LABELS:
# LABEL1:
label1 = Label(text="Website: ")
label1.grid(column=0, row=1)

# LABEL2:
label2 = Label(text="Email/Username: ")
label2.grid(column=0, row=2)

# LABEL3:
label3 = Label(text="Password: ")
label3.grid(column=0, row=3)

# CREATING ENTRIES:
# ENTRY1 (website):
entry1 = Entry(width=52)
# to focus the cursor at our particular entry:
entry1.focus()
# we use attribute columnspan to prolong our widget for 2 columns:
entry1.grid(column=1, row=1, columnspan=2)

# ENTRY2 (email):
entry2 = Entry(width=52)
# we use a method to have some text already inserted into an entry
# we can use 0 - means we want to insert from the beginning of the entry
# we can use END - to insert a text in the end of some existing text in the entry
entry2.insert(0, "laramera@outlook.it")
# we use attribute columnspan to prolong our widget for 2 columns:
entry2.grid(column=1, row=2, columnspan=2)

# ENTRY3 (password):
entry3 = Entry(width=33)
entry3.grid(column=1, row=3)

# CREATING BUTTONS:
# BUTTON1:
button1 = Button(text="Generate Password", command=generate_password)
button1.grid(column=2, row=3)

# BUTTON2:
button2 = Button(text="Add", width=30, command=save_data)
button2.grid(column=1, row=4, columnspan=2)



window.mainloop()