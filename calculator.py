from tkinter import *
mw=Tk()
mw.title('calculator')
def clear():
    db.delete(0,END)    
def btn_clk(num):
    cur_num=db.get()
    clear()
    f_num=cur_num+num
    db.insert(0,f_num)
first_num=0
math=''
math_sign=''
ms_list=['+','-','*','/']   
def calc(mathtype,ms):
    global first_num,math,math_sign
    math=mathtype
    math_sign=ms
    first_num=db.get()
    for x in first_num:
        if x in ms_list:
            first_num=first_num.replace(x,'')
    clear()
    db.insert(0,first_num+math_sign)
def equal():
    global first_num,math_sign   
    second_num=db.get().replace(str(first_num)+math_sign,'')
    clear()
    result=''
    if math=='add':
        result=int(first_num)+int(second_num)
    elif math=='sub':
        result=int(first_num)-int(second_num)
    elif math=='mul':
        result=int(first_num)*int(second_num)
    elif math=='div':
        result=int(first_num)/int(second_num)            
    db.insert(0,str(result))

#creating widgets
db=Entry(mw,width=14,font=('arial',28),justify=RIGHT)
btn_0=Button(mw,text='0',font=('arial',14),padx=36,pady=10,command=lambda:btn_clk('0'))
btn_1=Button(mw,text='1',font=('arial',14),padx=36,pady=10,command=lambda:btn_clk('1'))
btn_2=Button(mw,text='2',font=('arial',14),padx=36,pady=10,command=lambda:btn_clk('2'))
btn_3=Button(mw,text='3',font=('arial',14),padx=36,pady=10,command=lambda:btn_clk('3'))
btn_4=Button(mw,text='4',font=('arial',14),padx=36,pady=10,command=lambda:btn_clk('4'))
btn_5=Button(mw,text='5',font=('arial',14),padx=36,pady=10,command=lambda:btn_clk('5'))
btn_6=Button(mw,text='6',font=('arial',14),padx=36,pady=10,command=lambda:btn_clk('6'))
btn_7=Button(mw,text='7',font=('arial',14),padx=36,pady=10,command=lambda:btn_clk('7'))
btn_8=Button(mw,text='8',font=('arial',14),padx=36,pady=10,command=lambda:btn_clk('8'))
btn_9=Button(mw,text='9',font=('arial',14),padx=36,pady=10,command=lambda:btn_clk('9'))
btn_add=Button(mw,text='+',font=('arial',14),padx=36,pady=10,command=lambda:calc('add','+'))
btn_sub=Button(mw,text='-',font=('arial',14),padx=38,pady=10,command=lambda:calc('sub','-'))
btn_mul=Button(mw,text='*',font=('arial',14),padx=38,pady=10,command=lambda:calc('mul','*'))
btn_div=Button(mw,text='/',font=('arial',14),padx=38,pady=10,command=lambda:calc('div','/'))
btn_equal=Button(mw,text='=',font=('arial',14),padx=38,pady=40,command=equal)
btn_clear=Button(mw,text='Clear',font=('arial',14),padx=72,pady=10,command=clear)
#showing widgets
btn_add.grid(row=6,column=0,padx=2,pady=2)
btn_sub.grid(row=6,column=1,padx=2,pady=2)

btn_mul.grid(row=5,column=0,padx=2,pady=2)
btn_div.grid(row=5,column=1,padx=2,pady=2)
btn_equal.grid(row=5,column=2,rowspan=2,padx=2,pady=2)

btn_0.grid(row=4,column=0,padx=2,pady=2)
btn_clear.grid(row=4,column=1,columnspan=2,padx=2,pady=2)

btn_1.grid(row=3,column=0,padx=2,pady=2)
btn_2.grid(row=3,column=1,padx=2,pady=2)
btn_3.grid(row=3,column=2,padx=2,pady=2)

btn_4.grid(row=2,column=0,padx=2,pady=2)
btn_5.grid(row=2,column=1,padx=2,pady=2)
btn_6.grid(row=2,column=2,padx=2,pady=2)

btn_7.grid(row=1,column=0,padx=2,pady=2)
btn_8.grid(row=1,column=1,padx=2,pady=2)
btn_9.grid(row=1,column=2,padx=2,pady=2)

db.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
mw.mainloop()
