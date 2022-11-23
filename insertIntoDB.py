#Project To insert Lookup and Delete Items In Inventory
import tkinter as mytk
from tkinter import *
import fileinput

myInventoryForm = mytk.Tk()
myInventoryForm.title('Inventory Input')
myInventoryForm.geometry("380x600")

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

def updateData():
    with open("database.txt", "r+") as file:
        data = file.read()

        def applyUpdates():
            with open("database.txt", "r+") as file:
                lines = file.read()
                file.close()
                #if data.find(NameTxt.get()):
                newName = data.replace(NameTxt.get() + ', ', updateNameTxt.get() + ', ')
                newAmount = data.replace(AmountTxt.get() + ', ', updateAmountTxt.get() + ', ')
                newCost = data.replace(CostTxt.get() + ', ', updateCostTxt.get() + ', ')
                newType = data.replace(typeTxt.get() + '\n', updatetypeTxt.get() + '\n')

                file = open("database.txt", 'w')
                file.write(newName)
                file.write(newAmount)
                file.write(newCost)
                file.write(newType)


                    #file.write(newName)
                #for line in lines:
                    #if line.find(NameTxt.get()):

                        #file.write(newName)
                        #file.write(line)

                #data.replace(NameTxt.get() + ', ', updateNameTxt.get() + ', ')
                # text_file.write(AmountTxt.get() + ', ')
                # text_file.write(CostTxt.get() + ', ')
                # text_file.write(typeTxt.get() + '\n')





        updateNameLabel = Label(myInventoryForm, text="Replace Name", width=10)
        updateNameLabel.place(x=20, y=300)

        updateNameTxt = Entry(myInventoryForm, width=27, relief="flat")
        updateNameTxt.place(x=120, y=300)

        updateAmountLabel = Label(myInventoryForm, text="Replace Amount", width=10)
        updateAmountLabel.place(x=20, y=330)

        updateAmountTxt = Entry(myInventoryForm, width=27, relief="flat")
        updateAmountTxt.place(x=120, y=330)

        updateCostLabel = Label(myInventoryForm, text="Replace Cost", width=10)
        updateCostLabel.place(x=20, y=360)

        updateCostTxt = Entry(myInventoryForm, width=27, relief="flat")
        updateCostTxt.place(x=120, y=360)

        updateTypeLabel = Label(myInventoryForm, text="Replace Type", width=10)
        updateTypeLabel.place(x=20, y=390)

        updatetypeTxt = Entry(myInventoryForm, width=27, relief="flat")
        updatetypeTxt.place(x=120, y=390)

        changeButton = Button(myInventoryForm, text="Update", command=applyUpdates, relief="groove", fg='blue')
        changeButton.place(x=150, y=410)





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
writeButton.place(x=20, y=190)

readButton = Button(myInventoryForm, text="Show DB", command=readTextFile, relief="groove", fg='blue')
readButton.place(x=120, y=190)

deleteButton = Button(myInventoryForm, text="Delete", command=deleteRow, relief="groove", fg='blue')
deleteButton.place(x=220, y=190)

updateButton = Button(myInventoryForm, text="Update", command=updateData, relief="groove", fg='blue')
updateButton.place(x=320, y=190)

myInventoryForm.configure(background='#FFE6D8')
myInventoryForm.mainloop()
