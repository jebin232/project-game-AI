import os
from numpy import random as rp
def song():
    mu=[1,2,3,4,5,6,7,8,9,10]
    for i in mu:
        son = rp.choice(i)
        music="E:\Jb song"
        songs=os.listdir(music)
        print(songs)
        os.startfile(os.path.join(music,songs[son]))
song()