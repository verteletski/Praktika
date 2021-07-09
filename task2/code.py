from tkinter import *
import tkinter as tk
import math
from tkinter import messagebox
root = Tk()
# Задаємо розміри вікна
root.geometry('310x400')
root.title('Calculator Verteletski')
root['bg']='black'
# Функція натискання на клавіші, зроблено для того, щоб можна було вводити дані в калькулятор задопомогою клавіатури
def press_key(event):
    print(repr(event.char))
    if event.char.isdigit() :
        Number(event.char)
    elif event.char in '+-*/':
        Operations(event.char)
    elif event.char == '\r':
        calculate()
root.bind('<Key>', press_key)
# Це функція яка записує числа на екран
def Number(num):
    Numb=A.get()
    if Numb[0]=='0' and len(Numb)==1:
        Numb=Numb[1:]
    A['state']= tk.NORMAL
    A.delete(0,tk.END)
    A.insert(0,Numb+num)
    A['state']= tk.DISABLED
# Функція знаходження логарифму з основою 2.
def Log():
    Numb=A.get()
    x=float(Numb)
    Numb=math.log2(x)
    A['state']= tk.NORMAL
    A.delete(0,tk.END)
    A.insert(0,Numb)
    A['state']= tk.DISABLED
# Функція знаходження логарифму з основою 10.
def Ln():
    Numb=A.get()
    x=float(Numb)
    Numb=math.log10(x)
    A['state']= tk.NORMAL
    A.delete(0,tk.END)
    A.insert(0,Numb)
    A['state']= tk.DISABLED
# Функція знаходження сінуса ( для обчислення потрібно щоб число було в радіанах, і до натискання кнопки на екрані )
def Sinus():
    Numb=A.get()
    x=float(Numb)
    Numb=math.sin(x)
    A['state']= tk.NORMAL
    A.delete(0,tk.END)
    A.insert(0,Numb)
    A['state']= tk.DISABLED
# Функція знаходження косінуса ( для обчислення потрібно щоб число було в радіанах, і до натискання кнопки на екрані )
def Cosinus():
    Numb=A.get()
    x=float(Numb)
    Numb=math.cos(x)
    A['state']= tk.NORMAL
    A.delete(0,tk.END)
    A.insert(0,Numb)
    A['state']= tk.DISABLED
# Функція знаходження тангенса ( для обчислення потрібно щоб число було в радіанах, і до натискання кнопки на екрані )
def tgs():
    Numb=A.get()
    x=float(Numb)
    Numb=math.tan(x)
    A['state']= tk.NORMAL
    A.delete(0,tk.END)
    A.insert(0,Numb)
    A['state']= tk.DISABLED
# Функція знаходження котангенса ( для обчислення потрібно щоб число було в радіанах, і до натискання кнопки на екрані )
def ctgs():
    Numb=A.get()
    x=float(Numb)
    Numb=math.cos(x)/math.sin(x)
    A['state']= tk.NORMAL
    A.delete(0,tk.END)
    A.insert(0,Numb)
    A['state']= tk.DISABLED
# Це функція яка записує операції на екран, такі як + - * / % .
def Operations(op):
    Operator=A.get()
    if Operator[-1] in '+-*/%':
        Operator = Operator[:-1]
    elif '+' in Operator or '-' in Operator or '*' in Operator or '/' in Operator:
        calculate()
        Operator=A.get()
    A['state']= tk.NORMAL
    A.delete(0,tk.END)
    A.insert(0,Operator+op)
    A['state']= tk.DISABLED
# Функція, яка рахує, після натискання =, або якщо після однієї операції, замість = поставити іншу операцію, наприклад -, то вона спочатку порахує, а потім запише ту операцію
def calculate():
    Numb=A.get()
    if Numb[-1] in '+-*/':
        Numb = Numb+Numb[:-1]
    A['state']= tk.NORMAL
    A.delete(0,tk.END)
    try:
        A.insert(0,eval(Numb))
    except (NameError,SyntaxError):
        messagebox.showinfo('Warning','Need to input only numbers!')
        A.insert(0,0)
    except ZeroDivisionError:
        messagebox.showinfo('Warning','You trying to /0!!')
        A.insert(0,0)
    A['state']= tk.DISABLED
# Функція очистки екрану
def clear():
    A['state']= tk.NORMAL
    A.delete(0,tk.END)
    A.insert(0,'0')
    A['state']= tk.DISABLED
# Функція, яка видаляє останнє число
def delete():
    Numb=A.get()
    Numb = Numb[:-1]
    if len(Numb)==0 :
        Numb='0'
    A['state']= tk.NORMAL
    A.delete(0,tk.END)
    A.insert(0,Numb)
    A['state']= tk.DISABLED
# Функція, яка переводить число з екрану в 2їчну систему числення (+2 балли)
def TranslateIn2():
    Numb = A.get()
    b = ''
    n=int(Numb)
    while n > 0 :
            b = str(n % 2) + b
            n = n // 2
    A['state']= tk.NORMAL
    A.delete(0,tk.END)
    A.insert(0,b)
    A['state']= tk.DISABLED
# Тут йдуть функції натискання клавіш, які викликають вище названі функції
def DeleteButton(op):
    return tk.Button(font=('Arial',15),text=op,command=delete)

def NumButtons(num):
    return tk.Button(font=('Arial',15),text=num,command=lambda : Number(num),bd=5)

def OperationButtons(op):
    return tk.Button(font=('Arial',15),text=op,command=lambda : Operations(op),bd=5)

def CalculateButton(op):
    return tk.Button(font=('Arial',15),text=op,command=calculate)

def ClearButton(op):
    return tk.Button(font=('Arial',15),text=op,command=clear)

def SinButton(op):
    return tk.Button(font=('Arial',15),text=op,command=Sinus,bd=5)

def CosButton(op):
    return tk.Button(font=('Arial',15),text=op,command=Cosinus,bd=5)

def TgButton(op):
    return tk.Button(font=('Arial',15),text=op,command=tgs,bd=5)

def CtgButton(op):
    return tk.Button(font=('Arial',15),text=op,command=ctgs,bd=5)

def LogButton(op):
    return tk.Button(font=('Arial',15),text=op,command=Log,bd=5)

def LnButton(op):
    return tk.Button(font=('Arial',15),text=op,command=Ln,bd=5)

def perevodB2(op):
    return tk.Button(font=('Arial',15),text=op,command=TranslateIn2,bd=5)
# Це перший рядок
A=tk.Entry(root,font=('Arial',18),width=15)
A.insert(0,'0')
# Відключили це вікно вводу, але потім, коли щось натискаємо воно розблоковується і записує, після чого знову блочиться
A['state']= tk.DISABLED
# Розстягнення в ширину
A.grid(row=0,column=0,columnspan=6,stick='we',padx=5)
# Назначення клавіш 0-9
NumButtons('1').grid(row = 2,column = 2,stick='wens',padx=5,pady=5)
NumButtons('2').grid(row = 2,column = 3,stick='wens',padx=5,pady=5)
NumButtons('3').grid(row = 2,column = 4,stick='wens',padx=5,pady=5)
NumButtons('4').grid(row = 3,column = 2,stick='wens',padx=5,pady=5)
NumButtons('5').grid(row = 3,column = 3,stick='wens',padx=5,pady=5)
NumButtons('6').grid(row = 3,column = 4,stick='wens',padx=5,pady=5)
NumButtons('7').grid(row = 4,column = 2,stick='wens',padx=5,pady=5)
NumButtons('8').grid(row = 4,column = 3,stick='wens',padx=5,pady=5)
NumButtons('9').grid(row = 4,column = 4,stick='wens',padx=5,pady=5)
NumButtons('0').grid(row = 5,column = 3,stick='wens',padx=5,pady=5)
# Назначення клавіш "+ - * / %"
OperationButtons('+').grid(row = 4,column = 5,stick='wens',padx=5,pady=5)
OperationButtons('-').grid(row = 3,column = 5,stick='wens',padx=5,pady=5)
OperationButtons('*').grid(row = 2,column = 5,stick='wens',padx=5,pady=5)
OperationButtons('/').grid(row = 1,column = 5,stick='wens',padx=5,pady=5)
OperationButtons('%').grid(row = 2,column = 1,stick='wens',padx=5,pady=5)
# Назначення клавіш = , С, DEL
CalculateButton('=').grid(row = 5,column = 5,stick='wens',padx=5,pady=5)
ClearButton('C').grid(row = 5,column = 4,stick='wens',padx=5,pady=5)
DeleteButton('DEL').grid(row = 5,column = 2,stick='wens',padx=5,pady=5)
# Назначення клавіш sin, cos, tg, ctg
SinButton('sin').grid(row = 1,column = 1,stick='wens',padx=5,pady=5)
CosButton('cos').grid(row = 1,column = 2,stick='wens',padx=5,pady=5)
TgButton('tg').grid(row = 1,column = 3,stick='wens',padx=5,pady=5)
CtgButton('ctg').grid(row = 1,column = 4,stick='wens',padx=5,pady=5)
# Назначення клавіш log, ln
LogButton('log').grid(row = 3,column = 1,stick='wens',padx=5,pady=5)
LnButton('ln').grid(row = 4,column = 1,stick='wens',padx=5,pady=5)
# Назначення клавіши переводу в 2їчну систему числення
perevodB2('B 2').grid(row = 5,column = 1,stick='wens',padx=5,pady=5)
# Розміри клавіш
root.grid_columnconfigure(1,minsize=60)
root.grid_columnconfigure(2,minsize=60)
root.grid_columnconfigure(3,minsize=60)
root.grid_columnconfigure(4,minsize=60)
root.grid_columnconfigure(5,minsize=60)

root.grid_rowconfigure(1,minsize=60)
root.grid_rowconfigure(2,minsize=60)
root.grid_rowconfigure(3,minsize=60)
root.grid_rowconfigure(4,minsize=60)
root.grid_rowconfigure(5,minsize=60)

root.mainloop()