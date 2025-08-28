"""
Updated file directory
8/28/25
"""

from LSysFractalOptions import *
from FileReader import *
from RandomGeneration import *
import turtle 

directories_dict : dict = { 
    "1":"L-System/instructions/LSystemsInstructions.txt",
    "2":"L-System/instructions/DiscoveredRandomKoch.txt",
    "3":"L-System/instructions/KochInstructions.txt"
}

def setup() -> turtle:
    myTurtle = turtle.Turtle()
    myTurtle.hideturtle()
    sc=turtle.Screen()
    #make turtle go zoooom
    sc.tracer(2,20000)

    turtle.bgcolor("black")
    myTurtle.color("pink")

    return myTurtle

def standard_generation(dd,iterations,myTurtle):
    
    list_and_key = change_directory(dd,iterations,myTurtle)
    l_systems_list = list_and_key[0]

    print(l_systems_list)

    key = int(list_and_key[1])

    drawers = {}
    if key == 1:
        drawers = {1:Koch(l_systems_list[0]),2:Koch(l_systems_list[1]),3:ArrowHeadSierpinski(l_systems_list[2]),
               4: HilbertCurve(l_systems_list[3]), 5 : DragonCurve(l_systems_list[4]), 6:Koch(l_systems_list[5]),7:Koch(l_systems_list[6]), 8:Koch(l_systems_list[7]), 9:Koch(l_systems_list[8]), 10:Koch(l_systems_list[9]),11:Koch(l_systems_list[10])
                ,12:Koch(l_systems_list[11]),13:Koch(l_systems_list[12]) }
    elif key == 2:
        for i in range(len(l_systems_list)):
            drawers[i+1] = Koch(l_systems_list[i])
    else:
        drawers = {}


    perform = int(input("Enter a number 1-{} to graph a turtle: ".format(len(drawers))))
    while perform != -1:
        if perform in drawers:
            drawers[perform].draw() 
            second_perform  =  int(input("1 to save, 2 continue drawing, 3 change file save name, 4 change colors -1 to discard: "))

            while (second_perform != -1):
                if  second_perform  == 1:
                    drawers[perform].saveScreen() 
                    print("File Saved")
                elif second_perform == 2:
                    drawers[perform].draw() 
                elif second_perform==3:
                    print("not implemented")
                elif second_perform ==4:
                    print("not implemented")
                else:
                    print('error invalid command')
                second_perform  =  int(input("1 to save, 2 continue drawing, 3 change file save name, 4 change colors -1 to discard: "))


        perform = int(input("Enter a number 1-{} to graph a turtle: ".format(len(drawers))))

def change_directory(dd,iterations,myTurtle):
    while True:
        change = input("1 - Lsystem Generation, 2 Discovered Random Koch, 3 Koch")
        if change in directories_dict:
            file = directories_dict[change]
            break
    myFileReader = FileReader(file, dd, iterations, myTurtle)
    return [myFileReader.get_all_LSys(),change]
    
def random_generation(dd : int, iterations : int, myTurtle : turtle,filename : str):

    userChoice = 0
    while userChoice != -1:
        myRandomKoch = RandomKoch(dd,iterations,myTurtle, filename)
        print(myRandomKoch.__str__())
        userChoice = int(input("To Discard: 1, 2 graph, 3 save, 4 change name, 5 save picture, -1 quit: "))
        while userChoice != 1 and userChoice != -1:
            if userChoice == 2:
                myRandomKoch.draw()
            elif userChoice == 3:
                myRandomKoch.save_file()
            elif userChoice ==4:
                myRandomKoch.change_name(input("Enter a new name: "))
            elif userChoice  ==5:
                myRandomKoch.saveScreen()
            userChoice = int(input("To Discard: 1, 2 graph, 3 save, 4 change name, 5 save picture -1 quit: "))

def main():

    #Configures turtle  elements like background etc 
    myTurtle = setup()

    #Drawing Dist
    dd = 10
    iterations : int = 5

    #Default file choice is to choose the set of famous well known fractals that behave well 
    file : str = "instructions/LSystemsInstructions.txt"
    random_file : str = "instructions/DiscoveredRandomKoch.txt"
    myFileReader = FileReader(file, dd, iterations, myTurtle)
    l_systems_list = myFileReader.get_all_LSys()
    draw_set = 1 

    generate = 0
    while generate != -1:
        generate = int(input("1 for Random  Generation,  2 for normal generation -1 to quit: "))
        if generate == 1:
            random_generation(dd,iterations,myTurtle,random_file)
        elif generate ==2:
            standard_generation(dd,iterations,myTurtle)

if __name__ == "__main__":
    main()