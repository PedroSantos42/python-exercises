import pygame

# para funcionar deve haver um arquivo nesta pasta com o nome Desafio021.mp3

pygame.init()
pygame.mixer.music.load('Desafio021.mp3')
pygame.mixer.music.play()
pygame.event.wait()