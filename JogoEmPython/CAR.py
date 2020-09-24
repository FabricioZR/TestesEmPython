import pygame, sys, random
from pygame.locals import *
import os
import time

def main():
    pygame.init()
    tela = pygame.display.set_mode([400,650])
    pygame.display.set_caption("JOGO")
    relogio = pygame.time.Clock()
    corbranca=(255,255,255)
    explosao=pygame.mixer.Sound('colidiu_som.wav')
    imover = pygame.image.load('colidiu_imagem.png')

    def colidiu():
        print ("SEUS PONTOS SAO:", pontos)
        tela.blit(imover, (0, 270))
        explosao.play()
        pygame.display.update()
        time.sleep(3)
        pygame.quit()
        


    class car (pygame.sprite.Sprite):

        def  __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.CAR = pygame.image.load('carro.png')
            self.rect = self.CAR.get_rect()
            self.rect.centerx = 200
            self.rect.centery = 500
            self.velocidade = 100

        def colocar(self, superficie):
            superficie.blit(self.CAR, self.rect)

        def movimento(self):
            if self.rect.left <85:
               self.rect.left = 85
            if self.rect.right > 320:
               self.rect.right = 320
    move = 0

    jogador = car()
    imfundo = pygame.image.load('fundo.png')
    
    va = random.randint(1,3)
    verd = True
    pontos=0
    while verd:
        pontos+=1
        move += 12
        if move >= 650:
            va = random.randint(1,3)
            move = 0
        jogador.movimento()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    jogador.rect.left -= jogador.velocidade

                if event.key == pygame.K_RIGHT:
                    jogador.rect.right += jogador.velocidade

        relogio.tick(100)
        tela.blit(imfundo, (0,-650+move))
        tela.blit(imfundo, (0,move))
        if va == 1:
            obs = pygame.Rect(65,move,75,10)
            pygame.draw.rect(tela,corbranca,obs)
            obs1 = pygame.Rect(165,move,75,10)
            pygame.draw.rect(tela,corbranca,obs1)
        if va == 2:
            obs = pygame.Rect(165,move,75,10)
            pygame.draw.rect(tela,corbranca,obs)
            obs1 = pygame.Rect(265,move,75,10)
            pygame.draw.rect(tela,corbranca,obs1)
        if va == 3:
            obs = pygame.Rect(265,move,75,10)
            pygame.draw.rect(tela,corbranca,obs)
            obs1 = pygame.Rect(65,move,75,10)
            pygame.draw.rect(tela,corbranca,obs1)
        if obs.colliderect(jogador):
            colidiu()
        if obs1.colliderect(jogador):
            colidiu()    


        jogador.colocar(tela)
        pygame.display.update()



main()
