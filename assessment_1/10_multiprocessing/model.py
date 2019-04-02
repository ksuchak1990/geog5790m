'''
 Model.py                                         

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

from landscape import Landscape 
from agent import Agent
import random

class Model :
    '''
     Main class for running a model.
     The class contains an array of agents plus a landscape object.
     The landscape keeps track of the density of agents in each location.
     The agents move randomly if they are in an area crowded with other agents.
     They move randomly if this is the case.
     Eventually they should end up evenly distributed.
     author <A href="http:#www.geog.leeds.ac.uk/people/a.evans/">Dr Andy Evans</A>
     version 1.0
    '''
    

    def main(self):
        '''
         Most stuff is done in main, to make using parallelisation easier to integrate 
         at a later stage. This version is not currently parallelised.
        '''
    
        width = 10                 # Landscape width
        height = 10                # Landscape height
        densitylimit = 100         # Density above which agents move.
        number_of_agents = 1000
        iterations = 100           # Model iterations before stopping
        agents = []

        # Setup landcsape.
        
        landscape = Landscape()
        landscape.width = width
        landscape.height = height



        for i in range (number_of_agents):

            agents.append(Agent())
            agents[i].densitylimit = densitylimit
            agents[i].landscape = landscape         # Agents get a reference to the 
                                                    # landscape to interrogate for densities.
                                                    # They could also get a reference to the 
                                                    # agent list if agents need to talk, 
                                                    # but here they don't.

            # Randomly allocate agents a start location.
            
            x = int(width/2)         # Set to middle for start
            y = int(height/2)        # Set to middle for start

            agents[i].x = x 
            agents[i].y = y 

         

        # Give the landscape a reference to the agent list so it 
        # can find out where they all are and calculate densities.
        
        landscape.agents = agents

        # Print start map
        
        landscape.calc_densities()
        for x in range(width):
            for y in range (height):
                print(landscape.getdensityat(x,y), end=" ")
            print("")
        print("-------------------------")

        # Run

        for time in range(iterations):

            landscape.calc_densities()

            for i in range (number_of_agents):
                agents[i].step()
             




        # Report

        for x in range(width):
            for y in range (height):
                print(landscape.getdensityat(x,y), end=" ")
            print("")
        

if __name__ == "__main__":
    Model().main()
    

