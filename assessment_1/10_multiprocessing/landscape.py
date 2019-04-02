'''
 Landscape.py                                         

 --Copyright notice-- 

 Copyright (c) School of Geography, University of Leeds. 
 http:#www.geog.leeds.ac.uk/
 This software is licensed under 'The Artistic License' which can be found at 
 the Open Source Initiative website at... 
 http:#www.opensource.org/licenses/artistic-license.php
 Please note that the optional Clause 8 does not apply to this code.

 The Standard Version source code, and associated documentation can be found at... 
 [online] http:#www.ccg.leeds.ac.uk/software/ 

 --End of Copyright notice-- 
'''

 

class Landscape:
    '''
     Basic landscape class.
     A single landscape object is made in the model, and all agents have a reference to it.
     The landscape has a reference to the array of agents created in the main 
     model class, so it can get each agent in turn and ask for its location.
     From this, it calculates a denisty map.
     In Model.py the map is then requested by each agent in turn, who uses the 
     densities to decide whether to move.
     author <A href="http:#www.geog.leeds.ac.uk/people/a.evans/">Dr Andy Evans</A>
     version 1.0
    '''

    _width = 0
    _height = 0
    _agents = []        # Reference to the list of agents created in Model.py.
    _densities = []

    

    def calc_densities(self):
        '''
         Calulates a density map.
         Called each iteration in Model.py before the agents move.
         Note this is a 1D array, not 2D as landscape, for efficiency of transfer.
        '''
    
        self._densities = []
        for pos in range(self._width * self._height):
            self._densities.append(0)

        for i in range (len(self._agents)) :

            self._densities[(self._agents[i].y * self._width) + self._agents[i].x] += 1
        
        
 
    

    def getdensityat(self, x, y) :
        '''
         Returns the density at a specific location.
         Hides the complexity of 1D to 2D conversion.
        '''
    
        return self._densities[(y*self._width) + x]

   

    

    def setagents (self, agents) :
        '''
         Sets a reference to the agent list.
        '''
    
        self._agents = agents

    
    
    agents = property(fget=None, fset=setagents)
    
    

    
    
    def setwidth(self, width) :
        '''
         Mutator for landscape width.
        '''
    
        self._width = width

    
    def getwidth(self) : 
        '''
         Accessor for landscape width.
        '''
    
        return self._width

        
    width = property(getwidth, setwidth)

    
    
    

    def setheight(self, height) :
        '''
         Mutator for landscape height.
        '''
    
        self._height = height
    

    
    def getheight(self) :
        '''
         Accessor for landscape height.
        '''
    
        return self._height

    
    height = property(getheight, setheight)


