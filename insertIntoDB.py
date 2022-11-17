#Project To insert Lookup and Delete Items In Inventory
import tkinter as mytk
from tkinter import *

myInventoryForm = mytk.Tk()
myInventoryForm.title('Inventory Input')
myInventoryForm.geometry("380x300")

def readTextFile():

    root = Tk()
    with open("database.txt", "r") as f:
        Label(root, text=f.read()).pack()


def writeTextFile():
    text_file = open("database.txt", 'a+')
    text_file.write(NameTxt.get() + ', ')
    text_file.write(AmountTxt.get() + ', ')
    text_file.write(CostTxt.get() + ', ')
    text_file.write(typeTxt.get() + '\n')

def deleteRow():
    with open("database.txt", "r") as file:
        lines = file.readlines()

        with open("database.txt", 'w') as fileDel:
            for line in lines:
                if line.find(NameTxt.get()):
                    fileDel.write(line)
                if line.split(', ')[3].find(typeTxt.get()):
                    fileDel.write(line)


Bannerlabel = Label(myInventoryForm, text="Inventory Form", width=40, bg='#81907E', fg='white')
Bannerlabel.place(x=20, y=20)

NameLabel = Label(myInventoryForm, text="Item Name", width=10, bg='#FFE6D8')
NameLabel.place(x=20, y=60)

NameTxt = Entry(myInventoryForm, width=27, relief="flat")
NameTxt.place(x=120, y=60)


NameTxt.focus()

AmountLabel = Label(myInventoryForm, text="Item Amount", width=10, bg='#FFE6D8')
AmountLabel.place(x=20, y=90)

AmountTxt = Entry(myInventoryForm, width=27, relief="flat")
AmountTxt.place(x=120, y=90)

CostLabel = Label(myInventoryForm, text="Item Cost", width=10, bg='#FFE6D8')
CostLabel.place(x=20, y=120)

CostTxt = Entry(myInventoryForm, width=27, relief="flat")
CostTxt.place(x=120, y=120)

typeLabel = Label(myInventoryForm, text="Item Type", width=10, bg='#FFE6D8')
typeLabel.place(x=20, y=150)

typeTxt = Entry(myInventoryForm, width=27, relief="flat")
typeTxt.place(x=120, y=150)

writeButton = Button(myInventoryForm, text="Insert", command=writeTextFile, relief="groove", fg='blue')
writeButton.place(x=80, y=190)

readButton = Button(myInventoryForm, text="Show DB", command=readTextFile, relief="groove", fg='blue')
readButton.place(x=180, y=190)

deleteButton = Button(myInventoryForm, text="Delete", command=deleteRow, relief="groove", fg='blue')
deleteButton.place(x=280, y=190)

myInventoryForm.configure(background='#FFE6D8')
myInventoryForm.mainloop()
