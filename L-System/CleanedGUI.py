from RandomGeneration import *
from LSysFractalOptions import *
import tkinter as tk  
from tkinter import *
from FileReader import  *

class GrapherGUI():
    filename   : str 
    title :str

    #TKinter
    graph_window  : tk
    report_text : Label
    completion_status : Label 
    right_side_commands : list

    #class with different attributes used to manipulate the turtle, t 
    grapher_turtle : RandomKoch
    #used to clear screen
    screen      : turtle
    #turtle used to draw 
    t : turtle

    def __init__(self,filename : str,title : str, myTurtle : turtle):

        #Used to Create Turlte 
        self.dd : int = 10
        self.iterations : int = 5 

        self.t = myTurtle
        self.filename = filename
        self.graph_window = Tk()
        self.title = title
        self.drawers = self.read_file()
        self.create_turtle()
        self.create_gui()

    def create_gui(self):
        top_frame  = LabelFrame(self.graph_window,padx=0,pady=5)
        self.low_frame  = LabelFrame(self.graph_window,padx=10,pady=10)

        #Create Top Most Section
        lsys_label = tk.Label(top_frame,text =self.title,font=('Arial 24 bold'))
        back_button = Button(top_frame,text="Go Back",font=('Arial 14'),command=self.terminate)
        lsys_label.pack(padx=20,pady=10)
        back_button.pack()

        #Creates  2 Frames 
        frame_left =  LabelFrame(self.graph_window,padx =0, pady=5)
        frame_right = LabelFrame(self.graph_window,padx =15, pady=5)

        #Creates Turtle That Will Be Used to Graph 
        self.report_text = Label(self.low_frame,text=self.grapher_turtle.__str__(),font=('TimesNewRomn 12'))
        self.add_elements_lowframe()
        #left side
        left_sub_left = LabelFrame(frame_left,padx=15,pady=15)
        

    

        #Puts Everything onto the left side of the screen
        #new random --> gets information for a new file 
        #clear      --> wipes fractal from screen
        #save_file  --> adds to file of saved fractals 
        #saveScreen --> saves fractal render as png 

        """Modified Version, Original below this code block"""

        #get commands for the left side 
        left_side_commands=self.get_left_side_commands()
        left_side = [Label(frame_left, text="Options",font=('Arial 16')),left_sub_left]
        for buttons in left_side_commands:
            left_side.append(Button(left_sub_left,text=buttons[0],font=('Arial 12'),command=buttons[1]))

        #right side
        self.complete_status = Label(frame_right,text="Status: Empty",font=('TimesNewRoman 12 bold'))

        #low frame 
        report_label = Label(self.low_frame,text="Fractal Info",font=('Arial 16'))

        #on the right side there are 2 more frames, a left and a right 
        sub_left = LabelFrame(frame_right,padx=0,pady=5)
        sub_right = LabelFrame(frame_right,padx=0,pady=5)

        text_box_width = 10
        text_box_height =1

        #Puts  Evverything onto the right side of the screen
        #update_turtle_info --> updates turtle info
        self.right_side_commands = [Label(frame_right,text="Modify Content",font=('Arial 16')),self.complete_status,
                    Button(frame_right,text="Modify",font=("Arial 10"),command=self.update_turtle_info),]
        changeable_elements : list[str] = ["Name:","New Axiom:",
                                           "New Permutation:"  ,"Name Angle:",
                                           "New Iterations:"   ,"New Drawing Distance :",]
        
        #adds  everything to the list of right side commands 
        for items in changeable_elements:
            self.right_side_commands.append(Label(sub_left,text=items,font=('TimesNewRoman 10')))
            self.right_side_commands.append(Text(sub_right,height=text_box_height,width=text_box_width,pady=2))

        #Renders All Buttons/Labels
        for buttons in [left_side,self.right_side_commands]:
            for label in buttons:
                label.pack()

        report_label.pack()
        self.report_text.pack()

        #First Top and Bottom Frames 
        top_frame.pack()
        self.low_frame.pack(pady=10)
        #Sub Frames
        sub_left.pack(padx=10,pady=10,side=LEFT)
        sub_right.pack(padx=10,pady=10,side=RIGHT)
        #Big Frames On Left and Right
        frame_left.pack(padx=10,pady=10,side=LEFT)
        frame_right.pack(padx=10,pady=10,side=RIGHT)

        #Runs
        self.graph_window.mainloop()

    def create_turtle(self):
        """
        This turtle will rely on using a child function to define the turtle
        """
        #Hides Drawers 
        self.t.hideturtle()
        #Makes turtle faster 
        self.screen_atr=turtle.Screen()
        self.screen_atr.tracer(2,20000)
        #Change Background color and turtle draw color
        turtle.bgcolor("black")
        self.t.color("pink")

        self.dd = 10
        self.iterations = 5
        #Updates Data 
        try:
            self.report_text.configure(text=self.grapher_turtle.__str__())
        except Exception as e:
            print(e)

    def update_turtle_info(self):
        change_commands = [self.grapher_turtle.change_name,self.grapher_turtle.change_axiom,
                        self.grapher_turtle.change_permutation,self.grapher_turtle.change_angle,
                        self.grapher_turtle.change_it,self.grapher_turtle.change_dd]
        for i in range(4,15,2):
            instance = self.right_side_commands[i].get(1.0,"end-1c") 
            if instance!='':
                change_commands[(i-4)//2](instance)

        self.report_text.configure(text=self.grapher_turtle.__str__())

    def add_elements_lowframe(self):
        pass 
    
    """The lower left panel has some buttons with some commands, these buttons will have varying commands based on what we want to execute"""
    def get_left_side_commands(self):
        pass 

    def read_file(self):
        pass

    def new_random(self):
        self.clear()
        self.create_turtle()
        self.render()

    def clear(self):
        self.t.clear()
        self.complete_status.configure(text="Status: Empty",fg="#000")

    def render(self):
        self.clear()
        self.complete_status.configure(text="Status: Incomplete",fg="#F00")
        self.grapher_turtle.draw()
        self.complete_status.configure(text="Status: Completed",fg="#0F0")

    def terminate(self):
        turtle.bye()
        self.graph_window.destroy()

"""GUI for left side"""
class RandomGrapher(GrapherGUI):

    def __init__(self,filename : str,title : str, myTurtle : turtle):
        super().__init__(filename,title,myTurtle)

    """Creates turtle manager for the fractal, the turtle is initially"""
    def create_turtle(self):
        self.grapher_turtle = RandomKoch(self.dd,self.iterations,self.t, self.filename)
        print(self.grapher_turtle)
        super().create_turtle()

    """Send commands for the left side when using Randomizer GUI"""
    def get_left_side_commands(self):
        super().get_left_side_commands()
        left_side_commands = [  ["Draw New Fractal",self.new_random],["Continue Fractal",self.render], ["New Fractal",self.create_turtle],["Clear Fractal",self.clear],
                            ["Download Fractal",self.grapher_turtle.save_file],["Save Picture",self.grapher_turtle.saveScreen]]
        return left_side_commands

class PresetGrapher(GrapherGUI):

    def __init__(self,filename : str,title : str, myTurtle : turtle):
        self.file_drop_display = None 
        
        #has a unique field called "drawers", a dictionary of all of the available turtles 
        super().__init__(filename,title,myTurtle)

    #Patches report by including a drop down menu to change the current fractal within a directory, and change the fractal directory 
    def read_file(self) -> dict:
        print(self.filename)
        myFileReader = FileReader(self.filename, self.dd, self.iterations, self.t)

        l_systems_list : list[dict] = myFileReader.get_all_LSys()

        drawers = {} 
        #Loads up turtles within a save file as "drawers." depending upon user choice, one of the classes will be chosen to graph a turtle 
        if self.filename == "/instructions/DiscoveredRandomKoch.txt":
            for i in range(len(l_systems_list)):
                drawers[i+1] = Koch(l_systems_list[i])
        else:
            drawers = {1:Koch(l_systems_list[0]),2:Koch(l_systems_list[1]),3:ArrowHeadSierpinski(l_systems_list[2]),
               4: HilbertCurve(l_systems_list[3]), 5 : DragonCurve(l_systems_list[4]), 6:Koch(l_systems_list[5]),7:Koch(l_systems_list[6]), 8:Koch(l_systems_list[7]), 9:Koch(l_systems_list[8]), 10:Koch(l_systems_list[9]),11:Koch(l_systems_list[10])
                ,12:Koch(l_systems_list[11]),13:Koch(l_systems_list[12]) }
        
        
        return drawers

    """Draws fractal user selected"""
    def draw_selected_fractal(self):

        #get fractal that user selected from list of fractals
        self.load_fractal()
        print("*"*50)
        print(self.grapher_turtle.get_name())
        print("*"*50)
        self.render()

    """Loads fractal that user selected"""
    def load_fractal(self):
        

        #check if the drop menu has already been initialized or not, if it has not we are initially displaying everything
        if self.file_drop_display:
            #get name of the fractal 
            fractal_name : str = self.file_drop_display.get()
            #look for correct grapher turtle 
            for i in range(1,len(self.drawers)+1):
                drawer = self.drawers[i]

                if(drawer.get_name()==fractal_name):
                    self.grapher_turtle=drawer
                    break  
        #otherwise default turtle is at 1
        else:
            self.grapher_turtle=self.drawers[1]

        #Updates Turtle info once selected, will only update info if the turtle's name chosen is any different than the previous one
        #this is important because otherwise the axiom label will grow too large 
        try:
            self.report_text.configure(text=self.grapher_turtle.__str__())
        except Exception as e:
            print(e)


    """Send commands for the left side when using Randomizer GUI"""
    def get_left_side_commands(self):
        super().get_left_side_commands()
        left_side_commands = [  ["Draw Fractal",self.draw_selected_fractal],["Continue Fractal",self.render], ["Load Fractal",self.load_fractal],["Clear Fractal",self.clear]
                              ,["Save Picture",self.grapher_turtle.saveScreen]]
        return left_side_commands

    """Adds elements to the top with two drop down menus"""
    def add_elements_lowframe(self):

        self.fractal_options = []
        for i in range(len(self.drawers)):
            self.fractal_options.append(self.drawers[i+1].get_name())
        self.file_options = self.fractal_options

        #add read in files to display as dropdown menu 
        self.file_label = Label(self.low_frame,text="File: {}".format(self.file_options[0])).pack()
        
        self.file_drop_display = tk.StringVar(self.low_frame)
        self.file_drop_display.set(self.file_options[0])
        file_drop = OptionMenu(self.low_frame ,self.file_drop_display , *self.file_options ) 

        file_drop.pack() 


        #get self.drawers()
        self.fractal_options = []
        for i in range(len(self.drawers)):
            self.fractal_options.append(self.drawers[i+1].get_name())

        #second drop down menu for random fractals from Koch by default 
        # self.fractal_drop_label=Label(self.low_frame,text="Fractal: {}".format(self.fractal_options[0])).pack()
        # fractal_drop_display = tk.StringVar() 
        # fractal_drop_display.set("Select Fractal")
        # fractal_drop = OptionMenu(self.low_frame,fractal_drop_display,*self.fractal_options)
        # fractal_drop.pack()

    """Initializes a turtle from a set of already determined fractals"""
    def create_turtle(self):
        #Takes element from drop down menu for selecting a turtle within a file, then  sets grapher to that turtle 
        
        #implicitly sets the grapher turtle using the load
        self.load_fractal()
        

        #self.grapher_turtle = RandomKoch(self.dd,self.iterations,self.t, self.filename)
        print(self.grapher_turtle)
        super().create_turtle()