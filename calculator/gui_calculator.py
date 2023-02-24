import customtkinter as ctk

calculation = ""


def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(0, "end")
    text_result.insert(0, calculation)


def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(0, "end")
        text_result.insert(0, calculation)
    except:
        clear_field()
        text_result.insert(0, "Error")


def clear_field():
    global calculation
    calculation = ""
    text_result.delete(0, "end")


root = ctk.CTk()
root.geometry("320x450")
root.title("Py-culator")

text_result = ctk.CTkTextbox(root, state="disabled", height=50, width=320, font=("Arial", 24))
text_result.grid(columnspan=5)

btn_1 = ctk.CTkButton(root, text="1", command=lambda: add_to_calculation(1), width=80, height=80, font=("Ariel", 24))
btn_1.grid(row=2, column=1)
btn_2 = ctk.CTkButton(root, text="2", command=lambda: add_to_calculation(2), width=80, height=80, font=("Ariel", 24))
btn_2.grid(row=2, column=2)
btn_3 = ctk.CTkButton(root, text="3", command=lambda: add_to_calculation(3), width=80, height=80, font=("Ariel", 24))
btn_3.grid(row=2, column=3)
btn_4 = ctk.CTkButton(root, text="4", command=lambda: add_to_calculation(4), width=80, height=80, font=("Ariel", 24))
btn_4.grid(row=3, column=1)
btn_5 = ctk.CTkButton(root, text="5", command=lambda: add_to_calculation(5), width=80, height=80, font=("Ariel", 24))
btn_5.grid(row=3, column=2)
btn_6 = ctk.CTkButton(root, text="6", command=lambda: add_to_calculation(6), width=80, height=80, font=("Ariel", 24))
btn_6.grid(row=3, column=3)
btn_7 = ctk.CTkButton(root, text="7", command=lambda: add_to_calculation(7), width=80, height=80, font=("Ariel", 24))
btn_7.grid(row=4, column=1)
btn_8 = ctk.CTkButton(root, text="8", command=lambda: add_to_calculation(8), width=80, height=80, font=("Ariel", 24))
btn_8.grid(row=4, column=2)
btn_9 = ctk.CTkButton(root, text="9", command=lambda: add_to_calculation(9), width=80, height=80, font=("Ariel", 24))
btn_9.grid(row=4, column=3)
btn_0 = ctk.CTkButton(root, text="0", command=lambda: add_to_calculation(0), width=80, height=80, font=("Ariel", 24))
btn_0.grid(row=5, column=2)
btn_plus = ctk.CTkButton(root, text="+", command=lambda: add_to_calculation("+"), width=80, height=80, font=("Ariel", 24))
btn_plus.grid(row=2, column=4)
btn_minus = ctk.CTkButton(root, text="-", command=lambda: add_to_calculation("-"), width=80, height=80, font=("Ariel", 24))
btn_minus.grid(row=3, column=4)
btn_mul = ctk.CTkButton(root, text="*", command=lambda: add_to_calculation("*"), width=80, height=80, font=("Ariel", 24))
btn_mul.grid(row=4, column=4)
btn_div = ctk.CTkButton(root, text="/", command=lambda: add_to_calculation("/"), width=80, height=80, font=("Ariel", 24))
btn_div.grid(row=5, column=4)
btn_open = ctk.CTkButton(root, text="(", command=lambda: add_to_calculation("("), width=80, height=80, font=("Ariel", 24))
btn_open.grid(row=5, column=1)
btn_close = ctk.CTkButton(root, text=")", command=lambda: add_to_calculation(")"), width=80, height=80, font=("Ariel", 24))
btn_close.grid(row=5, column=3)
btn_equals = ctk.CTkButton(root, text="=", command=evaluate_calculation, width=160, height=80, font=("Ariel", 24))
btn_equals.grid(row=6, column=3, columnspan =2)
btn_clear = ctk.CTkButton(root, text="C", command=clear_field, width=160, height=80, font=("Ariel", 24))
btn_clear.grid(row=6, column=1, columnspan =2)
root.mainloop()
