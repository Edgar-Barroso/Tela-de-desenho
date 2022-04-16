import pygame
import random
import cv2
import numpy as np
import torch
from torch import nn, optim
from torchvision import datasets
from torchvision import transforms
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt
import time

largura = 800
altura = 600

cor_branca = (255, 255, 255)
cor_pincel = (80, 11, 200)


def main(frames):
    pygame.init()
    tela = pygame.display.set_mode([largura, altura])
    tela.fill(cor_branca)
    relogio = pygame.time.Clock()
    sair = False
    while sair is False:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pintar = True
                while pintar:
                    pygame.display.update()
                    x, y = pygame.mouse.get_pos()
                    pygame.draw.circle(tela, (random.random() * 255, random.random() * 255, random.random() * 255),(x, y), 8)
                    for event2 in pygame.event.get():
                        if event2.type == pygame.MOUSEBUTTONUP:
                            pintar = False
                            break
                break
            if event.type == pygame.QUIT:
                sair = True
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    tela = pygame.display.set_mode([largura, altura])
                    tela.fill(cor_branca)
        relogio.tick(frames)
        pygame.display.update()
    pygame.image.save(tela, 'tela.jpeg')
    pygame.quit()


if __name__ == '__main__':
    frames = 120
    main(frames)
