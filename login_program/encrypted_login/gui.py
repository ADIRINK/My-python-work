if __name__ == '__main__':

    import customtkinter
    from cryptography.fernet import Fernet

    root = customtkinter.CTk()
    root.geometry("500x420")
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")
    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)
    label1 = customtkinter.CTkLabel(master=frame, text="Enter your credentials", font=("Dialog", 12))
    label1.pack(pady=12, padx=10)
    label = customtkinter.CTkLabel(master=frame, text="Login System", font=("Dialog", 24))
    label.pack(pady=12, padx=10)
    entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
    entry1.pack(pady=12, padx=10)
    entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
    entry2.pack(pady=12, padx=10)
    checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember me")
    checkbox.pack(pady=12, padx=6)

    def write_key():
        master_key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(master_key)
            print("Key created!")

    def load_key():
        label1.configure(text="Opening file...")
        file = open("key.key", "rb")
        passkey = file.read()
        label1.configure(text="Loading key...")
        file.close()
        return passkey

    key = load_key()
    fer = Fernet(key)

    def login():
        label1.configure(text="Checking login...")
        username = entry1.get()
        label1.configure(text="Checking password...")
        password = entry2.get()
        if view(username, password):
            label1.configure(text="Login successful")
        else:
            label1.configure(text="Invalid username or password")

    def register():
        user_list = []
        label1.configure(text="Checking login...")
        username = entry1.get()
        label1.configure(text="Checking password...")
        password = entry2.get()
        label1.configure(text="Opening file...")
        with open('password.txt', 'r') as f:
            for line in f:
                name, password = line.strip().split('|')
                user_list.append(name)
            if username in user_list:
                label1.configure(text="Username already taken!")
            else:
                with open('password.txt', 'a') as r:
                    label1.configure(text="Writing...")
                    r.write(username + "|" + fer.encrypt(password.encode()).decode() + "\n")
                    label1.configure(text="Saving...")

    button = customtkinter.CTkButton(master=frame, text="Login", command=login)
    button.pack(pady=12, padx=6)

    button1 = customtkinter.CTkButton(master=frame, text="Register", command=register)
    button1.pack(pady=6, padx=10)

    def view(user, password):
        label1.configure(text="Opening file...")
        print("OpenFile")
        with open('password.txt', 'r') as f:
            label1.configure(text="Reading file...")
            print("ReadFile")
            for line in f.readlines():
                user_data, password_data = line.strip().split('|')
                label1.configure(text="Stripping data...")
                print("StripData")
                password_data = fer.decrypt(password_data.encode()).decode().strip()
                print(user, password + "\n" + user_data, password_data)
                if user == user_data and password == password_data:
                    label1.configure(text="Success!")
                    print("FileOpen")
                    return True
                else:
                    print("FIleOpenFail")
        return False

    root.mainloop()
