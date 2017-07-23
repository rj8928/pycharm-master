class Person(object):
#人
    def __init__(self,name):
        super(Person,self).__init__()
        self.name = name #人名
    def anzhuang_zidan(self,dan_jia_temp,zi_dan_temp):
        #把子弹装到弹夹
        #弹夹.保存子弹（子弹）
        dan_jia_temp.save(zi_dan_temp)
    
    def anzhuang_danjia(self,gun_temp,dan_jia_temp):
        #把弹夹装到枪
        gun_temp.baocun_danjia(dan_jia_temp)



class Gun(object):
#枪
    def __init__(self,name):
        super(Gun,self).__init__()
        self.name = name #枪名
        self.danjia = None 
    def baocun_danjia(self,dan_jia_temp):
        self.danjia = dan_jia_temp #保存弹夹


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



class Zi_dan(object):
#子弹
    def __init__(self,shanghai)
        super(Zi_dan,self).__init__()
        self.shanghai = shanghai #子弹伤害


def main():
    #用来控制整个程序
    
    #1. 创建老王对象
    laowang = Person("老王") 
    #2. 创建枪对象
    ak47 = Gun("ak47")
    #3. 创建一个弹夹对象
    danjia = Dan_jia(20)
    #4. 创建一些子弹
    zidan = Zi_dan(10)#数字为杀伤力
    #5. 创建一个敌人
    
    #6. 老王把子弹装到弹夹
    laowang.anzhuang_zidian(danjia,zidan)
    #7. 老王把弹夹装到枪中
    laowang.anhuang_danjia(ak47,danjia)
    #8. 老王拿枪
    #老王开枪打敌人
if __name__ == '__main__':
    main()
