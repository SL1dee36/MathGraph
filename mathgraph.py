import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import webbrowser
from getpass import getuser
import urllib.request
import sys,os

def open_link(event):
    webbrowser.open("https://t.me/Slide36")

def on_closing():
    root.destroy()
    exit()

help_math = r'''
    [?]    Примеры формул:

    [1]    sin(x) | arcsin(x)
    [2]    cos(x) | arccos(x)
    [3]    tan(x) | arctan(x)
    [4]    sum(x) 
    [5]    exp(-x**3)
    [6]    log(x)
    [7]    ln(x)
    [8]    sqrt(x)
    [9]    power(x, n)
    [10]   abs(x)
    [11]   round(x)
    [12]   floor(x)
    [13]   ceil(x)

    [+]    И др..  
    можете изучить библиотеку NumPy 
    для более подробного разбора
'''


def update_plot():
    formula = input_entry.get()
    try:
        x = np.linspace(-10, 10, 400)
        y = eval(formula, {'__builtins__': None}, {'x': x, 'np': np, 'sin': np.sin, 'cos': np.cos, 
                                                   'tan': np.tan, 'pi': np.pi, 'sqrt': np.sqrt, 'arctan': np.arctan, 'arcsin': np.arcsin, 
                                                   'arccos': np.arccos, 'exp': np.exp, 'abs': np.absolute, 'round': np.round, 
                                                   'floor': np.floor, 'ceil': np.ceil, 'sum': np.sum, 'log': np.log, 'ln': np.log10, 'power': np.power})

        plot_ax.clear()
        plot_ax.plot(x, y)
        plot_canvas.draw()

        error_label.pack_forget()
    except Exception as e:
        print(e)
        plot_ax.clear()
        plot_canvas.draw()
        error_label.pack()

root = tk.Tk()
vername='MathGraph v14.9b'
root.title("MathGraph v14.9b")

try:
    root.iconbitmap(default="calculus.ico")
except:
    try:
        url = 'https://www.dropbox.com/scl/fi/9vme49q8zo6cahyu2v9cu/calculus.ico?rlkey=vwkckz49btdf0wg74bxosjc8d&dl=1'
        try:
            save_path = "C:/Users/{}/AppData/Local/Temp".format(getuser())
            urllib.request.urlretrieve(url, save_path)
            try:
                root.iconbitmap(default="C:/Users/{}/AppData/Local/Temp/calculus.ico".format(getuser()))
            except:
                root.title(f"{vername} > ошибка: Продуцируемая иконка не найдена!")
                pass
        except:
            root.title(f"{vername} > ошибка: Мы не смогли найти путь до папки temp")
            pass
    except:
        root.title(f"{vername} > ошибка: Мы не смогли подключиться к интернету, для обновления!")

root.geometry("1200x600")
root.wm_minsize(1200, 600)
root.protocol("WM_DELETE_WINDOW", on_closing)
#root.resizable(False, False)

left_frame = tk.Frame(root)
left_frame.pack(side="left")

input_label = tk.Label(left_frame, text="Введите формулу:", font=("consolas", 12))
input_label.pack(pady=10)

input_entry = tk.Entry(left_frame, font=("consolas", 12), width=40)
input_entry.pack()
input_entry.configure(justify="center")

hints_label = tk.Label(left_frame, text="Подсказки интересных формул:", font=("consolas", 12))
hints_label.pack(pady=10)

hints_text = tk.Text(left_frame, height=10, width=40, font=("consolas", 12))
hints_text.pack()
hints_text.insert(tk.END, f"{help_math}")

right_frame = tk.Frame(root)
right_frame.pack(side="right")

error_label = tk.Label(right_frame, text="Ошибка в формуле", font=("consolas", 12), fg="red")
error_label.pack(pady=10)
error_label.pack_forget()

figure = plt.figure(figsize=(8, 6))
plot_ax = figure.add_subplot(1, 1, 1)
plot_canvas = FigureCanvasTkAgg(figure, master=right_frame)
plot_canvas.get_tk_widget().pack()

update_button = tk.Button(left_frame, text="Обновить", font=("consolas", 12), command=update_plot, relief='flat')
update_button.pack(pady=10)

feedback_btn = tk.Label(left_frame, text="feedback", fg="#0064ff", cursor="hand2", width=13, font=("consolas", 12))
feedback_btn.pack(pady=50)
feedback_btn.bind("<Button-1>", open_link)


root.mainloop()