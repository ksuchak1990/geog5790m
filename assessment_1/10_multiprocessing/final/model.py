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
import multiprocessing

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
    

    
        
        
    def task(self, node, number_of_nodes, pipes):    

    
        width = 10                 # Landscape width
        height = 10                # Landscape height
        densitylimit = 50         # Density above which agents move.
        number_of_agents = 1000
        node_number_of_agents = 0
        iterations = 100           # Model iterations before stopping
        agents = []

        # Setup landcsape.
        
        landscape = Landscape()
        landscape.width = width
        landscape.height = height

        pipe_to_zero = None
        
        # Setup agents

        if (node != 0):

            node_number_of_agents = int(number_of_agents/(number_of_nodes - 1))
 
 
            if (node == (number_of_nodes - 1)):
                node_number_of_agents = int(node_number_of_agents + (number_of_agents % (number_of_nodes - 1)))
               
            pipe_to_zero = pipes[node - 1]


            for i in range (node_number_of_agents):

                agents.append(Agent())
                agents[i].densitylimit = densitylimit
                agents[i].landscape = landscape         # Agents get a reference to the 
                                                        # landscape to interrogate for densities.
                                                        # They could also get a reference to the 
                                                        # agent list if agents need to talk, 
                                                        # but here they don't.

                # Allocate agents a start location.
                
                x = int(width/2)         # Set to middle for start
                y = int(height/2)        # Set to middle for start

                agents[i].x = x 
                agents[i].y = y 

             

            # Give the landscape a reference to the agent list so it 
            # can find out where they all are and calculate densities.
            
            landscape.agents = agents

        # Print start map
        
        
        # Run

        for time in range(iterations):

            
            # Send out the local densities to node zero

            if (node != 0):
  
                landscape.calc_densities()
 
                densities = landscape.getdensities() 

                pipe_to_zero.send(densities) 
 
            else : # if node is node zero

                # Get the local densities in to node zero

                densities = [] 
                for x in range(width):
                    for y in range(height):
                        densities.append(0)
                        

                for i in range (len(pipes)):
 
                    # Get the local density from each node i.

                    local_densities = pipes[i].recv() 


                    # Add node i's density surface to the global surface.

                    for x in range(width):
                        for y in range(height):
                            densities[(y*width) + x] = densities[(y*width) + x] + local_densities[(y*width) + x] 
                            
 
            # Send out the global densities to the nodes

            if (node == 0):
 
                for i in range (len(pipes)):
 
                    pipes[i].send(densities) 
 
            else:
 
                # Receive the global densities from node zero.

                global_densities = pipe_to_zero.recv() 
 
                  
                landscape.setdensities(global_densities) 
 
                # Move the agents if the density is too high.

                for i in range(node_number_of_agents): 
 
                    agents[i].step() 
 

        
            # Report

            

            if (node == 0) :
                print("time = ", time, " -------------------") 
                landscape.setdensities(densities)
                for x in range(width):
                    for y in range (height):
                        print(landscape.getdensityat(x,y), end=" ")
                    print("")   




    def main(self):
        '''
         This version is parallelised.
        '''
    
        number_of_nodes = multiprocessing.cpu_count() 
        processes = []
        parent_pipes = []
        child_pipes = []
 
        # Make the communication pipes.
        
        for i in range(1, number_of_nodes):
            parent_conn, child_conn = multiprocessing.Pipe()
            parent_pipes.append(parent_conn)
            child_pipes.append(child_conn)
 
        # Give node zero one end of the pipes and start it processing.
        
        p0 = multiprocessing.Process(group=None, target=self.task, name=None, args=(0, number_of_nodes, parent_pipes), kwargs={}, daemon=None)
        processes.append(p0)
        p0.start()
 
        # Give the other nodes the other ends, and start them processing.
 
        for i in range(1, number_of_nodes):
            p = multiprocessing.Process(group=None, target=self.task, name=None, args=(i, number_of_nodes, child_pipes), kwargs={}, daemon=None)
            processes.append(p)
            p.start()   
            
        # Wait for all processes to finish before exiting. 
         
        for p in processes:
            p.join()
            
            
if __name__ == "__main__":

    Model().main()
    

