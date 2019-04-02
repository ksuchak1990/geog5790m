'''
 Agent.py                                         

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

import random
 
class Agent:
    '''
     Basic agent class.
     The class allows each agent an x and y location.
     It also gets a reference to a landscape object -- each agent accesses the same landscape 
     object -- they just have a link to it.
     The agents move randomly if they are in an area crowded with other agents.
     They move randomly if this is the case.
     Eventually they should end up evenly distributed.
     author <A href="http:#www.geog.leeds.ac.uk/people/a.evans/">Dr Andy Evans</A>
     version 1.0
    '''


    _x = 0
    _y = 0
    _landscape = None
    _densitylimit = 0



    def step(self) :
        '''
         Called each time iteration. 
         Agents check the density at their pousing the landscape, and 
         move randomly if needs be.
        '''
    
        if (self._landscape.getdensityat(self._x,self._y) > self._densitylimit) :

            self._x = int(random.random() * float(self._landscape.width))
            self._y = int(random.random() * float(self._landscape.height))        

            
        
    
    def setx(self, x) :
        '''
         Mutator for x location.
        '''
    
        self._x = x


    def getx (self) : 
        '''
         Accessor for x location.
        '''
    
        return self._x

        
    x = property(getx, setx)   

    
    

    def sety(self, y) :
        '''
         Mutator for y location.
        '''
    
        self._y = y
    

    def gety (self) : 
        '''
         Accessor for y location.
        '''
    
        return self._y

        
    y = property(gety, sety)     



    

    def setlandscape(self, landscape) :
        '''
         For adding a reference to the landscape object.
        '''
    
        self._landscape = landscape

        
    landscape = property(fset=setlandscape) 

    
    
    

    def setdensitylimit(self, densitylimit) :
        '''
         For accessing a reference to the landscape object.
        '''
    
        self._densitylimit = densitylimit

        
    def getdensitylimit (self) : 
        '''
         Accessor for densitylimit location.
        '''
    
        return self._densitylimit    
        
        
    densitylimit = property(getdensitylimit, setdensitylimit)     



    
