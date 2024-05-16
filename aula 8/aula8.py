#Título: Inimigos movimentos randômicos e game over
#link do material da aula: https://bit.ly/pythontela01
#saiba mais: comentários do autor - https://vemfazermatematicaegames.blogspot.com/2020/05/pygames-construindo-inimigos-com.html

import pygame, sys
import math
import random
import time

pygame.init()

largura_janela = 1800   
altura_janela = 900
pygame.display.set_caption('jogo da galinha')
clock = pygame.time.Clock()

fgExit = False

personagemImg = pygame.image.load('galinha.png')
personagem2Img = pygame.image.load('ovo.png')
cenario = pygame.image.load('cenario.jpg')
DEFAULT_IMAGE_SIZE = (2000, 1000) #tamanho do cenario
escala = (2000, 1000)
inexistir = (0, 0)
cenario = pygame.transform.scale(cenario, DEFAULT_IMAGE_SIZE)

DEFAULT_IMAGE_SIZE = (100, 100) #tamando do personagem
escala = (2000, 1000)
inexistir = (0, 0)
personagem2Img = pygame.transform.scale(personagem2Img, DEFAULT_IMAGE_SIZE)
personagemImg = pygame.transform.scale(personagemImg, DEFAULT_IMAGE_SIZE)

somdefundo = pygame.mixer.music.load('som de fundo.mp3')
pygame.mixer.music.set_volume(1.5)
pygame.mixer.music.play(-1)

fonte = pygame.font.SysFont("dejavusans", 30)
textoperdeu = fonte.render("Você perdeu! Reiniciei o jogo!", True, (255,0,0))
texto0 = fonte.render("Clique com o mouse para instruções.", True, (255,0,0))
texto1 = fonte.render("Olá gamer, seja bem vindo ao jogo do Mário!", True, (255,0,0))
texto2 = fonte.render("Vamos começar a jogar?", True, (255,0,0))
texto3 = fonte.render("Use as setas para se movimentar.", True, (255,0,0))
texto4 = fonte.render("Desvie do cogumelo para ficar vivo!", True, (255,0,0))
texto5 = fonte.render("Obrigado por prestigiar esse game!", True, (255,0,0))
contador = 0

tela = pygame.display.set_mode((largura_janela, altura_janela))
x = (largura_janela * 0.1)
y = (altura_janela * 0.1)
x1 = 0
x2 = 0
y1 = 0
y2 = 0
personagem_speed = 0

xgalinha = x+45
ygalinha = y+65
xcogumelo = 500+128 #atenção! 128 é o raio do meu cogumelo!
ycogumelo = 300+128
x_1 = x
y_1 = y
t = 0


def colidiu():
    distancia =  math.sqrt(math.pow(xgalinha-xcogumelo,2)+math.pow(ygalinha-ycogumelo,2))
    print (distancia)
    if distancia<128+50:
        return True
    else:
        return False
    
while not fgExit:
    t = t + 1.5
    xcogumelo = 1000+ 1000 * math.cos( 0.01*t)+ 40 * math.cos( 0.09*t +0.3) #velocidade e em consequencia onde o personagem alcança
    ycogumelo = 500 + 500 * math.sin( 0.005* t)-40 * math.sin( 0.06*t)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fgExit = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            contador = contador +1
            if contador == 1:
               tela.fill((0,0,0))
               tela.blit(texto1, (0,550))
            if contador == 2:
               tela.fill((0,0,0))
               tela.blit(texto2, (0,550))
            if contador == 3:
               tela.fill((0,0,0))
               tela.blit(texto3, (0,550))
            if contador == 4:
               tela.fill((0,0,0))
               tela.blit(texto4, (0,550))
            if contador == 5:
               tela.fill((0,0,0))
               tela.blit(texto5, (0,550))
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x1 = 0
            if event.key == pygame.K_RIGHT:
                x2 = 0
            if event.key == pygame.K_UP:
                y1 = 0
            if event.key == pygame.K_DOWN:
                y2 = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1 = -5
                
            if event.key == pygame.K_RIGHT:
                x2 = 5
                
            if event.key == pygame.K_UP:
                y1 = -5
               
            if event.key == pygame.K_DOWN:
                y2 = 5
    x += x1 + x2
    y += y1 + y2
    xgalinha = x+45
    ygalinha = y+65
    if colidiu():
        tela.fill((0,0,0))
        tela.blit(textoperdeu, (150,300))
        pygame.display.update()
        time.sleep(4)
        pygame.quit()
        x = x_1
        y = y_1                       
    else:
        x_1 = x
        y_1 = y
    tela.blit(cenario,(0,0))
    tela.blit(personagemImg, (x, y))
    tela.blit(personagem2Img, ( xcogumelo -128 , ycogumelo -128 ))
    pygame.display.update()
    clock.tick(60)

pygame.quit()
