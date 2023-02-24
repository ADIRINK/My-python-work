import psutil
import customtkinter
import sys

def program():
    root = customtkinter.CTk()
    root.title("CPU and Memory usage")
    root.minsize(200, 200)
    root.maxsize(200, 200)
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")
    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=20, fill="both", expand=True)
    label = customtkinter.CTkLabel(master=frame, text="CPU 0%", font=("Dialog", 24))
    label.pack(pady=12)
    label1 = customtkinter.CTkLabel(master=frame, text="RAM 0%", font=("Dialog", 24))
    label1.pack(pady=12)
    def exit_program():
        sys.exit()
    button1 = customtkinter.CTkButton(master=frame, text="Quit ", command=exit_program)
    button1.pack(pady=12)

    def update():
        cpu_usage = psutil.cpu_percent()
        ram_usage = psutil.virtual_memory().percent

        if cpu_usage == 20 or cpu_usage < 20 or cpu_usage == 0:
            label.configure(text_color="white", text="CPU " + str(cpu_usage) + "%")
        elif cpu_usage == 21 or cpu_usage < 40 or cpu_usage == 40:
            label.configure(text_color="yellow", text="CPU " + str(cpu_usage) + "%")
        elif cpu_usage == 41 or cpu_usage < 65 or cpu_usage == 65:
            label.configure(text_color="orange", text="CPU " + str(cpu_usage) + "%")
        elif cpu_usage == 66 or cpu_usage < 100 or cpu_usage == 100:
            label.configure(text_color="red", text="CPU " + str(cpu_usage) + "%")

        if ram_usage == 20 or ram_usage < 20 or ram_usage == 0:
            label1.configure(text_color="white", text="RAM " + str(ram_usage) + "%")
        elif ram_usage == 21 or ram_usage < 40 or ram_usage == 40:
            label1.configure(text_color="yellow", text="RAM " + str(ram_usage) + "%")
        elif ram_usage == 41 or ram_usage < 65 or ram_usage == 65:
            label1.configure(text_color="orange", text="RAM " + str(ram_usage) + "%")
        elif ram_usage == 66 or ram_usage < 100 or ram_usage == 100:
            label1.configure(text_color="red", text="RAM " + str(ram_usage) + "%")

        if not root.winfo_exists():
            return

        root.after(500, update)

    update()
    root.mainloop()

while True:
    program()
