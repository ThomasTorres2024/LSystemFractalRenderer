from LSysFractals import *

class HilbertCurve(LSysFractal):
    def __init__(self,turtle_info : dict):
        super().__init__(turtle_info)
        self._list_options  : dict = {"-" : self.minus, "F" : super().forward ,"+" : self.plus,}
        self._movement_options : dict = {"A" : self.A, "B" : self.B}

    #Value changing  Functions
    def A(self, index) -> None:
        super().change_iteration(self._permutations["A"],index)    

    def B(self, index) -> None:
        super().change_iteration(self._permutations["B"],index) 
 
class ArrowHeadSierpinski(LSysFractal):
    def __init__(self,turtle_info : dict):
        super().__init__(turtle_info)
        self._movement_options = {"A" : self.A, "B" : self.B}

    def A(self,index):
        super().change_iteration(self._permutations["A"],index)
        self.BMove()
        super().minus()
        self.AMove()
        super().minus()
        self.BMove()
    
    def B(self, index):
        super().change_iteration(self._permutations["B"],index)
        #Moves Turtle 
        self.AMove()
        super().plus()
        self.BMove()
        super().plus()
        self.AMove()

    def AMove(self):
        super().plus()
        super().forward()
        super().minus()
        super().forward()
        super().minus()
        super().forward()
    
    def BMove(self):
        super().forward()
        self.t.left(60)
        super().forward()
        self.t.left(60)
        super().forward()
        self.t.right(60)

"""Koch Fractal, Inherits from LSYsFractal"""
class Koch(LSysFractal):
    #Works for KochFlake and Curve
    def __init__(self, turtle_info : dict):
        super().__init__(turtle_info)
        self._movement_options = {"F" : self.F}

    def F(self,index):
        super().change_iteration(self._permutations["F"],index)
        super().forward()

class DragonCurve(LSysFractal):
    def __init__(self, turtle_info : dict):
        super().__init__(turtle_info)
        self._movement_options : dict = {"F" : self.F, "G" : self.G}

    def F(self,index):
        super().change_iteration(self._permutations["F"],index)
        super().forward()
    
    def G(self,index):
        super().change_iteration(self._permutations["G"],index)
        super().forward()
