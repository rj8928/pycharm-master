class Person(object):
#人
    def __init__(self,name):
        super(Person,self).__init__()
        self.name = name #人名
        self.gun = None #枪对象的引用
        self.hp = 100
    def anzhuang_zidan(self,dan_jia_temp,zi_dan_temp):
        #把子弹装到弹夹
        #弹夹.保存子弹（子弹）
        dan_jia_temp.save(zi_dan_temp)
    
    def anzhuang_danjia(self,gun_temp,dan_jia_temp):
        #把弹夹装到枪
        gun_temp.baocun_danjia(dan_jia_temp)
    def naqiang(self,gun_temp):
        self.gun = gun_temp

    def __str__(self):
        if self.hp >0:
            if self.gun:
                return "%s的血量为%d，有枪 %s"%(self.name,self.hp,self.gun)
            else:
                return "%s的血量为%d，没枪"%(self.name,self.hp)
        else:
            return "%s已经死了"%self.name
    def koubanji(self,diren):
        #开枪打敌人
        #枪开火
        self.gun.fire(diren)

    def diaoxue(self,shanghai):
        #根据伤害掉血
        self.hp -=shanghai
class Gun(object):
#枪
    def __init__(self,name):
        super(Gun,self).__init__()
        self.name = name #枪名
        self.danjia = None 
    def baocun_danjia(self,dan_jia_temp):
        self.danjia = dan_jia_temp #保存弹夹

    def __str__(self):
        if self.danjia:
            return "枪的信息：%s，%s"%(self.name,self.danjia)
        else:
            return "枪的信息：%s"%(self.name)
    def fire(self,diren):
        #开火
        #先从弹夹中取子弹
        zidan_temp = self.danjia.quzidan()
        if zidan_temp:
            zidan_temp.dazhong(diren)
        else:
            print("弹夹中没子弹了")
class Dan_jia(object):
#弹夹
#zidan_num = 0
    def __init__(self,max_arg ):
        super(Dan_jia,self).__init__()
        self.max_arg = max_arg  #子弹数
        self.zidan_list = [] #保存所有子弹的引用   
    def save(self,zi_dan_temp):
        #将子弹保存
        self.zidan_list.append(zi_dan_temp)

    def __str__(self):
        return "弹夹的信息为：%d/%d"%(len(self.zidan_list),self.max_arg)
    
    def quzidan(self):
        #弹出最上面的子弹
        if self.zidan_list:
            return self.zidan_list.pop()
class Zi_dan(object):
#子弹
    def __init__(self,shanghai):
        super(Zi_dan,self).__init__()
        self.shanghai = shanghai #子弹伤害
    def dazhong(self,diren):
        #让敌人掉血
        diren.diaoxue(self.shanghai)

def main():
    #用来控制整个程序
    
    #1. 创建老王对象
    laowang = Person("老王") 
    #2. 创建枪对象
    ak47 = Gun("ak47")
    #3. 创建一个弹夹对象
    danjia = Dan_jia(20)
    #4. 创建一些子弹
    for i in range(15):
        zidan = Zi_dan(10)#数字为杀伤力
    #5. 创建一个敌人
    
    #6. 老王把子弹装到弹夹
        laowang.anzhuang_zidan(danjia,zidan)
    #7. 老王把弹夹装到枪中
    laowang.anzhuang_danjia(ak47,danjia)
    #8. 老王拿枪
    laowang.naqiang(ak47)
    #创建敌人
    gebi_laosong = Person("隔壁老宋")
    #test
    #print(gebi_laosong)
    #print(danjia)
    #print(ak47)
    #print(laowang)
    #老王开枪打敌人
    #老王.扣扳机(隔壁老宋)
    print(laowang)
    print(gebi_laosong)
    laowang.koubanji(gebi_laosong)
    print(laowang)
    print(gebi_laosong)
    laowang.koubanji(gebi_laosong)
    print(laowang)
    print(gebi_laosong)
    laowang.koubanji(gebi_laosong)
    print(laowang)
    print(gebi_laosong)
    laowang.koubanji(gebi_laosong)
    print(laowang)
    print(gebi_laosong)
    laowang.koubanji(gebi_laosong)
    print(laowang)
    print(gebi_laosong)
    laowang.koubanji(gebi_laosong)
    print(laowang)
    print(gebi_laosong)
    laowang.koubanji(gebi_laosong)
    print(laowang)
    print(gebi_laosong)
    laowang.koubanji(gebi_laosong)
    print(laowang)
    print(gebi_laosong)
    laowang.koubanji(gebi_laosong)
    print(laowang)
    print(gebi_laosong)
    laowang.koubanji(gebi_laosong)
    print(laowang)
    print(gebi_laosong)
    laowang.koubanji(gebi_laosong)
    print(laowang)
    print(gebi_laosong)
    laowang.koubanji(gebi_laosong)
    print(laowang)
    print(gebi_laosong)
    laowang.koubanji(gebi_laosong)
    print(laowang)
    print(gebi_laosong)
    

if __name__ == '__main__':
        main()





