import tkinter as tk
from tkinter import messagebox
from password_generator import RandomPassword
import pyperclip

FONT = ("arial", 10, "bold")
BG_COLOR = "#D6E4E5"
ENTRY_COLOR = "#EFF5F5"
LABEL_COLOR = "#EB6440"
BUTTON_COLOR = "#497174"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    rd_pass = RandomPassword()
    random_password = rd_pass.generate()
    password_entry.delete(0, tk.END)
    password_entry.insert(0, random_password)
    pyperclip.copy(random_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    # ensure no blank entries
    if len(website) == 0:
        messagebox.showinfo(title="Alert", message=f"Please don't leave the website empty!")
    elif len(username) == 0:
        messagebox.showinfo(title="Alert", message=f"Please don't leave the username empty!")
    elif len(password) == 0:
        messagebox.showinfo(title="Alert", message=f"Please don't leave the password empty!")
    else:
        # confirmation pop-up
        is_ok = messagebox.askokcancel(title="Login Confirmation", message=f"Website:    {website}\nUsername: {username}\n"
                                                      f"Password:  {password}\n\nIs it okay to save?")

        if is_ok:
            with open("password-manager.txt", mode="a") as file:
                file.writelines(f"{website}, {username}, {password}\n")
                website_entry.delete(0, tk.END)
                username_entry.delete(0, tk.END)
                username_entry.insert(0, "kylewong00@gmail.com")
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
website_entry = tk.Entry(width=57, bg=ENTRY_COLOR)
website_entry.grid(column=1, row=1, columnspan=2, sticky=tk.W)
website_entry.focus()

username_entry = tk.Entry(width=57, bg=ENTRY_COLOR)
username_entry.insert(0, "kyrie@gmail.com")
username_entry.grid(column=1, row=2, columnspan=2, sticky=tk.W)

password_entry = tk.Entry(width=44, bg=ENTRY_COLOR)
password_entry.grid(column=1, row=3, columnspan=2, sticky=tk.W)

# buttons
generate_button = tk.Button(text="Generate", command=generate, font=FONT,bg=BG_COLOR, fg=LABEL_COLOR)
generate_button.grid(column=2, row=3, sticky=tk.E)

add_button = tk.Button(text="Add", width=42, command=save_password, font=FONT, bg=LABEL_COLOR, fg=BG_COLOR)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()