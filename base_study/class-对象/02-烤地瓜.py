class SweetPotato:
    def __init__(self):
        self.cookedString = "生的"
        self.cookedLevel = 0
        self.cindiments = []
    def __str__(self):
        return "地瓜的状态：%s(%d分钟,佐料有：%s)"%(self.cookedString,self.cookedLevel,str(self.cindiments))
    def cook(self,cooked_time):
        self.cookedLevel+=cooked_time
        if self.cookedLevel>=0 and self.cookedLevel<3:
            self.cookedString="生的"
        elif self.cookedLevel>=3 and self.cookedLevel<5:
            self.cookedString="半生不熟"
        elif self.cookedLevel>=5 and self.cookedLevel<8:
            self.cookedString="熟了"
        elif self.cookedLevel>=8:
            self.cookedString="糊了"
    def addCondiment(self,item):
        self.cindiments.append(item)

#创建一个地瓜对象
di_gua = SweetPotato()
di_gua.cook(1)
di_gua.cook(9)
di_gua.cook(6)
di_gua.addCondiment("大蒜，孜然")
print(di_gua)
