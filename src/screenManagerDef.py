### Screen Manager Definition ###

import pygame, sys, os

class ScreenManagerDef:
    def __init__(self, ScreenX, ScreenY, FullScreen):
        self.x = ScreenX
        self.y = ScreenY
        self.fullScreen = FullScreen

        self.screen = pygame.display.set_video_mode((self.x, self.y))

        if self.fullScreen: pygame.display.toggle_fullscreen()

    def blit(self, Surface, X, Y): self.screen.blit(Surface, (X,Y))
    
