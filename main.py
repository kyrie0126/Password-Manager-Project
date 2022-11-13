import tkinter as tk
from tkinter import messagebox
from password_generator import RandomPassword
import pyperclip
import json

FONT = ("arial", 10, "bold")
BG_COLOR = "#D6E4E5"
ENTRY_COLOR = "#EFF5F5"
LABEL_COLOR = "#EB6440"
BUTTON_COLOR = "#497174"


# ---------------------------- SEARCH LOGINS ------------------------------- #
def search():
    """Returns user/pass for website. If website login or json file DNE, return messagebox alert."""
    website = website_entry.get().title()
    try:
        with open("password-manager.json", mode="r") as data_file:
            data = json.load(data_file)
            username = data[website]["username"]
            password = data[website]["password"]
    except KeyError:
        messagebox.showinfo(title="Alert", message=f"No login for {website}")
    except FileNotFoundError:
        messagebox.showinfo(title="Alert", message=f"No logins exist")
    else:
        messagebox.showinfo(title=f"{website} Info:", message=f"Username: {username}\nPassword: {password}")
    finally:
        website_entry.delete(0, tk.END)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    rd_pass = RandomPassword()
    random_password = rd_pass.generate()
    password_entry.delete(0, tk.END)
    password_entry.insert(0, random_password)
    pyperclip.copy(random_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get().title()
    username = username_entry.get()
    password = password_entry.get()
    # prep for json export
    new_data = {
        website: {
            "username": username,
            "password": password
        }
    }

    # ensure no blank entries
    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Alert", message="Please don't leave any box empty!")
    else:
        try:
            with open("password-manager.json", mode="r") as data_file:
                # Read old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("password-manager.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Update with new data
            data.update(new_data)
            with open("password-manager.json", mode="w") as data_file:
                # Save updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, tk.END)
            username_entry.delete(0, tk.END)
            username_entry.insert(0, "test_email@gmail.com")
            password_entry.delete(0, tk.END)


# ---------------------------- UI SETUP ------------------------------- #
# window
window = tk.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg=BG_COLOR)

# background image
canvas = tk.Canvas(width=220, height=200, bg=BG_COLOR, highlightthickness=0)
lock_img = tk.PhotoImage(file="logo.png")
canvas.create_image(110, 100, image=lock_img)
canvas.grid(column=1, row=0)

# labels
website_label = tk.Label(text="Website:", fg=LABEL_COLOR, bg=BG_COLOR, font=FONT)
website_label.grid(column=0, row=1, sticky=tk.E)

username_label = tk.Label(text="Email / Username:", fg=LABEL_COLOR, bg=BG_COLOR, font=FONT)
username_label.grid(column=0, row=2, sticky=tk.E)

password_label = tk.Label(text="Password:", fg=LABEL_COLOR, bg=BG_COLOR, font=FONT)
password_label.grid(column=0, row=3, sticky=tk.E)

# text entry
website_entry = tk.Entry(width=44, bg=ENTRY_COLOR)
website_entry.grid(column=1, row=1, columnspan=2, sticky=tk.W)
website_entry.focus()

username_entry = tk.Entry(width=57, bg=ENTRY_COLOR)
username_entry.insert(0, "kylewong@gmail.com")
username_entry.grid(column=1, row=2, columnspan=2, sticky=tk.W)

password_entry = tk.Entry(width=44, bg=ENTRY_COLOR)
password_entry.grid(column=1, row=3, columnspan=2, sticky=tk.W)

# buttons
generate_button = tk.Button(text="Generate", width=8, command=generate, font=FONT, bg=BG_COLOR, fg=LABEL_COLOR)
generate_button.grid(column=2, row=3, sticky=tk.E)

add_button = tk.Button(text="Add", width=42, command=save_password, font=FONT, bg=LABEL_COLOR, fg=BG_COLOR)
add_button.grid(column=1, row=4, columnspan=2)

search_button = tk.Button(text="Search", width=8, command=search, font=FONT, bg=BG_COLOR, fg=LABEL_COLOR)
search_button.grid(column=2, row=1, sticky=tk.E)


window.mainloop()
