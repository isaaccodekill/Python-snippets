#
# Name : Bello isaac imoleayo
# Matric Number : 170805024
# Department : Computer science
#

from tkinter import *
import math


class ScientificCalculator():

    def __init__(self):
        self.total = 0
        self.current = ""
        self.new_num = True
        self.op_pending = False
        self.op = ""
        self.eq = False


    
    def display(self, value):
        text_box.delete(0, END)
        text_box.insert(0, value)

    def do_sum(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "minus":
            self.total -= self.current
        if self.op == "times":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        if self.op == "power":
            v = math.pow(self.total,self.current)
            self.total = v
        if self.op == "log":
            v = math.log(self.total,self.current)
            self.total = v
        self.new_num = True
        self.op_pending = False
        self.display(self.total)

    def num_press(self, num):
        self.eq = False
        temp = text_box.get()
        temp2 = str(num)
        if self.new_num:
            self.current = temp2
            self.new_num = False
        else:
            if temp2 == '.':
                if temp2 in temp:
                    return
            self.current = temp + temp2
        self.display(self.current)

    def calc_total(self):
        self.eq = True
        self.current = float(self.current)
        if self.op_pending == True:
            self.do_sum()
        else:
            self.total = float(text_box.get())


    def operation(self, op):
        self.current = float(self.current)
        if self.op_pending:
            self.do_sum()
        elif not self.eq:
            self.total = self.current
        self.new_num = True
        self.op_pending = True
        self.op = op
        self.eq = False

    def cancelBtn(self):
        self.eq = False
        self.current = "0"
        self.display(0)
        self.new_num = True

    def all_cancelBtn(self):
        self.cancel()
        self.total = 0

    def signBtn(self):
        self.eq = False
        self.current = -(float(text_box.get()))
        self.display(self.current)    

    def const_eBtn(self):
        self.eq = False
        self.current = math.e
        self.display(self.current)

    def const_piBtn(self):
        self.eq = False
        self.current = math.pi
        self.display(self.current)

    def sinBtn(self):
        v = float(text_box.get())
        v*=(math.pi/180)
        self.current = math.sin(v)
        self.display(self.current)


    def cosBtn(self):
        v = float(text_box.get())
        v*=(math.pi/180)
        self.current = math.cos(v)
        self.display(self.current)

    def tanBtn(self):
        v = float(text_box.get())
        v*=(math.pi/180)
        self.current = math.tan(v)
        self.display(self.current)

    def sinhBtn(self):
        v = float(text_box.get())
        v*=(math.pi/180)
        self.current = math.sinh(v)
        self.display(self.current)

    def coshBtn(self):
        v = float(text_box.get())
        v*=(math.pi/180)
        self.current = math.cosh(v)
        self.display(self.current)

    def tanhBtn(self):
        v = float(text_box.get())
        v*=(math.pi/180)
        self.current = math.tanh(v)
        self.display(self.current)
		
    def factBtn(self):
        f = float(text_box.get())
        self.current = math.factorial(f)
        self.display(self.current)

    def sqrtBtn(self):
        f = float(text_box.get())
        self.current = math.sqrt(f)
        self.display(self.current)

    def lnBtn(self):
        f = float(text_box.get())
        self.current = math.log(f)
        self.display(self.current)

    def logBtn(self):
        f = float(text_box.get())
        self.current = math.log10(f)
        self.display(self.current)

    def expoBtn(self):
        f = float(text_box.get())
        self.current = math.exp(f)
        self.display(self.current)

    def x2Btn(self):
        f = float(text_box.get())
        self.current = f**2
        self.display(self.current)
	
    def sinInverseBtn(self):
        v = float(text_box.get())
        self.current = math.asin(v)
        self.current = math.degrees(self.current)
        self.display(self.current)

    def cosInverseBtn(self):
        v = float(text_box.get())
        self.current = math.acos(v)
        self.current = math.degrees(self.current)
        self.display(self.current)
        
    def tanInverseBtn(self):
        v = float(text_box.get())
        self.current = math.atan(v)
        self.current = math.degrees(self.current)
        self.display(self.current)
		






# Create the GUI models
window = Tk()
window.title("Isaac Bello's calculator")
windowFrame = Frame(window);
calculator = ScientificCalculator()
windowFrame.grid()

# creating labels


text_box = Entry(windowFrame, bd=5, width= 30, font=74 , justify = "right", relief = SUNKEN)
text_box.grid(row = 0, column = 0, columnspan = 8, pady = 20)
text_box.insert(0, "0")

# Generating the number buttons
numbersBtn = "123456789"
i = 0
button = []
for j in range(1,4):
    for k in range(3):
        button.append(Button(windowFrame, bd=4, width = 4, font = 18, text = numbersBtn[i] ))
        button[i].grid(row = j, column = k)
        button[i]["command"] = lambda x = numbersBtn[i]: calculator.num_press(x)
        i += 1


zerobutton= Button(windowFrame, bd=4,  font = 28, width = 14, text = " 0 ")
zerobutton["command"] = lambda: calculator.num_press(0)
zerobutton.grid(row = 4, column = 0, columnspan = 2, padx=16, pady=16)

#The basic Arithmetic operator Buttons
button_div = Button(windowFrame, width = 4,  font = 28,  bd=4, text = chr(247))
button_div["command"] = lambda: calculator.operation("divide")
button_div.grid(row = 1, column = 3,padx=16, pady=16)

button_mult = Button(windowFrame, width = 4,  font = 28,  bd=4,text = " x ")
button_mult["command"] = lambda: calculator.operation("times")
button_mult.grid(row = 2, column = 3,padx=16, pady=16)

minus = Button(windowFrame, width = 4, bd=4, font = 28, text = " - ")
minus["command"] = lambda: calculator.operation("minus")
minus.grid(row = 3, column = 3,padx=16, pady=16)

point = Button(windowFrame, width = 4, bd=4, font = 1000,  text = " . ")
point["command"] = lambda: calculator.num_press(".")
point.grid(row = 5, column = 2,padx=16, pady=16)

add = Button(windowFrame, width = 4, bd=4,  font = 28,  text = " + ")
add["command"] = lambda: calculator.operation("add")
add.grid(row = 4, column = 3,padx=16, pady=16)

signBtn = Button(windowFrame,bd=4, width = 4, font = 18,  text = "-(x)")
signBtn["command"] = calculator.signBtn
signBtn.grid(row = 5, column = 5,padx=16, pady=16)

equals = Button(windowFrame, width = 4, bd=4, font = 48, text = " = ")
equals["command"] = calculator.calc_total
equals.grid(row = 4, column = 2, padx=16, pady=16)









#Memory operations
clear = Button(windowFrame,bd=4, width = 4, font = 18,  text = "  C  ", bg="cyan")
clear["command"] = calculator.cancelBtn
clear.grid(row = 5, column = 0,padx=16, pady=16)

all_clear = Button(windowFrame,bd=4, width = 4, font = 18,  text = " AC", bg = "cyan")
all_clear["command"] = calculator.all_cancelBtn
all_clear.grid(row = 5, column = 1,padx=16, pady=16)


#Trigonometric Operator buttons
sinButton= Button(windowFrame,  width = 4,bd=4, font = 18,  text = " sin ", bg = "cyan")
sinButton["command"] = calculator.sinBtn
sinButton.grid(row = 2, column = 5,padx=16, pady=16)

cosButton = Button(windowFrame, bd = 4, width = 4,  font = 18, text = " cos ", bg = "cyan")
cosButton["command"] = calculator.cosBtn
cosButton.grid(row = 3, column = 5,padx=16, pady=16)

tanButton = Button(windowFrame, bd = 4, width = 4,  font = 18, text = " tan ", bg = "cyan")
tanButton["command"] = calculator.tanBtn
tanButton.grid(row = 4, column = 5,padx=16, pady=16)

sinInvButton = Button(windowFrame,bd = 4, width = 4,  font = 18, text=u"sin-\u00B9", bg = "cyan")
sinInvButton["command"] = calculator.sinInverseBtn
sinInvButton.grid(row = 2, column = 6,padx=16, pady=16)

cosInvButton = Button(windowFrame,bd=4, width = 4,  font = 18, text = u"cos-\u00B9", bg = "cyan")
cosInvButton["command"] = calculator.cosInverseBtn
cosInvButton.grid(row = 3, column = 6,padx=16, pady=16)

tanInvButton = Button(windowFrame, bd=4,width = 4,  font = 18, text = u"tan-\u00B9",bg = "cyan")
tanInvButton["command"] = calculator.tanInverseBtn
tanInvButton.grid(row = 4, column = 6,padx=16, pady=16)

sinhButton = Button(windowFrame, bd = 4, width = 4, font = 18,  text = " sinh ", bg = "cyan")
sinhButton["command"] = calculator.sinhBtn
sinhButton.grid(row = 2, column = 7,padx=16, pady=16)

coshButton = Button(windowFrame, bd = 4, width = 4, font = 18,  text = " cosh ", bg = "cyan")
coshButton["command"] = calculator.coshBtn
coshButton.grid(row = 3, column = 7,padx=16, pady=16)

tanhButton = Button(windowFrame, bd = 4, width = 4,  font = 18, text = " tanh ", bg = "cyan")
tanhButton["command"] = calculator.tanhBtn
tanhButton.grid(row = 4, column = 7,padx=16, pady=16)

#Logarithmitic buttons
lnButton = Button(windowFrame, width = 4, font = 18, bd=4,text = " ln  ", bg = "grey")
lnButton["command"] = calculator.lnBtn
lnButton.grid(row = 1, column = 6,padx=16, pady=16)

logButton = Button(windowFrame, width = 4, font = 18,  bd=4,text = " log ",bg = "grey")
logButton["command"] = calculator.logBtn
logButton.grid(row = 1, column = 7,padx=16, pady=16)


buttonExpon = Button(windowFrame, width = 4, font = 18,  bd=4, text = " e ̂ x ",bg = "grey")
buttonExpon["command"] = calculator.expoBtn
buttonExpon.grid(row = 1, column = 8,padx=16, pady=16)
  


#The Exponential Buttons
sqrtButton = Button(windowFrame, bd = 4, width = 4, font = 18,  text = "  √x  ", bg = "grey")
sqrtButton["command"] = calculator.sqrtBtn
sqrtButton.grid(row = 4, column = 8,padx=16, pady=16)

buttonPower = Button(windowFrame, width = 4, font = 18,  bd = 4, text = " x ̂ y ",bg = "cyan")
buttonPower["command"] = lambda: calculator.operation("power")
buttonPower.grid(row = 3, column = 8,padx=16, pady=16)

buttonpower2 = Button(windowFrame, width = 4, font = 18, bd=4,text=u"x\u00B2",bg = "cyan")
buttonpower2["command"] = calculator.x2Btn
buttonpower2.grid(row = 2, column = 8,padx=16, pady=16)


#Constants PI and e
button_pi = Button(windowFrame, width = 4, font = 18,  bd=4,text = " π ",bg = "grey")
button_pi["command"] = calculator.const_piBtn
button_pi.grid(row = 5, column = 3,padx=16, pady=16)

button_e = Button(windowFrame,bd=4, width = 4,  font = 18, text = " e ",bg="grey")
button_e["command"] = calculator.const_eBtn
button_e.grid(row = 1, column = 5,padx=16, pady=16)





window.mainloop()




