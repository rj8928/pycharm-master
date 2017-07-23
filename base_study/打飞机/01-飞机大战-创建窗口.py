#coding=utf_8
import sys
import pygame
from pygame.locals import*
import time


class HeroPlane(object): #创建飞机类
    def __init__(self,screen_temp):
        self.x = 210
        self.y = 700
        self.screen = screen_temp
        self.image = pygame.image.load("./feiji/hero1.png")
        self.bullet_list = []
    
    
    #显示飞机,子弹
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
    #左移
    def move_left(self):
        self.x -=5
    #右移
    def move_right(self):
        self.x +=5
    #上移
    def move_up(self):
        self.y -=5
    #下移
    def move_down(self):
        self.y +=5
    #开火
    def fire(self):
        self.bullet_list.append(Bullet(self.screen,self.x,self.y))

#创建子弹类
class Bullet(object):
    def __init__(self,screen_temp,x,y):
        self.x = x+40
        self.y = y-20
        self.demage = 10
        self.screen = screen_temp
        self.image = pygame.image.load("./feiji/bullet.png")
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))

    def move (self):
        self.y -= 20
    





def scan_keybound(self):
    
    for event in pygame.event.get():

#判断是否是点击了退出按钮
        if event.type == QUIT:
            print("exit")
            exit()
        #判断是否是按下了键
        elif event.type == KEYDOWN:
        #检测按键是否是a或者left
                    if event.key == K_a or event.key == K_LEFT:
                        print('left')
                        self.move_left()
                #检测按键是否是d或者right
                    elif event.key == K_d or event.key == K_RIGHT:
                        print('right')
                        self.move_right()
                #检测按键是否是空格键
                    elif event.key == SPACE:
                        print('space')
                        self.fire()

def main():

#1. 创建一个窗口，用来显示内容
        screen = pygame.display.set_mode((480,852),0,32)


#2. 创建一个窗口大小的图片，用来充当背景
        background = pygame.image.load("./feiji/background.png")
        hero =HeroPlane(screen) 
        while True:
        #把背景图贴到窗口
            screen.blit(background,(0,0))
            hero.display()
            #加载图片
            pygame.display.update()
            #设置休眠时间，节省内存
            scan_keybound(hero)
            time.sleep(0.01)
    










if __name__ == "__main__":
    main()
 
    


