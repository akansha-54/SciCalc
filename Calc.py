from tkinter import *
import math
class calculate() :

    def num_press(self, num):
        self.eq = False
        temp = self.enter.get()
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
            self.total = float(self.enter.get())

    def display(self, value):
        self.enter.delete(0, END)
        self.enter.insert(0, value)

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

    def do_sum(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "minus":
            self.total -= self.current
        if self.op == "multiply":
            self.total *= self.current
        if self.op == "divide":
            if self.current == 0 :
                self.total="Zero Division Error"
            else:
                self.total /= self.current
        if self.op == "power":
            self.total = math.pow(self.total,self.current)
        if self.op == "sqrt":
            if self.current < 0 :
                self.total = "Input Error"
            else:
                self.total = math.pow(self.total, 1 / 2)
        if self.op == "fact":
            self.total=int(self.enter.get())
            self.total=math.factorial(self.total)
        if self.op == "ln":
            if self.current <= 0 :
                self.total = "Domain Error"
            else:
                self.total = math.log(self.current,math.e)
        if self.op == "log":
            if self.current <= 0 :
                self.total = "Domain Error"
            else:
                self.total=math.log10(self.total)
        if self.op == "sine":
            self.total=math.sin(self.total)
        if self.op == "cosine":
            self.total = math.cos(self.total)
        if self.op == "tangent":
            self.total = math.tan(self.total)
        if self.op == "exp":
            self.total = math.exp(self.total)
        if self.op == "inv":
            if self.total == 0 :
                self.total = "Zero Division Error"
            else:
                self.total = 1/self.total
        if self.op == "percent":
            self.total = (self.total*100)/self.current
        self.new_num = True
        self.op_pending = False
        self.display(self.total)

    def clear(self):
        self.eq = False
        self.current = "0"
        self.display(0)
        self.new_num = True

    def all_clear(self):
        self.clear()
        self.total = 0

    def sign(self):
        self.eq = False
        self.current = -(float(self.enter.get()))
        self.display(self.current)

    def __init__(self):
        self.total = 0
        self.current = ""
        self.new_num = True
        self.op_pending = False
        self.op = ""
        self.eq = False

        self.obj=Tk()
        self.obj.title("Calculator")
        self.obj.geometry("425x190+500+350")
        self.obj.resizable(0,0)
        self.obj.config(bg="khaki")

        self.enter = Entry(font=("lucida handwriting",15,"bold"),width=27,bg="Crimson",fg="white")



        self.b1 = Button(text="7",width=8,font=("Times New Roman",9,"bold"),bg="black",fg="white",command=lambda: self.num_press('7'))
        self.b2 = Button(text="8",width=8,font=("Times New Roman",9,"bold"),bg="black",fg="white",command=lambda: self.num_press('8'))
        self.b3 = Button(text="9",width=8,font=("Times New Roman",9,"bold"),bg="black",fg="white",command=lambda: self.num_press('9'))
        self.b4 = Button(text="4",width=8,font=("Times New Roman",9,"bold"),bg="black",fg="white",command=lambda: self.num_press('4'))
        self.b5 = Button(text="5",width=8,font=("Times New Roman",9,"bold"),bg="black",fg="white",command=lambda: self.num_press('5'))
        self.b6 = Button(text="6",width=8,font=("Times New Roman",9,"bold"),bg="black",fg="white",command=lambda: self.num_press('6'))
        self.b7 = Button(text="1",width=8,font=("Times New Roman",9,"bold"),bg="black",fg="white",command=lambda: self.num_press('1'))
        self.b8 = Button(text="2",width=8,font=("Times New Roman",9,"bold"),bg="black",fg="white",command=lambda: self.num_press('2'))
        self.b9 = Button(text="3",width=8,font=("Times New Roman",9,"bold"),bg="black",fg="white",command=lambda: self.num_press('3'))
        self.b10 = Button(text="+",width=8,font=("Times New Roman",9,"bold"),bg="black",fg="white",command=lambda: self.operation("add"))
        self.b11 = Button(text="-",width=8,font=("Times New Roman",9,"bold"),bg="black",fg="white",command=lambda: self.operation("minus"))
        self.b12 = Button(text="*",width=8,font=("Times New Roman",9,"bold"),bg="black",fg="white",command=lambda: self.operation("multiply"))
        self.b13 = Button(text="/",width=8,font=("Times New Roman",9,"bold"),bg="black",fg="white",command=lambda: self.operation("divide"))
        self.b14 = Button(text="%",width=8,font=("Times New Roman",9,"bold"),bg="black",fg="white",command=lambda: self.operation("percent"))
        self.b15 = Button(text="^",width=8,font=("Times New Roman",9,"bold"),bg="black",fg="white",command=lambda: self.operation("power"))
        self.b16 = Button(text="!",width=8,font=("Times New Roman",9,"bold"),bg="black",fg="white",command=lambda: self.operation("fact"))
        self.b17 = Button(text="sin",width=8,font=("Times New Roman",9,"bold"),bg="black",fg="white",command=lambda: self.operation("sine"))
        self.b18 = Button(text="cos",width=8,font=("Times New Roman",9,"bold"),bg="black",fg="white",command=lambda: self.operation("cosine"))
        self.b19 = Button(text="tan",width=8,font=("Times New Roman",9,"bold"),bg="black",fg="white",command=lambda: self.operation("tangent"))
        self.b20 = Button(text="log",width=8,font=("Times New Roman",9,"bold"),bg="black",fg="white",command=lambda: self.operation("log"))
        self.b21 = Button(text="ln",width=8,font=("Times New Roman",9,"bold"),bg="black",fg="white",command=lambda: self.operation("ln"))
        self.b22 = Button(text="=",width=8,font=("Times New Roman",9,"bold"),bg="black",fg="white",command=lambda:self.calc_total())
        self.b23 = Button(text=".",width=8,font=("Times New Roman",9,"bold"),bg="black",fg="white",command=lambda: self.num_press('.'))
        self.b24 = Button(text="C",width=18,font=("Times New Roman",9,"bold"),bg="black",fg="white",command=lambda: self.all_clear())
        self.b26 = Button(text="0",width=8,font=("Times New Roman",9,"bold"),bg="black",fg="white",command=lambda: self.num_press('0'))
        self.b27 = Button(text="e^x",width=8,font=("Times New Roman",9,"bold"),bg="black",fg="white",command=lambda: self.operation("exp"))
        self.b28 = Button(text="1/x",width=8,font=("Times New Roman",9,"bold"),bg="black",fg="white",command=lambda: self.operation("inv"))
        self.b29 = Button(text="√",width=8,font=("Times New Roman",9,"bold"),bg="black",fg="white",command=lambda: self.operation("sqrt"))
        self.b30 = Button(text="±",width=8,font=("Times New Roman",9,"bold"),bg="black",fg="white",command=lambda: self.sign())

        self.enter.place(x="7",y="5")

        self.b1.place(x="5",y="40")
        self.b2.place(x="75",y="40")
        self.b3.place(x="145",y="40")
        self.b13.place(x="215",y="40")
        self.b14.place(x="285",y="40")
        self.b29.place(x="355",y="40")

        self.b4.place(x="5",y="70")
        self.b5.place(x="75",y="70")
        self.b6.place(x="145",y="70")
        self.b12.place(x="215",y="70")
        self.b17.place(x="285",y="70")
        self.b28.place(x="355",y="70")

        self.b7.place(x="5",y="100")
        self.b8.place(x="75",y="100")
        self.b9.place(x="145",y="100")
        self.b11.place(x="215",y="100")
        self.b18.place(x="285",y="100")
        self.b27.place(x="355",y="100")

        self.b30.place(x="5",y="130")
        self.b26.place(x="75",y="130")
        self.b23.place(x="145",y="130")
        self.b10.place(x="215",y="130")
        self.b19.place(x="285",y="130")
        self.b20.place(x="355",y="130")

        self.b24.place(x="5",y="160")
        self.b22.place(x="145",y="160")
        self.b15.place(x="215",y="160")
        self.b16.place(x="285",y="160")
        self.b21.place(x="355",y="160")

        self.obj.mainloop()


if __name__=="__main__":
    calculate()