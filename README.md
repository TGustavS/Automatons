# Automatons
Some Automatons I programmed.

# Langton's Ant
Check https://en.wikipedia.org/wiki/Langton%27s_ant for a full explanation. In short there is an ant in the middle of the board that either moves left or right depending on the color of the tile it steps on. When a tile is stepped on it will change its color through a predetermined list of colors it can cycle through. <br>

By looking at the easiest example with two different color states, where the ant moves left if it steps on a white tile and right when it moves on a yellow tile, one notices that the behavior that emerges seems to be rather complex. 

<p align="center">
    <img width=30% src="https://github.com/TGustavS/Automatons/blob/main/LangtonsAnt/Gifs/Langtons1.gif">
</p>

Interestingly it takes about 10000 steps until the ant goes into a stable pattern and creates a so called highway.

<p align="center">
    <img width=50% src="https://github.com/TGustavS/Automatons/blob/main/LangtonsAnt/Gifs/Langtons2.gif">
</p>
