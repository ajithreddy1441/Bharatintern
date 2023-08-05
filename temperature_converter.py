from tkinter import *

window= Tk()
window.title('Temperature Converter')
window.minsize(width=300, height=200)
window.config(padx=50,pady=50)

label=Label(text='Covert form Celcius to Fahrenheit:',font=('Courrier',25,'bold'))
label.grid(column=2, row=0)
label.config(pady=10)

input=Entry()
input.grid(row=1,column=2)

ans=Label(text=' ',font=('Courrier',10,'bold'))
ans.grid(row=4,column=2)

def celcius():
    temp = float(input.get())
    temp_C= temp-32*5/9
    ans['text']='Temperature in Celcius is: '+str(int(temp_C))

def forenheit():
    temp = float(input.get())
    temp_F= temp*9/5+32
    ans['text']='Temperature in Fahrenheit is: '+str(int(temp_F))


button=Button(text='Covert to Celcous', command=celcius)
button.grid(row=2,column=1)

button=Button(text='Covert to fohrenheit', command=forenheit)
button.grid(row=2,column=3)

window.mainloop()