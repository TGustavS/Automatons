### Table of Contents
**[One Dimensional Cellular Automaton](#one-dimensional-cellular-automaton)**<br>
**[Langton's Ant](#langtons-ant)**<br>
**[GameOfLife](#gameoflife)**<br>

# One Dimensional Cellular Automaton
This is the first Automaton considered in the book 'A new kind of science'. Here each cell is either on or off depending on the states of the three cells above it. Interestingly one can get extremly complex behavoir even with such an simple premise. Below is a picture of Rule 30. It creates such complex structures that its middle row was used as a random number generator in the mathematica programming language. The structure of it is still not understood.

<p align="center">
    <img width=50% src="https://github.com/TGustavS/Automatons/blob/main/Pyramid/Rule30.png">
</p>


# Langton's Ant
Check https://en.wikipedia.org/wiki/Langton%27s_ant for a full explanation. In short there is an ant in the middle of the board that either moves left or right depending on the color of the tile it steps. When a tile is stepped on it will change its color through a predetermined list of colors it can cycle through. <br>
Eg. the rule LR means we have two colors: white and yellow. When the ant steps on a white tile the tile becomes yellow and the ant turns left. When it steps on a yellow tile it becomes white and turns right. <br>

I had some bugs while saving my results as a GIF so here are some nice looking ones I was able to save. The rule is LLRR.

<p align="center">
    <img width=50% src="https://github.com/TGustavS/Automatons/blob/main/LangtonsAnt/Gifs/Langton2.gif">
</p>

When trying out the program for yourself you will notice, that most of the rules will produce rather random looking things.  

# GameOfLife
A simple implementation of Conways Game of Life with a commandline interface I wrote as a practice. It only depends on matplotlib, random and argparse. 
As a practice I tried to find a fast algorithm to compute the new generations. If you have any ideas how to improve on it please write me.

```bash
python3 GOF.py -speed 30 -board brain
```

<p align="center">
    <img width=50% src="https://github.com/TGustavS/GameOfLife/blob/main/Brain.gif">
</p>



To get all informations what you can customize type the following in the command line:

```bash
python3 GOT.py --help
```

# Seeds
I took the seeds from https://conwaylife.com/wiki. Check the website if you want to know more about this wonderful game. <br>
Seed Names:
  - glider
  - spaceship
  - glidergun
  - bigglider
  - reflector
  - factory
  - ak-94
  - brain

# Algorithm
Rules for GOT:
  - If a dead cells has exactly 3 neighbors it is alive in the next generation otherwise it is still dead
  - If an alive cell has 2 or 3 neighbors it survives else it dies.


My algorithm is on average about 4x faster than the straight forward approach, i.e. for every generation count the neighbors of each cell and write on a new board if the cell is dead or alive. 

I saved the state of each cell as an int (0 dead or 1 alive). 

My algorithm:
  - go through each cell and check its value mod 10 is 1 (alive)
    - if it is add 10 to each neighbor 
    - if it is dead don't do anything
  - once done go through the board again and change all cells with value 30, 21 or 31 to 1 and the rest to 0.

Example:
```bash
[[0,0,0,0],                 [[10,20,20,10],             [[0,0,0,0],
 [0,1,1,0],       -->        [10,21,31,30],     -->      [0,1,1,1],
 [0,0,1,1],                  [20,50,61,41],              [0,0,0,0],
 [0,1,1,1]]                  [10,21,41,31]]              [0,1,0,1]]
``` 
The advantages of this algorithm are, that one only checks the neighbors of alive cells and that one does not have to make a copy of the board. Everything happens on the same board. 

 <p align="center">
   <img width=50% src="https://github.com/TGustavS/GameOfLife/blob/main/random.gif">
</p>
