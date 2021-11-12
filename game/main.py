import pygame
import sys

from game.personagem.main import Character


##CONSTANTES

FPS = 60



##Inicializa o jogo
pygame.init()

##Cria a display surface com 800 de LARGURA e 400 de ALTURA
screen = pygame.display.set_mode((800,400))

##Criando um clock que limita o gameloop
clock = pygame.time.Clock()

##Titulo do jogo na janela.
pygame.display.set_caption("For me it's about destiny")






##GAME LOOP
def main():
    while True:
        
        ##Nesse loop criamos os eventos e adicionamos na lista 
        ##que estavamos loopando.
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                
                pygame.quit()
                sys.exit()
        
        henrique = Character("Henrique",100,200)
        
        henrique.stopped()
        
        ##Faz update da display surface com tudo que adicionamos
        pygame.display.update()
        
        ##limita quantas vezes o gameloop vai rodar por segundo.
        clock.tick(FPS)


if __name__ == "__main__":
    main()