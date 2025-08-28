"""Abstract super class for fractals"""

import turtle 
import time
import os
from PIL import Image

class LSysFractal:
    #Inputs 

    t : turtle 
    drawing_dist : int 
    shift : int
    iterations : int 

    _name : str 
    _angle : float
    #Number of things added in 1 permutation
    _items_per_run : int
    #original instructions
    _axiom : list[str]
    #List of all possible permutations eg A -> BAB , B -> AAA
    _permutations : dict

    #Assigned in init
    _iterative_list : list[str] 

    #Assigned in Subclasses
    _list_options : dict
    _movement_options : dict

    def __init__(self, turtle_info : dict):
        self.drawing_dist = turtle_info["drawing_dist"]
        self._axiom = turtle_info["axiom"]
        self._permutations = turtle_info["permutations"]

        self.t = turtle_info["grapher"]
        self.t.hideturtle()
        self.angle = turtle_info["angle"]
        self.drawing_dist = turtle_info["drawing_dist"]
        self.iterations = turtle_info["iterations"]
        self._items_per_run = turtle_info["items_run"]
        self.scaler=turtle_info["scaler"]

        #For Every Use 
        self.shift = 0
        self._iterative_list = self._axiom.copy()
        self._list_options  : dict = {"-" : self.minus,"+" : self.plus}
        self._name = turtle_info["name"]

        self.reset_x=0
        self.reset_y=0

        self.axiom_display = ""
        self.original_info_cached = False 

        #all original info before modification
        self.original_info_dict : dict = {}

        for char in self.get_axiom(): self.axiom_display+=char

    def get_name(self) -> str:
        return self._name

    def get_axiom(self) -> list[str]:
        """Returns instruction to make a fractal at the ith iteration: """
        return self._axiom
    
    """
    Saves screen as a postscript, opens the ps  file with  PIl converts it to a png, and then
    deletes the PS file (idk how to optimize this skull emoji)
    """
    def saveScreen(self):

        #check if there is a directory of the form rendered/fractal_name/
        #if it alreaady exists add to directory 
        #otherwise create a file and add to directory, there will be a unique folder
        #for every fractal
        directory = "renders/{}/".format(self._name)
        if not os.path.exists(directory):
            #create file with this name 
            os.makedirs(directory, exist_ok=True)

        self.t.hideturtle()
        ts = turtle.getscreen()
        #creates ps and png filenames 
        ps_file_name : str = "{}{}.eps".format(directory,self._name)
        
        base_png_file_name : str = "{}{}".format(directory,self._name)
        png_file_name = base_png_file_name 
        i = 1
        while (os.path.isfile(png_file_name+str(".png"))):
            png_file_name = "{}{}".format(base_png_file_name,i)
            i+=1
        png_file_name+=".png"
        #creates png  file 
        ts.getcanvas().postscript(file=(ps_file_name))
        try:
            with Image.open(ps_file_name) as image:
                #saves png
                image.save(png_file_name, "PNG")
                print("File saved as {}".format(png_file_name))
        except Exception as e:
            print(e)

        #deltes old ps file 
        os.remove(ps_file_name)

    #Movement Functions
    def plus(self) -> None:
        self.t.left(self.angle)

    def minus(self) -> None:
        self.t.right(self.angle)

    #Value Changing Functions 
    def change_iteration(self,characters,index) -> int:
        #Index is the position that the list iterates through, characters is the list of characters
        self._iterative_list[index]= characters[0]
        for i in range(1,len(characters)):
            self._iterative_list.insert(i+index,characters[i])   

    def draw(self):
        """Draws the fractal iteration times, gradually gets more detailed"""
        #self.write_fractal_name()
        time_start = time.time()
        #print(self._axiom)
        for iterations in range(self.iterations):
            
            #Goes through the list and keeps adding elements to it 
            start : int = time.time()
            for i in range(len(self._axiom)):
                if self._axiom[i] in self._list_options:
                    self._list_options[self._axiom[i]]()
                elif self._axiom[i] in self._movement_options:
                    self._movement_options[self._axiom[i]](self.shift+i)
                    self.shift+=self._items_per_run    
            end : int = time.time()
            print("Iteration {} complete in {}".format(iterations+1,end-start))    
            #print(self._axiom)
            if iterations != self.iterations -1:
                self.reset()
        time_end = time.time()
        print("{} fractals of {} completed in: {}".format(self.iterations,self._name,(time_end-time_start)))


    def forward(self) -> None:
        self.t.forward(self.drawing_dist)

    def get_dd(self) -> int: 
        return self.drawing_dist
    
    def change_reset_coords(self,x,y):
        self.reset_x=x
        self.reset_y=y

    #Etc Functions
    def reset(self) -> None:
        self.t.up()
        self.t.goto(self.reset_x,self.reset_y)
        self._axiom= self._iterative_list.copy()
        self.t.clear()
        self.t.setheading(0)
        self.shift = 0
        #Drawing distance needs to get smaller each time to fit the whole thing on the screen
        self.drawing_dist*=self.scaler
        self.t.down()
    
    def write_fractal_name(self):
        self.t.up()
        self.t.goto(-500,700)
        self.t.down()
        turtle.write(self._name,font=("Verdana",20, "normal"))
        self.t.reset()

    """Changes the name of the fractal"""
    def change_name(self,name :str):
        self._name =name

    """If info was already modified, doesn't do anything since the 
    object should already have all of its information saved.
    
    Otherwise, saves all info into a dict"""
    def cache_original_info(self):
        if not self.original_info_cached:
            self.original_info_dict["name"]=self.get_name()
            self.original_info_dict["axiom"]=self.get_axiom()
            self.original_info_dict["angle"]=self.angle
            self.original_info_dict["dd"]=self.drawing_dist
            self.original_info_dict["iterations"]=self.iterations
            self.original_info_cached=True


    """Goes through original info and resets all fields"""
    def reset_original_info(self):
        if self.original_info_cached:
            self._name=self.original_info_dict["name"]
            self._axiom=self.original_info_dict["axiom"]
            self.angle=self.original_info_dict["angle"]
            self.drawing_dist=self.original_info_dict["dd"]
            self.iterations=self.original_info_dict["iterations"]
            self.original_info_cached=False 

    """Modifies the axiom of the L-Sys"""
    def change_axiom(self,new_axiom : str):
        self.cache_original_info()
        
        new_axiom_list : list[str] = []

        #this really required more verification, to make sure that the 
        #characters the user enters conform to the actual dictionary of what
        #this thing accepts 
        for char in new_axiom:
            if char.isal() or char == "-" or char == "+":
                new_axiom_list.append(char)

        self._axiom=new_axiom_list

    """Changes the angle of the L-Sys fractal"""
    def change_angle(self,new_angle : str):
        self.cache_original_info()

        #tries to convert angle checks if type conversion is fine or not here
        try:
            converted_angle : float = float(new_angle)
            self.angle=converted_angle
        except ValueError as e:
            print(e)
            print(f"ERROR {new_angle} could not be cast a number")

    """Changes drawing dist of Lsys"""
    def change_drawing_distance(self,dd):
        self.cache_original_info()

        #tries to convert drawing dist if type conversion is fine or not here
        try:
            drawing_dist : float = float(dd)
            self.drawing_dist=drawing_dist
        except ValueError as e:
            print(e)
            print(f"ERROR {dd} could not be cast a number")

    """Changes drawing dist of Lsys"""
    def change_iteration_for_gui(self,it):
        self.cache_original_info()

        #tries to convert drawing dist if type conversion is fine or not here
        try:
            iterations : float = int(it)
            self.iterations=iterations
        except ValueError as e:
            print(e)
            print(f"ERROR {it} could not be cast a number")


    """Returns all relevant turtle info"""
    def __str__(self):
        return ("Name: {}\nRoot Axiom: {}\nAngle: {}\nIterations: {}\nDrawing Distance: {}"
                .format(self._name,self.axiom_display,self.angle,self.iterations,self.drawing_dist))