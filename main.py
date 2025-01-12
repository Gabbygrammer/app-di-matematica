import os
import subprocess
import sys
import time
import tkinter
from tkinter import Tk, Label, Button, Entry, Scrollbar, Toplevel

root_extractor_path = ""
function_calculator_path = ""
testing = False

if testing:
    root_extractor_path = "./math-root-extractor.exe"
    function_calculator_path = "./math-function-calculator.exe"
else:
    root_extractor_path = os.path.join(sys._MEIPASS, "math-root-extractor.exe")
    function_calculator_path = os.path.join(sys._MEIPASS, "math-function-calculator.exe")

# if not os.path.exists(f"{os.getenv("LOCALAPPDATA")}\\app-mate"):
#     os.mkdir(f"{os.getenv('LOCALAPPDATA')}\\app-mate")

def extract_root(window):
    number = root_input_field.get()
    root_input_field.delete(0, 'end')
    process = subprocess.run(f"{root_extractor_path} {number}", capture_output=True, text=True)
    if process.returncode == 0:
        rootResultField.configure(text=process.stdout)
        rootResultField.pack()

        try:
            root.after(500, window.lift)
            root.after(500, window.focus_set)
        except:
            pass
        
def estrattore_di_radici():
    window = Toplevel()
    window.title("Estrattore di radici")
    window.resizable(False, False)
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width / 2) - (300 / 2)
    y = (screen_height / 2) - (300 / 2)
    window.geometry(f"300x300+{int(x)}+{int(y)}")

    title = Label(window, text="Estrattore di radici")
    title.configure(font=("Arial", 11, "bold"))
    title.pack()

    information = Label(window, text="Inserisci la radice di un numero intero (solo il numero):")
    information.configure(font=("Arial", 8))
    information.pack()

    global root_input_field
    root_input_field = Entry(window)
    root_input_field.pack()

    extractButton = Button(window, text="Estrai", command=lambda wind=window: extract_root(wind))
    extractButton.pack()

    global rootResultField
    rootResultField = Label(window, text="")

    window.mainloop()

def calcola_funzione(window):
    time_start = time.time()
    expression = function_input_field.get()
    function_input_field.delete(0, 'end')
    x = expression.split("=")[0].strip().replace("f(", "").replace(")", "")
    result = eval(expression.split("=")[1].strip().replace("x", x))
    function_result_field.configure(text=f"Il risultato è: {result}")
    function_result_field.pack()
    duration = time.time() - time_start
    duration = round(duration, 2)
    calculation_duration.configure(text=f"Eseguito in {duration} secondi")
    calculation_duration.pack()
    
    try:
        root.after(500, window.lift)
        root.after(500, window.focus_set)
    except:
        pass

def calcolatore_di_funzioni():
    window = Toplevel()
    window.title("Calcolatore di funzioni")
    window.resizable(False, False)
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width / 2) - (300 / 2)
    y = (screen_height / 2) - (300 / 2)
    window.geometry(f"300x300+{int(x)}+{int(y)}")

    title = Label(window, text="Calcolatore di funzioni")
    title.configure(font=("Arial", 10, "bold"))
    title.pack()

    information = Label(window, text="Inserisci una funzione f con il valore di x tra parentesi:")
    information.configure(font=("Arial", 8))
    information.pack()

    example = Label(window, text="Esempio: f(3) = x * 2 [quindi x = 3]")
    example.configure(font=("Arial", 9))
    example.pack()

    global function_input_field
    function_input_field = Entry(window)
    function_input_field.pack(side=tkinter.TOP, pady=(10, 0), fill=tkinter.X)

    scrollbar = Scrollbar(window, orient=tkinter.HORIZONTAL, command=function_input_field.xview)
    scrollbar.pack(side=tkinter.TOP, fill=tkinter.X, pady=(0, 10))

    function_input_field.configure(xscrollcommand=scrollbar.set)

    calculateButton = Button(window, text="Calcola", command=lambda: calcola_funzione(window=window))
    calculateButton.pack()

    global calculation_duration
    calculation_duration = Label(window, text="")

    global function_result_field
    function_result_field = Label(window, text="")

    window.mainloop()

root = Tk()
root.title("Programma matematico da Gabri")
root.resizable(False, False)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (300 / 2)
y = (screen_height / 2) - (300 / 2)
root.geometry(f"300x300+{int(x)}+{int(y)}")

title = Label(root, text="Benvenuto al mio programma matematico!")
title.configure(font=("Arial", 11, "bold"))
title.pack()

choose = Label(root, text="Scegli una delle seguenti opzioni:")
choose.configure(font=("Arial", 9))
choose.pack()

choice1 = Button(root, text="Estrattore di radici", command=estrattore_di_radici)
choice1.pack()

choice2 = Button(root, text="Calcolatore di funzioni", command=calcolatore_di_funzioni)
choice2.pack()

root.mainloop()