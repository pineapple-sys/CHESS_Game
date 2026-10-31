import pygame as py, sys
from src.config import *
from src import game
def draw_board(screen):
    n = 0
    for i in range(0,HEIGHT+1,RECT_SIZE):
        for j in range(0,WIDTH+1,RECT_SIZE):
            if n%2:
                py.draw.rect(screen, DARK,(j,i,RECT_SIZE,RECT_SIZE))
            else:
                py.draw.rect(screen, LIGHT,(j,i,RECT_SIZE,RECT_SIZE))
            n +=1
def show_piece(screen, coord, position):
    
    for i in range(len(coord)):

        piece = py.image.load(f"images/{list(position)[i]}.png").convert_alpha()
        piece = py.image.load(f"images/{list(position)[i]}.png").convert_alpha()
        piece = py.transform.smoothscale(piece,(RECT_SIZE,RECT_SIZE))
        
        if any(isinstance(coord[i][a], list) for a in range(len(coord[i]))):
            for a in range(len(coord[i])):
                piece_pos = (coord[i][a][1]*RECT_SIZE,coord[i][a][0]*RECT_SIZE)
                screen.blit(piece, piece_pos,special_flags=py.BLEND_PREMULTIPLIED)
        else:
            if isinstance(coord[i], list) and len(coord[i])==2:
                piece_pos = (coord[i][1]*RECT_SIZE,coord[i][0]*RECT_SIZE)
                screen.blit(piece, piece_pos,special_flags=py.BLEND_PREMULTIPLIED)
def click(event, coord, matrice, active):
    if event.type == py.MOUSEBUTTONDOWN and event.button == 1:
        cases_r = []
        
        for i in coord:
            for a in i:
                if not isinstance(a, list):
                    cases_r.append((int(i[1]),int(i[0])))
                  
                else:
                    cases_r.append((int(a[1]),int(a[0])))

        
        c =list(event.pos)
        c =(round(c[0]//RECT_SIZE),round(c[1]//RECT_SIZE))
        if c in cases_r:
            if active == (c[0]*RECT_SIZE,c[1]*RECT_SIZE):
                return ()
            
            return (c[0]*RECT_SIZE,c[1]*RECT_SIZE)
        
    return active
            


def draw_active(screen, active, plateau, possibilities):
    carré_vert = py.Surface((RECT_SIZE, RECT_SIZE), py.SRCALPHA)
    carré_vert.fill((GREEN_OPACITY))
    screen.blit(carré_vert,active)
    coord =[]
    for i in possibilities:
        coord.append(game.nargwhere(plateau,i))

    surface_cercle = py.Surface((RADIUS*2,RADIUS*2), py.SRCALPHA)
    for i in coord:
        py.draw.circle(surface_cercle,GREEN_OPACITY,(RADIUS,RADIUS),RADIUS)
        screen.blit(surface_cercle,(i[1]*RECT_SIZE+RADIUS*2,i[0]*RECT_SIZE+RADIUS*2))
            
def mov(active,player, event, matrice, position, player_pos, pawn_double):
    """
    if active:
        if event.type == py.MOUSEBUTTONDOWN and event.button == 1:
        player_pos = []
        for i in player:
            for a in i:
                if not isinstance(a, list):
                    player_pos.append((int(i[1]),int(i[0])))
                    
                else:
                    player_pos.append((int(a[1]),int(a[0])))
    """
    if active:
        coord = [active[1]//RECT_SIZE,active[0]//RECT_SIZE]
        possibilities = []
        for i in position:
            if not isinstance(position[i].split(), list):
                if position[i]== str(matrice[coord[0]][coord[1]]):
                    possibilities = game.legal_mov(i,str(matrice[coord[0]][coord[1]]), matrice, player_pos,pawn_double).split()
            else:
                for a in position[i].split():
                    if a == str(matrice[coord[0]][coord[1]]):
                        possibilities = game.legal_mov(i,str(matrice[coord[0]][coord[1]]), matrice, player_pos, pawn_double).split()
        return possibilities

                        

        
        

def main():
    py.init()
    py.display.set_caption("Chess Board!")
    screen = py.display.set_mode((WIDTH,HEIGHT),py.SRCALPHA)
    pawn_double,plateau, position,coord, player, player_pos= game.start()
    active = () #piece quon touche en vert: (20, 85, 30)
    possibilities = []
    running = True
    while running:
       
        for event in py.event.get():
            if event.type == py.QUIT:
                running = False
            active = click(event, player, plateau, active)
            possibilities = mov(active,player, event, plateau, position, player_pos, pawn_double)
            if active and event.type == py.MOUSEBUTTONDOWN and event.button ==1:
                game.deplacement(active, position,possibilities, plateau,event, coord, pawn_double)
        screen.fill(BACKGROUND_COLOR)
        draw_board(screen)
        if active:
            draw_active(screen, active, plateau, possibilities)
        show_piece(screen,coord, position)
        py.display.flip()
    print(pawn_double)
    py.quit()
    sys.exit()

if __name__ == "__main__":
    main()