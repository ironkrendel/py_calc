from tkinter import *
import math
import tkinter

def press_0():
    if out.cget("text") == "0":
        pass
    else:
        out.config(text=out.cget("text")+'0')
        
def press_1():
    if out.cget("text") == "0":
        out.config(text="1")
    else:
        out.config(text=out.cget("text")+'1')
        
def press_2():
    if out.cget("text") == "0":
        out.config(text="2")
    else:
        out.config(text=out.cget("text")+'2')
        
def press_3():
    if out.cget("text") == "0":
        out.config(text="3")
    else:
        out.config(text=out.cget("text")+'3')
        
def press_4():
    if out.cget("text") == "0":
        out.config(text="4")
    else:
        out.config(text=out.cget("text")+'4')
        
def press_5():
    if out.cget("text") == "0":
        out.config(text="5")
    else:
        out.config(text=out.cget("text")+'5')
        
def press_6():
    if out.cget("text") == "0":
        out.config(text="6")
    else:
        out.config(text=out.cget("text")+'6')
        
def press_7():
    if out.cget("text") == "0":
        out.config(text="7")
    else:
        out.config(text=out.cget("text")+'7')
        
def press_8():
    if out.cget("text") == "0":
        out.config(text="8")
    else:
        out.config(text=out.cget("text")+'8')
        
def press_9():
    if out.cget("text") == "0":
        out.config(text="9")
    else:
        out.config(text=out.cget("text")+'9')
        
def press_plus():
    if out.cget("text") == "0":
        pass
    elif out.cget("text")[-1] == "+" or out.cget("text")[-1] == "-" or out.cget("text")[-1] == "/" or out.cget("text")[-1] == "*":
        pass
    else:
        out.config(text=out.cget("text")+'+')
        
def press_minus():
    if out.cget("text") == "0":
        pass
    elif out.cget("text")[-1] == "+" or out.cget("text")[-1] == "-" or out.cget("text")[-1] == "/" or out.cget("text")[-1] == "*":
        pass
    else:
        out.config(text=out.cget("text")+'-')
        
def press_mult():
    if out.cget("text") == "0":
        pass
    elif out.cget("text")[-1] == "+" or out.cget("text")[-1] == "-" or out.cget("text")[-1] == "/" or out.cget("text")[-1] == "*":
        pass
    else:
        out.config(text=out.cget("text")+'*')
        
def press_divide():
    if out.cget("text") == "0":
        pass
    elif out.cget("text")[-1] == "+" or out.cget("text")[-1] == "-" or out.cget("text")[-1] == "/" or out.cget("text")[-1] == "*":
        pass
    else:
        out.config(text=out.cget("text")+'/')
        
def press_sqrt():
    if "+" in out.cget("text") or "-" in out.cget("text") or "/" in out.cget("text") or "*" in out.cget("text"):
        pass
    else:
        res = math.sqrt(float(out.cget("text")))
        if res - int(res) == 0:
            out.config(text=str(int(res)))
        else:
            out.config(text=str(res))
        
    
def press_power():
    if "+" in out.cget("text") or "-" in out.cget("text") or "/" in out.cget("text") or "*" in out.cget("text"):
        pass
    else:
        res = float(out.cget("text")) * float(out.cget("text"))
        if res - int(res) == 0:
            out.config(text=str(int(res)))
        else:
            out.config(text=str(res))
        
def press_switch():
    num = 0
    digits = []
    step_op = "*"
    step = 10
    for i in str(out.cget("text")):
        if i.isdigit() == True:
            if int(i) == 0:
                if step_op == "*":
                    num = num * 10
                else:
                    step = step * 10
                    pass
            else:
                if step_op == "*":
                    num = num * 10
                    num += int(i)
                else:
                    num += int(i) / step
                    step = step * 10
        elif i == ".":
            step_op = "/"
        else:
            digits.append(num)
            step_op = "*"
            if i == "+":
                digits.append("+")
            elif i == "-":
                digits.append("-")
            elif i == "*":
                digits.append("*")
            elif i == "/":
                digits.append("/")
            num = 0
    digits.append(num)
    if len(digits) == 1:
        if digits[0] > 0:
            out.config(text="-"+out.cget("text"))
        else:
            pass
    elif out.cget("text")[0] == "-" and len(digits) == 3:
        out.config(text=out.cget("text")[1::])
        

def press_dot():
    if out.cget("text")[-1] == "." or out.cget("text")[-1] == "+" or out.cget("text")[-1] == "-" or out.cget("text")[-1] == "/" or out.cget("text")[-1] == "*":
        pass
    else:
        num = 0
        digits = []
        step_op = "*"
        step = 10
        for i in str(out.cget("text")):
            if i.isdigit() == True:
                if int(i) == 0:
                    if step_op == "*":
                        num = num * 10
                    else:
                        step = step * 10
                        pass
                else:
                    if step_op == "*":
                        num = num * 10
                        num += int(i)
                    else:
                        num += int(i) / step
                        step = step * 10
            elif i == ".":
                step_op = "/"
            else:
                digits.append(num)
                step_op = "*"
                if i == "+":
                    digits.append("+")
                elif i == "-":
                    digits.append("-")
                elif i == "*":
                    digits.append("*")
                elif i == "/":
                    digits.append("/")
                num = 0
        digits.append(num)
        if "." in str(digits[-1]):
            pass
        else:
            out.config(text=out.cget("text")+".")
        
def delete_num():
    if out.cget("text")[0:-1:] == "":
        out.config(text="0")
    else:
        out.config(text=out.cget("text")[0:-1:])
        
def press_enter():
    num = 0
    digits = []
    step_op = "*"
    step = 10
    for i in str(out.cget("text")):
        if i.isdigit() == True:
            if int(i) == 0:
                if step_op == "*":
                    num = num * 10
                else:
                    step = step * 10
                    pass
            else:
                if step_op == "*":
                    num = num * 10
                    num += int(i)
                else:
                    num += int(i) / step
                    step = step * 10
        elif i == ".":
            step_op = "/"
        else:
            digits.append(num)
            step_op = "*"
            step = 10
            if i == "+":
                digits.append("+")
            elif i == "-":
                digits.append("-")
            elif i == "*":
                digits.append("*")
            elif i == "/":
                digits.append("/")
            num = 0
    digits.append(num)
    fin = 0
    if "+" not in digits and "-" not in digits and "/" not in digits and "*" not in digits:
        fin = float(out.cget("text"))
    else:
        if "*" in digits or "/" in digits:
            while True:
                indices = [i for i, x in enumerate(digits) if x == "*" or x == "/"]
                if indices == []:
                    break
                num1 = digits[indices[0] - 1]
                num2 = digits[indices[0] + 1]
                op = digits[indices[0]]
                if op == "/":
                    res = num1 / num2
                elif op == "*":
                    res = num1 * num2
                digits.pop(indices[0] - 1)
                digits.pop(indices[0])
                digits[indices[0] - 1] = float(res)
            fin += digits[0]
            i = 1
            while i < len(digits):
                if digits[i] == "+":
                    i += 1
                    fin += digits[i]
                elif digits[i] == "-":
                    i += 1
                    fin -= digits[i]
                elif digits[i] == "/":
                    i += 1
                    fin -= fin / digits[i]
                elif digits[i] == "*":
                    i += 1
                    fin = fin * digits[i]
                i += 1
        else:
            fin += digits[0]
            i = 1
            while i < len(digits):
                if digits[i] == "+":
                    i += 1
                    fin += digits[i]
                elif digits[i] == "-":
                    i += 1
                    fin -= digits[i]
                elif digits[i] == "/":
                    i += 1
                    fin -= fin / digits[i]
                elif digits[i] == "*":
                    i += 1
                    fin = fin * digits[i]
                i += 1
    if fin - int(fin) == 0:
        out.config(text=str(int(fin)))
    else:
        out.config(text=str(fin))
            

def resizing():
    if len(out.cget("text")) > 11:
        if 40-len(out.cget("text")) < 8:
            pass
        else:
            out.config(font=("Arial Bold", 40-len(out.cget("text"))))
    else:
        out.config(font=("Arial Bold", 40))
    window.after(10, resizing)
            
        
    
btn_width = 5
btn_height = 2
btn_spacing = 20
btn_font_size = 15

window = Tk()
window.title("Calculator")
window.geometry('360x520')
window.resizable(width=0, height=0)
out_Frame = tkinter.Frame(window, width=320, height=65)
out_Frame.grid(column=0, row=0, padx=(20,20), pady=(20,5), sticky="w")
out_Frame.pack_propagate(0)
out = Label(out_Frame, text="0", font=("Arial Bold", 40), height=1)
out.grid(column=0, row=0, padx=(20,20), pady=(20,5), sticky="w")
out.pack(expand=True)
btn_divide = Button(window, text="/", width=btn_width, height=btn_height, font=("Arial Bold", btn_font_size), command=press_divide)
btn_divide.grid(column=0, row=1, padx=(20,btn_spacing), pady=(10,10), sticky="w")
btn_mult = Button(window, text="*", width=btn_width, height=btn_height, font=("Arial Bold", btn_font_size), command=press_mult)
btn_mult.grid(column=0, row=1, padx=(85 + btn_spacing,btn_spacing), pady=(10,10), sticky="w")
btn_minus = Button(window, text="-", width=btn_width, height=btn_height, font=("Arial Bold", btn_font_size), command=press_minus)
btn_minus.grid(column=0, row=1, padx=(170 + btn_spacing,btn_spacing), pady=(10,10), sticky="w")
btn_plus = Button(window, text="+", width=btn_width, height=btn_height, font=("Arial Bold", btn_font_size), command=press_plus)
btn_plus.grid(column=0, row=1, padx=(255 + btn_spacing,btn_spacing), pady=(10,10), sticky="w")
btn_7 = Button(window, text="7", width=btn_width, height=btn_height, font=("Arial Bold", btn_font_size), command=press_7)
btn_7.grid(column=0, row=2, padx=(20,btn_spacing), pady=(10,10), sticky="w")
btn_8 = Button(window, text="8", width=btn_width, height=btn_height, font=("Arial Bold", btn_font_size), command=press_8)
btn_8.grid(column=0, row=2, padx=(85 + btn_spacing,btn_spacing), pady=(10,10), sticky="w")
btn_9 = Button(window, text="9", width=btn_width, height=btn_height, font=("Arial Bold", btn_font_size), command=press_9)
btn_9.grid(column=0, row=2, padx=(170 + btn_spacing,btn_spacing), pady=(10,10), sticky="w")
btn_switch = Button(window, text="+/-", width=btn_width, height=btn_height, font=("Arial Bold", btn_font_size), command=press_switch)
btn_switch.grid(column=0, row=2, padx=(255 + btn_spacing,btn_spacing), pady=(10,10), sticky="w")
btn_4 = Button(window, text="4", width=btn_width, height=btn_height, font=("Arial Bold", btn_font_size), command=press_4)
btn_4.grid(column=0, row=3, padx=(20,btn_spacing), pady=(10,10), sticky="w")
btn_5 = Button(window, text="5", width=btn_width, height=btn_height, font=("Arial Bold", btn_font_size), command=press_5)
btn_5.grid(column=0, row=3, padx=(85 + btn_spacing,btn_spacing), pady=(10,10), sticky="w")
btn_6 = Button(window, text="6", width=btn_width, height=btn_height, font=("Arial Bold", btn_font_size), command=press_6)
btn_6.grid(column=0, row=3, padx=(170 + btn_spacing,btn_spacing), pady=(10,10), sticky="w")
btn_sqrt = Button(window, text="sqrt", width=btn_width, height=btn_height, font=("Arial Bold", btn_font_size), command=press_sqrt)
btn_sqrt.grid(column=0, row=3, padx=(255 + btn_spacing,btn_spacing), pady=(10,10), sticky="w")
btn_1 = Button(window, text="1", width=btn_width, height=btn_height, font=("Arial Bold", btn_font_size), command=press_1)
btn_1.grid(column=0, row=4, padx=(20,btn_spacing), pady=(10,10), sticky="w")
btn_2 = Button(window, text="2", width=btn_width, height=btn_height, font=("Arial Bold", btn_font_size), command=press_2)
btn_2.grid(column=0, row=4, padx=(85 + btn_spacing,btn_spacing), pady=(10,10), sticky="w")
btn_3 = Button(window, text="3", width=btn_width, height=btn_height, font=("Arial Bold", btn_font_size), command=press_3)
btn_3.grid(column=0, row=4, padx=(170 + btn_spacing,btn_spacing), pady=(10,10), sticky="w")
btn_power = Button(window, text="power", width=btn_width, height=btn_height, font=("Arial Bold", btn_font_size), command=press_power)
btn_power.grid(column=0, row=4, padx=(255 + btn_spacing,btn_spacing), pady=(10,10), sticky="w")
btn_dot = Button(window, text=".", width=btn_width, height=btn_height, font=("Arial Bold", btn_font_size), command=press_dot)
btn_dot.grid(column=0, row=5, padx=(20,btn_spacing), pady=(10,10), sticky="w")
btn_0 = Button(window, text="0", width=btn_width, height=btn_height, font=("Arial Bold", btn_font_size), command=press_0)
btn_0.grid(column=0, row=5, padx=(85 + btn_spacing,btn_spacing), pady=(10,10), sticky="w")
btn_enter = Button(window, text="=", width=btn_width, height=btn_height, font=("Arial Bold", btn_font_size), command=press_enter)
btn_enter.grid(column=0, row=5, padx=(170 + btn_spacing,btn_spacing), pady=(10,10), sticky="w")
btn_del = Button(window, text="del", width=btn_width, height=btn_height, font=("Arial Bold", btn_font_size), command=delete_num)
btn_del.grid(column=0, row=5, padx=(255 + btn_spacing,btn_spacing), pady=(10,10), sticky="w")
window.after(10, resizing)
window.mainloop()