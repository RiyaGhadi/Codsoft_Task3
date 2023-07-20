import random
import string
from tkinter import *


def generate_password():
    length = int(length_entry.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''
    for i in range(length):
        password = password + random.choice(characters)

    password_label.configure(text="Generated Password: " + password,font=("Arial", 30))

root = Tk()
root.title("Password Generator")


main_label = Label(root, text="Password Generator",font=("Arial", 50, "bold","underline"), background="Blue",foreground="White")
main_label.pack(fill=BOTH)

name_label = Label(root, text="Enter Your Name :",font=("Arial", 30))
name_label.pack()

name_entry = Entry(root,font=("Arial", 20))
name_entry.pack()

length_label = Label(root, text="Password Length:",font=("Arial", 30))
length_label.pack()

length_entry = Entry(root,font=("Arial", 20))
length_entry.pack()

generate_button = Button(root, text="Generate", command=generate_password)
generate_button.pack()

password_label = Label(root, text="Generated Password:", font=("Arial",30))
password_label.pack()

root.mainloop()
