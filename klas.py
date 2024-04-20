import pygame
from random import randint
import time

pygame.init()

window = pygame.display.set_mode((1280, 780))

pygame.display.set_caption("Zombie Rush")
ikona= pygame.image.load("ikonka.png")
pygame.display.set_icon(ikona)

class Button():
    def __init__(self,x_cord , y_cord):
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.button_img = pygame.image.load("graj_button.png")
        self.sw_button_img = pygame.image.load("graj_button_sw.png")
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.button_img.get_width(), self.button_img.get_width())

    def tick(self):
        if self.hitbox.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                return True

    def draw(self, window):
        if self.hitbox.collidepoint(pygame.mouse.get_pos()):
            window.blit(self.sw_button_img, (self.x_cord, self.y_cord))
        else:
            window.blit(self.button_img, (self.x_cord, self.y_cord))


class Player:
    def __init__(self):
        self.x_cord = 0
        self.y_cord = 0
        self.image = pygame.image.load("postac2.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.speed = 6
        self.hp = 3
        self.red_3_img = pygame.image.load("3_red.png")
        self.red_2_img = pygame.image.load("2_red.png")
        self.red_1_img = pygame.image.load("1_red.png")
        self.red_0_img = pygame.image.load("0_red.png")


    def tick(self, keys):  # wykonuje sie pokażdym przjsciu petli
        if keys[pygame.K_w]:
            self.y_cord -= self.speed
        if keys[pygame.K_s]:
            self.y_cord += self.speed
        if keys[pygame.K_a]:
            self.x_cord -= self.speed
        if keys[pygame.K_d]:
            self.x_cord += self.speed

    def draw(self):  # drukuje postac na ekranie
        if self.x_cord <= 0:
            self.x_cord = 0
        if self.x_cord >= 220:
            self.x_cord = 220
        if self.y_cord <= 70:
            self.y_cord = 70
        if self.y_cord >= 780 - self.height - 80:
            self.y_cord = 780 - self.height - 80

        window.blit(self.image, (self.x_cord, self.y_cord))

        if self.hp == 3:
            window.blit(self.red_3_img, (30, 700))
        elif self.hp == 2:
            window.blit(self.red_2_img, (30, 700))
        elif self.hp == 1:
            window.blit(self.red_1_img, (30, 700))
        elif self.hp == 0:
            window.blit(self.red_0_img, (30, 700))


class Pocisk:
    def __init__(self):
        self.x_cord = 0
        self.y_cord = 0
        self.speed = 18
        self.img = pygame.image.load("nabój.png")
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.state = "ready"
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
        self.ready_img = pygame.image.load("bullet_ready.png")
        self.fire_img = pygame.image.load("bullet_fire.png")

    def tick(self, keys):
        if keys[pygame.K_SPACE]:
            self.state = "fire"
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)


    def draw(self, x, y, img):
        if self.state == "fire":
            window.blit(img, (x, y))

class Zombie:
    def __init__(self):
        self.image = pygame.image.load("zombie.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x_cord = 1400
        self.y_cord = randint(50, 550)
        self.speed = 5
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def tick(self):
        self.x_cord -= self.speed
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def draw(self):
        window.blit(self.image, (self.x_cord, self.y_cord))