import matplotlib
from matplotlib import pyplot as plt
from matplotlib import animation
import copy
orient = {
    'N': [[0,-1,'W'],[0,1,'O']],
    'O': [[-1,0,'N'],[1,0,'S']],
    'S': [[0,1,'O'],[0,-1,'W']],
    'W': [[1,0,'S'],[-1,0,'N']]
}

def create(n=200):
    Board = [[0 for i in range(n)] for j in range(n)]
    return Board


def translate(moves):
    moves = moves.replace('L','0').replace('R','1')
    tem = []
    for i in moves:
        tem.append(int(i))
    return tem


def langstonsAnt(moves,steps,size): 
    n = size
    m = len(moves) 
    current = [n//2,n//2]
    Board = create(n)
    direc = 'N'
    fig, ax = plt.subplots(tight_layout=True)
    my_cmap = matplotlib.colors.ListedColormap(['w', 'g','r','y','b','c','m','k','silver','gold'])
    ax.axis('off')
    # Grid
    for x in range(n + 1):
        ax.axhline(x, lw=0.02, color='k', zorder=5)
        ax.axvline(x, lw=0.02, color='k', zorder=5)
    ims = []

    for i in range(steps):
        if current[0] == 0 or current[1] == 0:
            print('Board is to small')
            break
        if steps > 500 and i%10 == 0:     
            data = ax.imshow(Board, cmap=my_cmap, extent=[0, n, 0, n])
            ims.append((data,))
        tem = copy.deepcopy(current)
        current[0] += orient[direc][moves[Board[tem[0]][tem[1]]]][0]
        current[1] += orient[direc][moves[Board[tem[0]][tem[1]]]][1]
        direc = orient[direc][moves[Board[tem[0]][tem[1]]]][2]
        Board[current[0]][current[1]] = (Board[current[0]][current[1]]+1)%m
        
        
    im_ani = animation.ArtistAnimation(
        fig, ims, interval=1, repeat_delay=300, blit=True
    )
    plt.show()
    save = input('Do you want to save the GIF?  [y],[n] \n')
    
    if save == 'y':
        name = input("Give name for Gif:")
        im_ani.save((name + ".gif"))

    
if __name__ == "__main__":
    moves = input('Input movement pattern eg.: RRLL\n')
    steps = int(input('Input number of Steps:\n'))
    size = int(input('Input size of board:\n'))
    moves = translate(moves)
    langstonsAnt(moves,steps,size)