from LSysFractalOptions import Koch
import random
import turtle

class RandomKoch(Koch):

    axiom : list[str]
    permutation : list[str]
    turtle_info : dict 

    def __init__(self,dd,iterations,myTurtle,filename):

        #Make Random Axiom
        #self.axiom = self._random_list()
        #Make Random Permutation
        #self.permutation = self._random_list()

        self.choices = {"0":'F',"1":'+',"2":'-'}
        self.choices_list=['F','+','-']
        self.anglechoices = [30,45,60,90,120]
        self.seed = self.full_seed()

        seed_list = self.seed.split("%")
        angle = self.anglechoices[int(seed_list[0])]
        self.axiom=(self.converter(seed_list[1]))
        self.permutation=(self.converter(seed_list[2]))
        #self.permutation = self._random_list()
        #angle = random.choice(self.anglechoices)

        self.turtle_info = {"drawing_dist" : dd, "iterations" : iterations, "grapher" : myTurtle, "name" : "Random", 
                       "axiom":self.axiom,"angle":angle,"permutations": {"F":self.permutation},"items_run":len(self.permutation)-1,"scaler":0.75}
        self.filename = filename
        super().__init__(self.turtle_info)
    

    #Setters

    def change_name(self, new_name):
        self._name = new_name

    def change_axiom(self,new_axiom):
        change = True
        new_axiom.upper()
        for i in range(len(new_axiom)):
            if new_axiom[i] not in self.choices_list:
                change = False 
                break
        if (change):
            self.axiom = new_axiom

    def change_permutation(self,new_permutation):
        new_permutation.upper()
        change = True
        for i in range(len(new_permutation)):
            if new_permutation[i] not in self.choices_list:
                change = False 
                break
        if (change):
            self.permutation = new_permutation

    def change_angle(self,angle):
        try:
            self.angle=int(angle)
        except ValueError:
            pass

    def change_it(self,it):
        try:
            self.iterations=int(it)
        except ValueError:
            pass

    def change_dd(self,dd):
        try:
            self.drawing_dist=int(dd)
        except ValueError:
            pass


    #Getters

    def get_seed(self):
        return self.seed

    def get_angle(self):
        return self.angle

    def get_axiom(self):
        return self.axiom

    def get_permutation(self):
        return self.permutation
    
    def get_name(self) -> str:
        return self._name
    
    def __str__(self):
        axiom = permutation = ""

        for chars in self.axiom: axiom += chars 
        for chars in self.permutation: permutation+=chars
        return ("Name: {}\nAxiom: {}\nPermutation: {}\nAngle: {}\nIterations: {}\nDrawing Distance: {}\nSeed: {}"
                .format(self._name,axiom,permutation,self.angle,self.iterations,self.drawing_dist,self.seed))

    def conv(self, list_str : list[str]) -> str:
        output_str : str = ""
        for elements in list_str:
            output_str+=elements
        return output_str

    def save_file(self):
        try:
            with open(self.filename,'a') as file:
                print("Info if save is corrupted:\n {}".format(self.turtle_info)) 
                save_items : list[str] = [self.turtle_info["name"],"F:{}".format(self.conv(self.turtle_info["permutations"]["F"])),self.conv(self.turtle_info["axiom"]), str(self.turtle_info["angle"]), str(self.turtle_info["items_run"]), str(self.turtle_info["scaler"]) ]
                for elements in save_items:
                    file.write("{}\n".format(elements))

        except FileNotFoundError:
            print("ERROR: File not found: \n{}".format(self.turtle_info))

    def full_seed(self) -> str:
        #need angle list for this 
        angle = str(random.randint(0,len(self.anglechoices)-1))
        #need symbol list for 
        axiom = self.partial_seed(self.choices)
        #use same symbol list 
        permutation = self.partial_seed(self.choices)

        seed = "{}%{}%{}".format(angle,axiom,permutation)
        return seed

    def converter(self, seed_str) -> list[str]:
        """
        Turns seed into a list 
        """
        converted_seed = []
        for i in range(len(seed_str)):
            converted_seed.append(self.choices[seed_str[i]])
        if 'F' not in converted_seed:
            converted_seed.append('F')

        copied_list = converted_seed.copy()
        converted_seed.reverse() 
        copied_list+=converted_seed
        return copied_list


    def partial_seed(self,choices) -> str:
        #1st = angle number 
        #remaining elements = 
        #determines  angle 
        seed = ""
        #I have these values hard coded for now 
        length = length = random.randint(3,7)
        for i in range(length):
            seed+=str(random.randint(0,len(choices)-1))
        return seed 

    def _random_list(self) -> list[str]:
        length = random.randint(3,7)

        #self._random_seed(min_elements=3,max_elements=7,min_list=0,max_list=2)

        #choices = {0:'F',1:'+',2:'-'}
        choices = ['F','+','-']
        output_list = []
        for i in range(length):
            output_list.append(random.choice(choices))
        if 'F' not in output_list:
            output_list.insert(random.randint(0,len(output_list)-1),'F')
        #Enforce symmetry to force interesting patterns
        copied_list = output_list.copy()
        output_list.reverse() 
        copied_list+=output_list
        return copied_list

