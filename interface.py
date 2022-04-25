import tkinter as tk
import tkinter.messagebox as tkMessageBox
from tkinter import StringVar, IntVar, Variable
from turtle import width
from input import *


def ErrorMessage(s):
    tkMessageBox.showinfo("Error", "Please enter a valid "+s)


def SuccessMessage(s):
    tkMessageBox.showinfo("Success", s)


def handleEntries(val: str, s):
    if val == '':
        ErrorMessage(s)
        return False
    if s == 'Latitude':
        param['alat'] = val
    elif s == 'Longitude':
        param['alon'] = val
    elif s == 'Day':
        param['iday'] = val
    return True


def handleCWA():
    if assmEntry.get() == '':
        ErrorMessage("Assemetry Parameter for With Aerosol")
        return False
    if albEntry.get() == "":
        ErrorMessage("Albedo Parameter for With Aerosol")
        return False
    if extEntry.get() == '':
        ErrorMessage("Extinction Parameter for With Aerosol")
        return False
    WAparam['wbaer'] = albEntry.get()
    WAparam['gbaer'] = assmEntry.get()
    WAparam['qbaer'] = extEntry.get()
    return True


def handleCNA():
    if assm1Entry.get() == '':
        ErrorMessage("Assemetry Parameter for No Aerosol")
        return False
    if alb1Entry.get() == "":
        ErrorMessage("Albedo Parameter for No Aerosol")
        return False
    if ext1Entry.get() == '':
        ErrorMessage("Extinction Parameter for No Aerosol")
        return False
    NAparam['wbaer'] = alb1Entry.get()
    NAparam['gbaer'] = assm1Entry.get()
    NAparam['qbaer'] = ext1Entry.get()
    return True


def Handler():
    if handleEntries(latEntry.get(), "Latitude") == False:
        return
    if handleEntries(lonEntry.get(), "Longitude") == False:
        return
    if handleEntries(dayEntry.get(), "Day") == False:
        return

    if r.get() == 1:
        if handleCWA() == False:
            return
        if AerosolScript(WAparam) == False:
            ErrorMessage("values,Error in Aerosol Script")
            return
    elif r.get() == 2:
        if handleCNA() == False:
            return
        if WithoutAerosolScript(NAparam) == False:
            ErrorMessage("values,Error in No Aerosol Script")
            return
    else:
        if handleCWA() == False or handleCNA() == False:
            return
        if BothScript(WAparam, NAparam) == False:
            ErrorMessage("values,Error in Both Script")
            return
    SuccessMessage("output,Successfully Generated")


def HandleDropdown():
    if dpEntry.get() == '':
        ErrorMessage("Enter the Valid Value for selected dropdown")
        return
    param[DefaultValues.get()] = dpEntry.get()
    SuccessMessage("Selected Dropdown Entity Succesfully Updated")


master = tk.Tk()
master.title("SBDART INTERFACE")
master.geometry('1500x900')


lat = tk.Label(master, text="Latitude:", font=(
    "Helvetica", 12), width=15, height=4, justify='right')
lat.grid(row=0, column=1)


lon = tk.Label(master, text="Longitude:", font=(
    "Helvetica", 12), width=15, height=4, justify='center')
lon.grid(row=0, column=3)


latEntry = tk.Entry(master, font=("Helvetica", 12), bd=2, bg="white", width=15)
latEntry.grid(row=0, column=2)


lonEntry = tk.Entry(master, font=("Helvetica", 12), bd=2, bg="white", width=15)
lonEntry.grid(row=0, column=4)


day = tk.Label(master, text="Day:", font=("Helvetica", 12),
               width=15, height=4, justify='center')
day.grid(row=0, column=5)


dayEntry = tk.Entry(master, font=("Helvetica", 12), bd=2, bg="white", width=15)
dayEntry.grid(row=0, column=6)

l1 = tk.Label(master, text="Compulsory values for Running SBDART with Aerosol ", font=(
    "Helvetica", 12), height=4)
l1.grid(row=1, column=0, columnspan=3)

ass = tk.Label(master, text="Assymetry Parameter:", font=(
    "Helvetica", 12), width=25, height=4, justify='center')
ass.grid(row=2, column=0)


assmEntry = tk.Entry(master, font=("Helvetica", 12),
                     bd=2, bg="white", width=120)
assmEntry.grid(row=2, column=1, columnspan=6)


alb = tk.Label(master, text="Single Scattering Albedo:", font=(
    "Helvetica", 12), width=25, height=4, justify='center')
alb.grid(row=3, column=0)


albEntry = tk.Entry(master, font=("Helvetica", 12),
                    bd=2, bg="white", width=120)
albEntry.grid(row=3, column=1, columnspan=6)

ext = tk.Label(master, text="Extinction Coefficient:", font=(
    "Helvetica", 12), width=25, height=4, justify='center')
ext.grid(row=4, column=0)

extEntry = tk.Entry(master, font=("Helvetica", 12),
                    bd=2, bg="white", width=120)
extEntry.grid(row=4, column=1, columnspan=6)


l2 = tk.Label(master, text="Compulsory values for Running SBDART without Aerosol ", font=(
    "Helvetica", 12), height=4)
l2.grid(row=5, column=0, columnspan=3)

ass1 = tk.Label(master, text="Assymetry Parameter:", font=(
    "Helvetica", 12), width=25, height=4, justify='center')
ass1.grid(row=6, column=0)

assm1Entry = tk.Entry(master, font=("Helvetica", 12),
                      bd=2, bg="white", width=120)
assm1Entry.grid(row=6, column=1, columnspan=6)

alb1 = tk.Label(master, text="Single Scattering Albedo:", font=(
    "Helvetica", 12), width=25, height=4, justify='center')
alb1.grid(row=7, column=0)

alb1Entry = tk.Entry(master, font=("Helvetica", 12),
                     bd=2, bg="white", width=120)
alb1Entry.grid(row=7, column=1, columnspan=6)

ext1 = tk.Label(master, text="Extinction Coeficient:", font=(
    "Helvetica", 12), width=25, height=4, justify='center')
ext1.grid(row=8, column=0)

ext1Entry = tk.Entry(master, font=("Helvetica", 12),
                     bd=2, bg="white", width=120)
ext1Entry.grid(row=8, column=1, columnspan=6)

lb3 = tk.Label(master, text="Standard Parameters ",
               font=("Helvetica", 12), height=4)
lb3.grid(row=9, column=0, columnspan=3)

options = ['wlinf', 'wlsup', 'wlinc', 'isalb', 'uw', 'uo3', 'xco2',
           'xch4', 'xn2o', 'wlbaer', 'iaer', 'jaer', 'idatm', 'iout', 'nstr']
DefaultValues = StringVar()
DefaultValues.set(options[0])
dropdown = tk.OptionMenu(master, DefaultValues, *options)
dropdown.grid(row=10, column=0)


dpEntry = tk.Entry(master, font=("Helvetica", 12), bd=2, bg="white", width=20)
dpEntry.grid(row=10, column=1)

enter = tk.Button(master, text="Enter", width=10, height=3,command=HandleDropdown)
enter.grid(row=10, column=2)
lb4 = tk.Label(master, text="Different Ways of INPUTS Files for SBDART ", font=(
    "Helvetica", 12), height=4)
lb4.grid(row=11, column=0, columnspan=3)


r = IntVar()
r.set(1)
rb1 = tk.Radiobutton(master, text="With Aerosol",
                     variable=r, value=1, font=("Helvetica", 12))
rb2 = tk.Radiobutton(master, text="Without Aerosol",
                     variable=r, value=2, font=("Helvetica", 12))
rb3 = tk.Radiobutton(master, text="With Aerosol and Without Aerosol",
                     variable=r, value=3, font=("Helvetica", 12))
run = tk.Button(master, text="Run", font=("Helvetica", 12),
                width=10, height=3, command=Handler)
rb1.grid(row=12, column=0)
rb2.grid(row=12, column=1)
rb3.grid(row=12, column=2)
run.grid(row=12, column=3)


master.mainloop()
