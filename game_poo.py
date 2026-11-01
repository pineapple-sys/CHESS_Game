import numpy as np
from src.config import *

def note_to_coord(notation):
    l = [i for i in range(ord("a"),ord("z")+1)]
    matrice = np.zeros((8,8),dtype="O")
    n = 8
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            matrice[i][j] = f"{chr(l[j])}{n}"
        n-=1
    result = np.argwhere(matrice == notation)[0]
    return (int(result[1])*RECT_SIZE,int(result[0])*RECT_SIZE)
