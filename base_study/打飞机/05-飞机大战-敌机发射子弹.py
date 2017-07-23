#coding=utf_8
import sys
import pygame
from pygame.locals import*
import time
import random


class HeroPlane(object): #创建飞机类
    def __init__(self,screen_temp):
        self.x = 210
        self.y = 600
        self.screen = screen_temp
        self.image = pygame.image.load("./feiji/hero1.png")
        self.bullet_list = []
    #显示飞机,子弹
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge():
                self.bullet_list.remove(bullet)
                
    #左移
    def move_left(self):
        self.x -=15
    #右移
    def move_right(self):
        self.x +=15
    #上移
    def move_up(self):
        self.y -=5
    #下移
    def move_down(self):
        self.y +=5
    #开火
    def fire(self):
        self.bullet_list.append(Bullet(self.screen,self.x,self.y))
 

class EnemyPlane(object): #创建敌机
    def __init__(self,screen_temp):
        self.x = 0
        self.y = 0
        self.screen = screen_temp
        self.image = pygame.image.load("./feiji/enemy0.png")
        self.direction = "right"
        self.bullet_list = []
    #显示飞机,子弹
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge():
                self.bullet_list.remove(bullet)
    def move(self):
        if self.direction == "right":
            self.x +=5
        else:
            self.x -=5
        if self.x >430:
            self.direction = "left"
        elif self.x <0:
            self.direction = "right"
    #开火
    def fire(self):
        random_num = random.randint(1,100)
        if random_num == 8 or random_num == 20:
            self.bullet_list.append(EnemyBullet(self.screen,self.x,self.y))
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
    
    def judge(self):
        if self.y<0:
            return True
        else:
            return False


class EnemyBullet(object):
    def __init__(self,screen_temp,x,y):
        self.x = x+25
        self.y = y+40
        self.demage = 10
        self.screen = screen_temp
        self.image = pygame.image.load("./feiji/bullet1.png")
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
    def move (self):
        self.y += 15
    
    def judge(self):
        if self.y>852:
            return True
        else:
            return False



#键盘检测
def scan_keybound(self):
    for event in pygame.event.get():
#判断是否是点击了退出按钮
        if event.type == pygame.QUIT:
            print("exit")
            exit()
        #判断是否是按下了键
        elif event.type == pygame.KEYDOWN:
        #检测按键是否是a或者left
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                print('左')
                self.move_left()
                #self.fire()
            #检测按键是否是d或者right
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                print('右')
                self.move_right()
                #self.fire()
            #检测按键是否是空格键
            elif event.key == pygame.K_UP:
                print('开火')
                self.fire()

def main():
#1. 创建一个窗口，用来显示内容
        screen = pygame.display.set_mode((480,852),0,32)

#2. 创建一个窗口大小的图片，用来充当背景
        background = pygame.image.load("./feiji/background.png")
        hero =HeroPlane(screen) 
        diji =EnemyPlane(screen)
        while True:
        #把背景图贴到窗口
            screen.blit(background,(0,0))
            hero.display()
            diji.display()
            diji.move()
            diji.fire()
            #加载图片
            pygame.display.update()
            #设置休眠时间，节省内存
            scan_keybound(hero)
            time.sleep(0.01)
    










if __name__ == "__main__":
    main()
 
    


