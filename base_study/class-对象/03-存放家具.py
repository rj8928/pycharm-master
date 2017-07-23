#1. 买栋房子
class Home:
    def __init__(self,new_area,new_info,new_addr):
        self.area = new_area
        self.info = new_info
        self.addr = new_addr
        self.left_area = new_area
        self.contain_items = []
    def __str__(self):
        return "房子的面积是：%d\t户型是：%s\t地址是：%s\t家具有：%s"%(self.left_area,self.info,self.addr,str(self.contain_items))
    def add_item(self,item):
        #self.left_area -= item.area
        #self.contain_items.append(item.name)
        self.left_area -= item.get_area()
        self.contain_items.append(item.get_name())

class Bed:
    def __init__(self,new_name,new_area):
        self.name = new_name
        self.area = new_area
    def __str__(self):
        return "%s占用的面积是%d"%(self.name,self.area)

    def get_name(self):
        return self.name
    
    def get_area(self):
        return self.area

#调用对象        
fangzi = Home(129,"别墅","江西")
print(fangzi)
bed1 = Bed("弹簧床",4)
print(bed1)
fangzi.add_item(bed1)
print(fangzi)
bed2 = Bed("席梦思",6)
fangzi.add_item(bed2)
print(fangzi)
