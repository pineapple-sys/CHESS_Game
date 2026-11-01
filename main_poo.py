import pygame as py
from src.config import *
import game_poo
import sys

class Knight:
    def __init__(self, pos:str , color:str):
        self.pos = pos
        self.image = py.image.load(f"images/{color}-knight.png").convert_alpha()
        self.image = py.transform.smoothscale(self.image,(RECT_SIZE,RECT_SIZE))
    def show(self,screen, color):
        
        piece_pos = game_poo.note_to_coord(self.pos)
        screen.blit(self.image, piece_pos,special_flags=py.BLEND_PREMULTIPLIED)
        
class Bishop:
    def __init__(self, pos:str , color:str ):
        self.pos = pos 
        self.image = py.image.load(f"images/{color}-bishop.png").convert_alpha()
        self.image = py.transform.smoothscale(self.image,(RECT_SIZE,RECT_SIZE))
    def show(self,screen, color):
        
        piece_pos = game_poo.note_to_coord(self.pos)
        screen.blit(self.image, piece_pos,special_flags=py.BLEND_PREMULTIPLIED)
class King:
    def __init__(self, pos:str , color:str):
        self.pos = pos 
        self.image = py.image.load(f"images/{color}-king.png").convert_alpha()
        self.image = py.transform.smoothscale(self.image,(RECT_SIZE,RECT_SIZE))
    def show(self,screen, color):
       
        piece_pos = game_poo.note_to_coord(self.pos)
        screen.blit(self.image, piece_pos,special_flags=py.BLEND_PREMULTIPLIED)
class Queen:
    def __init__(self, pos:str , color:str):
        self.pos = pos
        self.image = py.image.load(f"images/{color}-queen.png").convert_alpha()
        self.image = py.transform.smoothscale(self.image,(RECT_SIZE,RECT_SIZE))
    def show(self,screen, color):
        
        piece_pos = game_poo.note_to_coord(self.pos)
        screen.blit(self.image, piece_pos,special_flags=py.BLEND_PREMULTIPLIED)
class Rook:
    def __init__(self, pos:str , color:str):
        self.pos = pos
        self.image = py.image.load(f"images/{color}-rook.png").convert_alpha()
        self.image = py.transform.smoothscale(self.image,(RECT_SIZE,RECT_SIZE))
    def show(self,screen, color):
        
        piece_pos = game_poo.note_to_coord(self.pos)
        screen.blit(self.image, piece_pos,special_flags=py.BLEND_PREMULTIPLIED)
class Pawn:
    def __init__(self, pos:str , color:str):
        self.pos = pos
        self.image = py.image.load(f"images/{color}-pawn.png").convert_alpha()
        self.image = py.transform.smoothscale(self.image,(RECT_SIZE,RECT_SIZE))
    def show(self,screen, color):

        piece_pos = game_poo.note_to_coord(self.pos)
        screen.blit(self.image, piece_pos,special_flags=py.BLEND_PREMULTIPLIED)
        
class Player:
    def __init__(self, player_pos:dict, color:str):
        self.position = []
        self.player_pos = player_pos
        self.color = color
    def show(self, screen):
        for i in self.position:
            i.show(screen,self.color)
    def start(self):
        for i in self.player_pos:
            name = i[6:]
            if name== "knight":
                for a in self.player_pos[i]:
                    piece = Knight(a, self.color)
                    self.position.append(piece)
            if name == "bishop":
                for a in self.player_pos[i]:
                    piece = Bishop(a, self.color)
                    self.position.append(piece)
            if name == "king":
                for a in self.player_pos[i]:
                    piece = King(a, self.color)
                    self.position.append(piece)
            if name == "queen":
                for a in self.player_pos[i]:
                    piece = Queen(a, self.color)
                    self.position.append(piece)
            if name == "pawn":
                for a in self.player_pos[i]:
                    piece = Pawn(a, self.color)
                    self.position.append(piece)
            if name == "rook":
                for a in self.player_pos[i]:
                    piece = Rook(a, self.color)
                    self.position.append(piece)


def draw_board(screen):
    for i in range(8):
        for j in range(8):
            n = i+j
            if n%2:
                py.draw.rect(screen,DARK, (i*RECT_SIZE,j*RECT_SIZE,RECT_SIZE,RECT_SIZE))
            else:
                py.draw.rect(screen,LIGHT, (i*RECT_SIZE,j*RECT_SIZE,RECT_SIZE,RECT_SIZE))
       
def main():
    py.init()
    screen = py.display.set_mode((WIDTH,HEIGHT))
    White = Player(white_pos, "white")
    White.start()
    for i in White.position:
        print(game_poo.note_to_coord(i.pos))
    
    
    running = True
    while running:
        for event in py.event.get():
            if event.type == py.QUIT:
                running = False
            
        screen.fill(BACKGROUND_COLOR)
        draw_board(screen)
        White.show(screen)
        py.display.flip()
    py.quit()
    sys.exit()

if __name__ == "__main__":
    main()







