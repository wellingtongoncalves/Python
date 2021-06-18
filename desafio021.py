'''from playsound import playsound
playsound('english.mp3')'''

import pygame
pygame.init()
pygame.mixer.music.load('english.mp3')
pygame.mixer.music.play()
pygame.event.wait()
input('Escreve qlq coisa aqui')