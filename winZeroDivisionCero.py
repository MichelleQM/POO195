import tkinter as tk
from tkinter import messagebox, Tk, Label
from ZeroDivisionCero import *

#Ventana para dividir

def Division():
    ventana = Tk()
    ventana.title("ZeroDivisionError")
    ventana.geometry("400x200")

    label = tk.Label(ventana, text="Ingrese dos números para dividir")
    label.pack() 

    tk.Label(ventana, text="Primer numero:").pack()
    entry_num1= tk.Entry(ventana)
    entry_num1.pack()

    tk.Label(ventana, text="Segundo numero:").pack()
    entry_num2 = tk.Entry(ventana)
    entry_num2.pack()

    def handle_division():
        try:
            num1 = float(entry_num1.get())
            num2 = float(entry_num2.get())
            calculator = DivisionCalculator(num1, num2)
            resultado = calculator.dividir()
            messagebox.showinfo("Resultado", f"El resultado de la división es: {resultado}")
        except ValueError:
            messagebox.showerror("ZeroDivisionError", "Por favor, ingrese números válidos.")
        except ZeroDivisionError as error:
            messagebox.showerror("Error", str(error))

    button = tk.Button(ventana, text="Dividir", command=handle_division)
    button.pack()

    ventana.mainloop()

Division()
