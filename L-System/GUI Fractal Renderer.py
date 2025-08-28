#New Main
"""This Version Works for the UI"""
from RandomGeneration import *
from CleanedGUI import *
import tkinter as tk  
from tkinter import ttk


RANDOM_FILENAME : str = "L-System/instructions/DiscoveredRandomKoch.txt"
PRESET_FILENAME : str = "L-System/instructions/LSystemsInstructions.txt"

def entry_gui():
    global window 
    window = Tk()

    style = ttk.Style(window)
    style.theme_use("vista")

    lsys_label = tk.Label(text ="Generate L-System Fractals",font=('Arial 24 bold'))
    lsys_label.pack(padx=20,pady=10)

    frame_left =  LabelFrame(window,padx =10, pady=5)
    frame_right = LabelFrame(window,padx =10, pady=5) 
    #When these buttons are pressed entry window is destroyed, new windows open

    buttons = [Button(frame_left,text ="Random Generation",font=('Arial 14'),command=random_gui),
               Button(frame_right,text="Preset Generation",font=('Arial 14'),command=preset_gui),
               Button(text="Quit",font=('Arial 14'),command=window.destroy)]
    frame_left.pack(padx=10,pady=10,side=LEFT)
    frame_right.pack(padx=10,pady=10,side=RIGHT)
    for button in buttons:
        button.pack()

    window.mainloop()

def random_gui():
    window.destroy()
    myTurtle = turtle.Turtle()
    #This Command Runs the GUI 
    myRandomGUI = RandomGrapher(RANDOM_FILENAME,"Random Fractal Generation:",myTurtle) 
    entry_gui()

def preset_gui():
    window.destroy()
    myTurtle = turtle.Turtle()

    #Function That Goes From File String -> Turtle 
    myRandomKoch = RandomKoch(10,5,myTurtle,PRESET_FILENAME)
    #This Command Runs the GUI 
    myRandomGUI = PresetGrapher(PRESET_FILENAME,"Preset Fractal Generation:",myTurtle) 
    entry_gui()

def select_class(selected_file : str ,myTurtle : turtle) -> object:
    """
    Returns corresponding turtle class depending upon the type of 
    """
    if selected_file == RANDOM_FILENAME:
        turtleClass = RandomKoch(10,5,myTurtle,RANDOM_FILENAME)  
    elif selected_file == PRESET_FILENAME:
        turtleClass = RandomKoch(10,5,myTurtle,RANDOM_FILENAME)  
    else:
        turtleClass = RandomKoch(10,5,myTurtle,RANDOM_FILENAME) 
    return turtleClass

def main(): 
    #Entry point is main GUI. Control is then transferred to the random or preset grapher GUIs 
    #When user presses buttons. 
    entry_gui()

if __name__ == "__main__":
    main()
