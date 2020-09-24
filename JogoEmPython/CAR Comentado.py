import pygame, sys, random
from pygame.locals import *

def main():                                           #o jogo todo é posto em um def
    pygame.init()                                     #comeca o jogo
    tela = pygame.display.set_mode([400,650])         #define o tamanho da tela
    pygame.display.set_caption("JOGO")                #define o nome da janela em que o jogo é exibido
    relogio = pygame.time.Clock()                     #"relogio" é a variavel usada para definir o tick
    corbranca=(255,255,255)                           #define cor branca em hexagonal(usada para desenhar os obstaculos)
    explosao=pygame.mixer.Sound('colidiu_som.wav')           #define um som para ser usado quando o jogador perder

    class car (pygame.sprite.Sprite):                 #define os objetos usados em "CAR"
        def  __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.CAR = pygame.image.load('carro.png')  #define a imagem do carro
            self.rect = self.CAR.get_rect()            #a imagem agora é contornada por um retangulo
            self.rect.centerx = 200                    #o retangulo do carro vai comecar no pixel 200 do eixo x
            self.rect.centery = 500                    #o retangulo do carro vai comecar no pixel 500 do eixo y
            self.velocidade = 100                      #o carro é movimentado 100 pixels toda vez que se chama essa funcao

        def colocar(self):
            superficie.blit(self.CAR, self.rect)       #colocar o retangulo do carro na tela

        def movimento(self):                           #DEFINIR UM LIMITE PARA O CARRO, SO TEM TRES PISTAS ENTAO ELE NAO PODE PASSAR
            if self.rect.left <85:
               self.rect.left = 85
            if self.rect.right > 320:
                self.rect.right = 310
    move = 0

    jogador = car()
    imfundo = pygame.image.load('fundo.png')           #UPLOAD DA IMAGEM DE FUNDO
    imover = pygame.image.load('colidiu_imagem.png')   #UPLOAD DA IMAGEM DE GAMEOVER
    va = random.randint(1,3)                           #USADO PARA OS OBSTACULOS APARECEREM EM PISTAS ALEATORIAS
    verd = True

    while verd:
        move += 13                             #DEFINE A VELOCIDADE DO CARRO
        if move >= 650:
            va = random.randint(1,3)
            move = 0

        jogador.movimento()
        for event in pygame.event.get():         #USADO PARA DEFINIR OS EVENTOS DO JOGO ( QUANDO O USUARIO APERTA ALGUMA PARTE DO TECLADO OU DA TELA)
            if event.type == QUIT:               #SE O USUARIO APERAR EM SAIR NA TELA DO JOGO
                pygame.quit()

            if event.type == pygame.KEYDOWN:       #USADO PARA DEFINIR OS EVENTOS DE TECLADO ( QUANDO O USUARIO APERTA ALGUMA PARTE DO TECLADO )
                if event.key == pygame.K_LEFT:
                    jogador.rect.left -= jogador.velocidade

                if event.key == pygame.K_RIGHT:
                    jogador.rect.right += jogador.velocidade

        relogio.tick(100)                          #define a quantidade de frames por segundo
        tela.blit(imfundo, (0,-650+move))          #em que lugar a imagem de fundo comeca ( e usado para fazer ela rodar, dando sensação de movimento)
        tela.blit(imfundo, (0,move))

        if va == 1:
            obs = pygame.Rect(65,move,75,10)
            pygame.draw.rect(tela,corbranca,obs)

        if va == 2:
            obs = pygame.Rect(165,move,75,10)
            pygame.draw.rect(tela,corbranca,obs)

        if va == 3:
            obs = pygame.Rect(265,move,75,10)
            pygame.draw.rect(tela,corbranca,obs)

        if obs.colliderect(jogador):             #se houver colisao ( é mostrada a imagem de gameover e o som que foi upado anteriormente)
            explosao.play()
            tela.blit(imover,(0,270))
            pygame.quit()

        jogador.colocar(tela)
        pygame.display.update()


    main()                            #chamada a função do jogo
