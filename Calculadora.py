import tkinter as tk
from tkinter import ttk
from tkinter import messagebox




def main():
    def calculator(num1, num2, operator):
        if operator == '+':
            if type(num1) == float or type(num2) == float:
                result = num1 + num2
            else:
                result = int(num1 + num2)
        elif operator == '-':
            if type(num1) == float or type(num2) == float:
                result = num1 - num2
            else:
                result = int(num1 - num2)
        elif operator == '*':
            if type(num1) == float or type(num2) == float:
                result = num1 * num2
            else:
                result = int(num1 * num2)
        elif operator == '/':
            result = round(num1 / num2, 2)
        else:
            result = num1 ** num2
        return result


    def radio():
        if actual.get() == 1:
            window.config(bg = "black")
            label_entrada1.config(bg = "black", fg = "white")
            label_entrada2.config(bg = "black", fg = "white")
            label_operator.config(bg = "black", fg = "white")
            label.config(bg = "black", fg = "white")
            label_hola.config(bg = "black", fg = "white")
            label_resultado.config(bg = "black", fg = "white")


        elif actual.get() == 2:
            window.config(bg = "lightgray")
            label_entrada1.config(bg = "lightgray", fg = "black")
            label_entrada2.config(bg = "lightgray", fg = "black")
            label_operator.config(bg = "lightgray", fg = "black")
            label.config(bg = "lightgray", fg = "black")
            label_hola.config(bg = "lightgray", fg = "black")
            label_resultado.config(bg = "lightgray", fg = "black")


    def ventana():
        messagebox.showinfo('Valor Inválido', 'Por favor ingrese un número')


    def click_calculate():
    
    
        num1 = entrada1.get()
        num2 = entrada2.get()
        operator = combo_operators.get()

        while len(num1) == 0 or len(num2) == 0:
            ventana()
            window.destroy()
            main()
    
        
        if float(num1) - int(float(num1)) != 0:
            valor1 = float(num1)
        else:
            valor1 = int(num1)
        if float(num2) - int(float(num2)) != 0:
            valor2 = float(num2)
        else:
            valor2 = int(num2)
        res = calculator(valor1, valor2, operator)
        label_resultado.configure(text='Result:' + str(res))


    def hola1(label):
        label.configure(text="NOOOOO")
    window = tk.Tk()
    window.title("Just A Calculator")
    window.geometry("400x400")
    window.config(cursor='pirate')
    label = tk.Label(window, text="Calculator", font=('Arial bold', 15))
    label.grid(column=0, row=0)
    entrada1 = tk.Entry(window, width=10)
    entrada2 = tk.Entry(window, width=10)
    entrada1.grid(column=1, row=1)
    entrada2.grid(column=1, row=2)
    label_entrada1 = tk.Label(window, text="Input 1st number:", font=('Arial bold', 10))
    label_entrada1.grid(column=0, row=1)
    label_entrada2 = tk.Label(window, text="Input 2nd number:", font=('Arial bold', 10))
    label_entrada2.grid(column=0, row=2)
    label_operator = tk.Label(window, text="Choose an operator", font=('Arial bold', 10))
    label_operator.grid(column=0, row=3)
    combo_operators = ttk.Combobox(window)
    combo_operators['values'] = ["+", '-', '*', '/', 'pow']
    combo_operators.current(0)
    combo_operators.grid(column=1, row=3)
    label_resultado = tk.Label(window, text="Result:", font=('Arial bold', 15))
    label_resultado.grid(column=0, row=5)
    label_hola = tk.Label(window, text="Qué no", font=("Arial bold", 16))
    label_hola.grid(column=1, row=6)
    window.config(bg = "lightgray")
    label_entrada1.config(bg = "lightgray", fg = "black")
    label_entrada2.config(bg = "lightgray", fg = "black")
    label_operator.config(bg = "lightgray", fg = "black")
    label.config(bg = "lightgray", fg = "black")
    label_hola.config(bg = "lightgray", fg = "black")
    label_resultado.config(bg = "lightgray", fg = "black")
    button = tk.Button(window,
                        command=lambda: click_calculate(
                            ),
                        text='Calculate',
                        bg="purple",
                        fg="white")
    button.grid(column=1, row=4)
    button2 = tk.Button(window,
                        text="NO",
                        bg="gray",
                        fg='white',
                        font=('Arial bold', 10),
                        command=lambda: hola1(label_hola))
    button2.grid(column=2, row=4)
    actual = tk.IntVar()
    radio_black = ttk.Radiobutton(window, text="Modo Oscuro", variable=actual, value=1, command=radio)
    radio_white = ttk.Radiobutton(window, text="Modo Claro", variable=actual, value=2, command=radio)
    radio_black.grid(column="3", row='0')
    radio_white.grid(column="3", row='1')
    window.config(bg = "lightgray")

    window.mainloop()

main()