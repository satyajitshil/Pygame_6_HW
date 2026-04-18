from tkinter import *

base = Tk()
base.title("Product Finder!")
base.geometry("400x300")

lbl = Label(text="Welcome!",fg= "darkblue", bg= "#BBC9CF",height=1,width=300)
prod1_lbl = Label(text="Enter Number #1", fg= "darkblue", bg= "#BDCBD1")
prod1_entry = Entry()
prod2_lbl = Label(text="Enter Number #2",fg= "darkblue", bg= "#BDCBD1") 
prod2_entry = Entry()

def find_prod():
    try:
        num1 = int(prod1_entry.get())
        num2 = int(prod2_entry.get())
        product = num1*num2
        global message
        greet = "Welcome to the Application\n"
        message = "The product of "+str(num1)+" and "+str(num2)+" is "+str(product)

        text_box.insert(END, greet)
        text_box.insert(END, message)
    except:
        text_box.insert(END,"Please enter VALID NUMBERS!\n")

text_box = Text(height= 3)
btn = Button(text= "Calculate", command= find_prod, fg= "darkblue", bg= "#BDCBD1")

lbl.pack()
prod1_lbl.pack()
prod1_entry.pack()
prod2_lbl.pack()
prod2_entry.pack()
btn.pack()
text_box.pack()

base.mainloop()
