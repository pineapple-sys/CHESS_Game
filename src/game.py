import numpy as np
from src.config import*

def start():  
    l = [i for i in range(ord("a"),ord("z")+1)]
    matrice = np.zeros((8,8),dtype="O")
    n = 8
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            matrice[i][j] = f"{chr(l[j])}{n}"
        n-=1
    position = { 
        #Black
        "black-king":"e8",
        "black-queen":"d8",
        "black-bishop":"f8 c8",
        "black-knight":"b8 g8",
        "black-rook":"h8 a8",
        "black-pawn":"a7 b7 c7 d7 e7 f7 g7 h7",
        #White
        "white-king":"e1",
        "white-queen":"d1",
        "white-bishop":"f1 c1",
        "white-knight":"b1 g1",
        "white-rook":"h1 a1",
        "white-pawn":"a2 b2 c2 d2 e2 f2 g2 h2"

    }
    player_pos= { 
        #White
        "white-king":"e1",
        "white-queen":"d1",
        "white-bishop":"f1 c1",
        "white-knight":"b1 g1",
        "white-rook":"h1 a1",
        "white-pawn":"a2 b2 c2 d2 e2 f2 g2 h2"

    }
    pawn = {}
    for i in player_pos:
        if i =="white-pawn":
            tab = player_pos[i].split()
            for a in tab:
                pawn[a] = True
   
    tableau = []
    for i in position:
        if len(position[i].split())>1:
            ligne = position[i].split()
            liste = []
            for a in ligne:
                liste.append(list(map(int,np.argwhere(matrice==a)[0])))
            tableau.append(liste)
        else:
            
            tableau.append(list(map(int,np.argwhere(matrice==position[i])[0])))
    
    
    player = []
    for i in player_pos:
        if len(player_pos[i].split())>1:
            ligne = player_pos[i].split()
            liste = []
            for a in ligne:
                liste.append(list(np.argwhere(matrice==a)[0]))
            player.append(liste)
        else:
            
            player.append(list(np.argwhere(matrice==player_pos[i])[0]))
    
    return pawn,matrice, position,list(tableau), player, player_pos


def legal_mov(piece,emplacement, plateau, player_pos, pawn):
    pos = []
    for i in player_pos:
        if isinstance(player_pos[i].split(),list):
            for a in player_pos[i].split():
                pos.append(a)
        else:
            pos.append(str(player.pos[i]))
    if piece == "white-bishop":
        all_legal = []
        pos_matrice = np.argwhere(plateau==emplacement)[0]
        num_depart = int(emplacement[1])
        num = num_depart
        pos = []
        for i in player_pos:
            if isinstance(player_pos[i].split(),list):
                for a in player_pos[i].split():
                    pos.append(a)
            else:
                pos.append(str(player.pos[i]))
        while ord(emplacement[0])+num-num_depart < ord('h') and num<8:
            num+=1
            mov = f"{chr(ord(emplacement[0])+num-num_depart)}{num}"
            if mov in pos:
                break
            else:
                all_legal.append(f"{chr(ord(emplacement[0])+num-num_depart)}{num}")
        num = int(emplacement[1])
        while ord(emplacement[0])-num+num_depart > ord('a') and num<8:
            num+=1
            mov = f"{chr(ord(emplacement[0])-num+num_depart)}{num}"
            if mov in pos:
                break
            else:
                all_legal.append(f"{chr(ord(emplacement[0])-num+num_depart)}{num}")

        
        legal =''
        for i in all_legal:
            legal += i+" "

        return legal
    if piece == "white-knight":
        
        mov1 = f"{chr(ord(emplacement[0])+2)}{int(emplacement[1])+1}"
        mov2 = f"{chr(ord(emplacement[0])+1)}{int(emplacement[1])+2}" 

        mov3 = f"{chr(ord(emplacement[0])+2)}{int(emplacement[1])-1}"
        mov4 = f"{chr(ord(emplacement[0])-1)}{int(emplacement[1])+2}"
        
        mov5 = f"{chr(ord(emplacement[0])+1)}{int(emplacement[1])-2}"
        mov6 = f"{chr(ord(emplacement[0])-2)}{int(emplacement[1])+1}"

        mov7 = f"{chr(ord(emplacement[0])-2)}{int(emplacement[1])-1}"
        mov8 = f"{chr(ord(emplacement[0])-1)}{int(emplacement[1])-2}"

        all_legal = [mov1,mov2,mov3,mov4,mov5,mov6,mov7,mov8]
        
        for i in all_legal[:]:
            if not ord('a')<=ord(i[0])<=ord('h') or not 1<=int(i[1:])<=8 or i in pos:
                all_legal.remove(i)

        legal = ''
        for i in all_legal:
            legal += i+" "
        return legal

    if piece=="white-pawn":
        mov1 = emplacement[0]+str(int(emplacement[1])+1)
        mov = [mov1]
        if pawn[emplacement] == True:
            mov2 = emplacement[0]+str(int(emplacement[1])+2)
            mov.append(mov2)
        legal = ''
        for i in mov:
            legal += i+" "
        
        return legal
    if piece=="white-rook":
        mov =[]
        num_depart = int(emplacement[1])
        num = num_depart
        while num < 8: #deplacement vers le haut
            m = f"{chr(ord(emplacement[0]))}{num}"
            if m in pos:
                break
            num +=1
            mov.append(f"{chr(ord(emplacement[0]))}{num}")
        num = num_depart-1 
        while num >=1:#deplacement vers le bas
            m = f"{chr(ord(emplacement[0]))}{num}"
            if m in pos:
                break
            mov.append(f"{chr(ord(emplacement[0]))}{num}")
            num -=1
        num = num_depart+1#deplacement vers la droite
        while ord(emplacement[0])+num-num_depart<=ord('h'):
            m = f"{chr(ord(emplacement[0])+num-num_depart)}{num_depart}"
            if m in pos:
                break
            mov.append(f"{chr(ord(emplacement[0])+num-num_depart)}{num_depart}")
            num+=1
        num = num_depart-1
        while ord(emplacement[0])+num-num_depart>=ord('a'):
            m = f"{chr(ord(emplacement[0])+num-num_depart)}{num_depart}"
            if m in pos:
                break
            mov.append(f"{chr(ord(emplacement[0])+num-num_depart)}{num_depart}")
            num-=1
        legal = ''
        for i in mov:
            legal += i+" "
        return legal
    if piece == "white-king":
        mov1 = emplacement[0]+str(int(emplacement[1])+1)
        mov2 = emplacement[0]+str(int(emplacement[1])-1)
        mov3 = chr(ord(emplacement[0])+1)+str(int(emplacement[1]))
        mov4 = chr(ord(emplacement[0])-1)+str(int(emplacement[1]))
        mov5 = chr(ord(emplacement[0])+1)+str(int(emplacement[1])+1)
        mov6 = chr(ord(emplacement[0])-1)+str(int(emplacement[1])-1)
        mov7 = chr(ord(emplacement[0])+1)+str(int(emplacement[1])-1)
        mov8 = chr(ord(emplacement[0])-1)+str(int(emplacement[1])+1)
        mov = [mov1,mov2,mov3,mov4,mov5,mov6,mov7,mov8]
        
        for i in mov[:]:
            if i in pos or not ord('a')<=ord(i[0])<=ord('z') or not 1<=int(i[1])<=8:
                mov.remove(i)
            
        legal = ''
        for i in mov:
            legal += str(i) + " "
        return legal
    if piece == "white-queen":
        all_legal = []
        pos_matrice = np.argwhere(plateau==emplacement)[0]
        num_depart = int(emplacement[1])
        num = num_depart
        pos = []
        for i in player_pos:
            if isinstance(player_pos[i].split(),list):
                for a in player_pos[i].split():
                    pos.append(a)
            else:
                pos.append(str(player.pos[i]))
        while ord(emplacement[0])+num-num_depart < ord('h') and num<8:
            num+=1
            mov = f"{chr(ord(emplacement[0])+num-num_depart)}{num}"
            if mov in pos:
                break
            else:
                all_legal.append(f"{chr(ord(emplacement[0])+num-num_depart)}{num}")
        num = int(emplacement[1])
        while ord(emplacement[0])-num+num_depart > ord('a') and num<8:
            num+=1
            mov = f"{chr(ord(emplacement[0])-num+num_depart)}{num}"
            if mov in pos:
                break
            else:
                all_legal.append(f"{chr(ord(emplacement[0])-num+num_depart)}{num}")
        
        num_depart = int(emplacement[1])
        num = num_depart
        while num < 8: #deplacement vers le haut
            m = f"{chr(ord(emplacement[0]))}{num}"
            if m in pos:
                break
            num +=1
            all_legal.append(f"{chr(ord(emplacement[0]))}{num}")
        num = num_depart-1 
        while num >=1:#deplacement vers le bas
            m = f"{chr(ord(emplacement[0]))}{num}"
            if m in pos:
                break
            all_legal.append(f"{chr(ord(emplacement[0]))}{num}")
            num -=1
        num = num_depart+1#deplacement vers la droite
        while ord(emplacement[0])+num-num_depart<=ord('h'):
            m = f"{chr(ord(emplacement[0])+num-num_depart)}{num_depart}"
            if m in pos:
                break
            all_legal.append(f"{chr(ord(emplacement[0])+num-num_depart)}{num_depart}")
            num+=1
        num = num_depart-1
        while ord(emplacement[0])+num-num_depart>=ord('a'):
            m = f"{chr(ord(emplacement[0])+num-num_depart)}{num_depart}"
            if m in pos:
                break
            all_legal.append(f"{chr(ord(emplacement[0])+num-num_depart)}{num_depart}")
            num-=1
        legal = ''
        for i in all_legal:
            legal += i+" "
        return legal

def nargwhere(matrice, n):
    return np.argwhere(matrice==n)[0]


def deplacement(active, position,possibilities, matrice, event, coord, pawn_double):

    coord_possible = []
    for i in possibilities:
        damn = nargwhere(matrice,i)
        coord_possible.append([int(damn[0]),int(damn[1])])
    mouse_pos = [event.pos[1]//RECT_SIZE,event.pos[0]//RECT_SIZE]
    elem = [active[1]//RECT_SIZE,active[0]//RECT_SIZE]
    case = matrice[elem[0]][elem[1]]
    future_case = matrice[mouse_pos[0]][mouse_pos[1]]
    if case in position["white-pawn"].split():
        if int(future_case[1])-int(case[1]):
            pawn_double[future_case] = False
            #pawn_double.pop(case)  avant de faire ça faut mettre a jour position player_pos etccc
    if mouse_pos in coord_possible:
        for i in coord[:]:
            if isinstance(i, list) and len(i)>=1:
                if isinstance(i[0], list):
                    for a in i[:]:
                        if a == elem:
                            i.remove(a)
                            i.append(mouse_pos)
                else:       
                    if i==elem:
                        coord.remove(i)
                        coord.append(mouse_pos)
   
    
    """
    for i in coord_possible:
        if mouse_pos == i:
            pos_elem = (active[1]//RECT_SIZE,active[0]//RECT_SIZE)
            for i in position:
                if isinstance(position[i].split(), list):
                    lign =''
                    for a in position[i].split():
                        
                        if str(a) == str(matrice[pos_elem[0]][pos_elem[1]]):
                            piece  =i
                        else:
                            lign += a + " "
                    position[i] = lign
                elif str(position[i]) == str(matrice[pos_elem[0]][pos_elem[1]]):
                    position = ""
                    piece = i

            
            position[i] += matrice[mouse_pos[0]][mouse_pos[1]]
    """
   

