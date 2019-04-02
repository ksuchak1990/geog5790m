# 9 - Cellular Automata

Cellular automata are a class of models that treat an environment as a
discrete grid and update the contents of each of the grid cells using some rules
concerning the surrounding cells.
In this practical, we use cellular automata to model how a forest fire spreads
across a small 10 x 10 grid.

The practical involves the following steps:

1. Build the environment: Build a 10 x 10 grid, with each cell containing the
   value 5 to represent the amount of fuel in the cell before the fire starts.
2. Set the fire at the initial position: Given a chosen grid cell, we reduce the
   value in the cell by 1; cells with value 0 < x < 5 are taken to be on fire.
3. Iterate over time, spreading the fire: Iterate forward, looping through the
   rows and columns, updating each cell such that if it is adjacent to another
   cell that is on fire then it catches fire.
4. Take care with edge cases: Two approaches are used in treating the boundaries
   of the model.
   1. Hard walls: A hard wall implementation ensures that the fire cannot spread
      any further than the edge of the environment.
   2. Torus: A toroidal environment allows the fire to spread off the edge of
      the environment, reentering at the opposite edge.
   The former is predominantly used, with the latter being considered
   unrealistic.

Further improvements were implemented:

1. Introduce a stopping condition: Introduce a stopping condition to the time
   step loop to ensure that the model stops as soon as the forest in completely
   burnt out.

