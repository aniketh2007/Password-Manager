# Importing modules
from tkinter import *
from tkinter import messagebox
from random import choice, randint,shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    password_letters = [choice(letters) for _ in range(8, 10)]
    password_symbols = [choice(symbols) for _ in range(2, 4)]
    password_numbers = [choice(numbers) for _ in range(2, 4)]
    
    password_list = password_letters + password_symbols + password_numbers
    
    password = "".join(password_list)
    password_entry.insert(index=0,string=password)
    pyperclip.copy(password)
    
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data ={
        website: {
            "email": email,
            "password" : password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops",message="Make sure no fields are kept empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json","r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No data found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=f"{website}",message=f"Email:{email}\n Password:{password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for the {website} exists")

        
# ---------------------------- UI SETUP ------------------------------- #
# Window Creation
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)


#Canvas Creation and importing image onto the screen
canvas = Canvas(width=200,height=200,highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=1,row=0)

#Labels
#Website 
website_label = Label(text="Website:")
website_label.grid(column=0,row=1)


#Email
email_label = Label(text="Email/Username:")
email_label.grid(column=0,row=2)

#Password 
password_label = Label(text="Password:")
password_label.grid(column=0,row=3)

#Entry files
#Website_entry
website_entry = Entry(width=40)
website_entry.grid(column=1,row=1)
website_entry.focus()

#Email Entry 
email_entry = Entry(width=50)
email_entry.grid(column=1,row=2,columnspan=2)
email_entry.insert(index=0,string="anikethh7@gmail.com")

#Password Entry
password_entry = Entry(width=50)
password_entry.grid(column=1,row=3,columnspan=2)

#Buttons

#Generate Button
generate_button = Button(text="Generate Button",command=generate_password)
generate_button.grid(column=2,row=3,columnspan=2)

#Add Button
add_button = Button(text="Add",width=36,command=save)
add_button.grid(column=1,row=4,columnspan=2)

#Search button
search_button = Button(text="Search",width=12,command=find_password)
search_button.grid(column=2,row=1,columnspan=2)


window.mainloop()