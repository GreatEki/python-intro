from tkinter import *

# Create GUI window
myWindow = Tk()

# Function to convert user input to miles
def km_to_miles():
    userInput = entryValue.get()
    if not userInput:
        myText.insert(END, 'Please Enter a number')
    else:
        miles=float(entryValue.get())*1.6
        myText.insert(END, miles)
        

    


# Create A Button Widget
myButton = Button(myWindow, text='Execute', command=km_to_miles)
myButton.grid(row=0, column=0)
# The grid() method specifies the positions we want to place the widget


# Create an Entry Widget
entryValue = StringVar()
myEntry = Entry(myWindow, textvariable=entryValue)
myEntry.grid(row=0, column=1)


# Create A Text Widget
myText = Text(myWindow, height=1, width=20)
myText.grid(row=0, column=2)


myWindow.mainloop()