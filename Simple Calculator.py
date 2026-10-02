import tkinter as tk
import winsound
import threading

window=tk.Tk()
window.title("Simple Calculator")
window.geometry("320x500")
window.config(bg="#1a1a1a")
window.iconbitmap("Calculator.ico")

count=0

def beep():
    winsound.Beep(3000,30)

def press(value):
    threading.Thread(target=beep).start()
    Display=display.get()
    if Display=="0":
        display.delete(0, tk.END)
        display.insert(tk.END, value)
    else:
        display.insert(tk.END, value)

def number_button(n):
    button=tk.Button(window, text=n, font=("Arial",18), bg="#242424", fg="white",
                     command=lambda:press(n), relief="flat", bd=0)
    m=(n-1)//3+4
    button.grid(row=m, column=(n-1)%3, padx=3, pady=3, sticky="nsew")

def calculate():
    threading.Thread(target=beep).start()
    global count
    count+=1
    if count>=5:
        from tkinter import messagebox
        messagebox.showinfo("Upgrade Required", "Pay to continue using?")
    else:
        Display=display.get()
        Display=Display.replace("÷","/")
        Display=Display.replace("×","*")
        Display=Display.replace("^","**")
        display.delete(0, tk.END)
        display.insert(tk.END, eval(Display))        

def clear_all():
    threading.Thread(target=beep).start()
    display.delete(0, tk.END)

def Clear():
    threading.Thread(target=beep).start()
    Display=display.get()
    Display=Display[:-1]
    display.delete(0, tk.END)
    display.insert(tk.END, Display)

def percent():
    threading.Thread(target=beep).start()
    Display=display.get()
    plus_pos=Display.rfind("+")
    minus_pos=Display.rfind("-")
    times_pos=Display.rfind("×")
    divide_pos=Display.rfind("÷")
    last_op_pos=max(plus_pos, minus_pos, times_pos, divide_pos)
    Percent=float(Display[last_op_pos+1:])
    Percent=str(Percent/100)
    Display=Display[:last_op_pos+1]
    display.delete(0, tk.END)
    display.insert(tk.END, Display)
    display.insert(tk.END, Percent)

for i in range(1,10):
    number_button(i)

display=tk.Entry(window, font=("Arial",20), justify="right", bg="#1a1a1a", fg="white",
                 relief="flat", bd=0, highlightthickness=0)
display.grid(row=0, column=0,rowspan=3, columnspan=4, padx=10, pady=10, sticky="nsew")

plus=tk.Button(window, text="+", font=("Arial",18), bg="#343434", fg="white",
               command=lambda: press("+"), relief="flat", bd=0)
plus.grid(row=4, column=3, padx=3, pady=3, sticky="nsew")

minus=tk.Button(window, text="-", font=("Arial",18), bg="#343434", fg="white",
                command=lambda: press("-"), relief="flat", bd=0)
minus.grid(row=5, column=3, padx=3, pady=3, sticky="nsew")

saltire=tk.Button(window, text="×", font=("Arial",18), bg="#343434", fg="white",
                  command=lambda: press("×"), relief="flat", bd=0)
saltire.grid(row=6, column=3, padx=3, pady=3, sticky="nsew")

solidus=tk.Button(window, text="÷", font=("Arial",18), bg="#343434", fg="white",
                  command=lambda: press("÷"), relief="flat", bd=0)
solidus.grid(row=7, column=3, padx=3, pady=3, sticky="nsew")

zero=tk.Button(window, text="0", font=("Arial",18), bg="#242424", fg="white",
               command=lambda: press("0"), relief="flat", bd=0)
zero.grid(row=7, column=0, columnspan=2, padx=3, pady=3, sticky="nsew")

equals=tk.Button(window, text="=", font=("Arial",18), bg="#2ECC9A", fg="white",
                 command=lambda: calculate(), relief="flat", bd=0)
equals.grid(row=7, column=2, padx=3, pady=3, sticky="nsew")

clearall=tk.Button(window, text="AC", font=("Arial",18), bg="#343434", fg="white",
                   command=lambda: clear_all(), relief="flat", bd=0)
clearall.grid(row=3, column=2, padx=3, pady=3, sticky="nsew")

clear=tk.Button(window, text="C", font=("Arial",18), bg="#343434", fg="white",
                command=lambda: Clear(), relief="flat", bd=0)
clear.grid(row=3, column=3, padx=3, pady=3, sticky="nsew")

percentage=tk.Button(window, text="%", font=("Arial",18), bg="#343434", fg="white",
                     command=lambda: percent(), relief="flat", bd=0)
percentage.grid(row=3, column=0, padx=3, pady=3, sticky="nsew")

power=tk.Button(window, text="^", font=("Arial",18), bg="#343434", fg="white",
               command=lambda: press("^"), relief="flat", bd=0)
power.grid(row=3, column=1, padx=3, pady=3, sticky="nsew")

for col in range(5):
    window.grid_columnconfigure(col, weight=1)

for row in range(8):
    window.grid_rowconfigure(row, weight=1)

window.mainloop()
