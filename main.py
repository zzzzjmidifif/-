# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 02:58:15 2022

@author: jerry
"""
import sys
import random
def win(dengji1):
    dengji1+=5
    return dengji1
def lose(dengji1):
    dengji1-=1
    return dengji1
def ev(dengji):
    if(dengji==40):
        return True
    elif(dengji==80):
        return True
    else:
        return False
def fight(shu1,shu2,dengji1,dengji2):
    if(shu1=="火"):
        if(shu2=="水"):
            print("敌方为水系！你被克制了")
            if(dengji1>=2*dengji2):
                return True
            else:
                return False
        elif(shu2=="火"):
            if(dengji1>=dengji2):
                return True
            else:
                return False
        elif(shu2=="草"):
            if(dengji1*2>=dengji2):
                return True
            else:
                return False
    elif(shu1=="水"):
        if(shu2=="草"):
            print("敌方为草系！你被克制了")
            if(dengji1>=2*dengji2):
                return True
            else:
                return False
        elif(shu2=="水"):
            if(dengji1>=dengji2):
                return True
            else:
                return False
        elif(shu2=="火"):
            if(dengji1*2>=dengji2):
                return True
            else:
                return False
    else:
        if(shu2=="火"):
            print("敌方为火系！你被克制了")
            if(dengji1>=2*dengji2):
                return True
            else:
                return False
        elif(shu2=="草"):
            if(dengji1>=dengji2):
                return True
            else:
                return False
        elif(shu2=="水"):
            if(dengji1*2>=dengji2):
                return True
            else:
                return False
def move(p,local):
    if (p=="上"):
        local.y+=1
    elif (p=="下"):
        local.y-=1
    elif (p=="左"):
        local.x-=1
    elif (p=="右"):
        local.y-=1
    else:
        print("输入方向无效")
        return 0
class bkm:
  def __init__(self,name, shu,dengji):
    self.name = name
    self.shu = shu
    self.dengji=dengji
class local:
  def __init__(self, x,y):
    self.x = x
    self.y = y
list1=[0,1,2,3,4,5,6,7,8,9]
dict1=[bkm("火焰鸟","火",7),bkm("火伊布","火",14),bkm("炎武王","火",50),bkm("烈焰马","火",30),bkm("巨沼怪","水",50),bkm("白海狮","水",35),bkm("可达鸭","水",11),bkm("可达鸭","水",6),bkm("小磁怪","草",20),bkm("豆豆鸽","草",4),bkm("霸王花","草",57)]
小火龙 = bkm("小火龙","火",10)
妙蛙种子 = bkm("妙蛙种子","草",10)
杰尼龟 = bkm("杰尼龟","水",10)
local = local(0,0)
print("创建自己的宝可梦")
print("选择自己的初始宝可梦")
print("小火龙，属性：火")
print("妙蛙种子，属性：草")
print("杰尼龟，属性：水")
length=0
name=input()
if(name == 小火龙.name):
    print("名字："+小火龙.name+" 属性："+小火龙.shu)
elif(name == 妙蛙种子.name):
    print("名字："+妙蛙种子.name+" 属性："+妙蛙种子.shu)
elif(name == 杰尼龟.name):
    print("名字："+杰尼龟.name+" 属性："+杰尼龟.shu)
else:
    print("你选择的宝可梦无效")
    sys.exit()
dengji1=dengji2=dengji3=1
while True:
    print("选择你前进的方向")
    direct = input()
    move(direct,local)
    length+=1
    if(length==2):
        print("遇到野生宝可梦:")
        length=0
        num=random.choice(list1)
        print(dict1[num].name)
        if(name==小火龙.name):
            if(fight(小火龙.shu,dict1[num].shu,小火龙.dengji,dict1[num].dengji)==True):
                小火龙.dengji=win(小火龙.dengji)
                print("WIN")
                print("恭喜你！成长5级")
                if(dengji1==1):
                    if(小火龙.dengji>=40):
                            dengji1+=1
                            print("恭喜你！小火龙到达40级，进化为火恐龙")
                elif(dengji1==2):
                    if(小火龙.dengji>=80):
                        dengji1+=1
                        print("恭喜你！火恐龙到达80级，进化为喷火龙")
            else:
                小火龙.dengji=lose(小火龙.dengji)
                print("LOSE")
                print("很遗憾，下降一级")
        elif(name==妙蛙种子.name):
            if(fight(妙蛙种子.shu,dict1[num].shu,妙蛙种子.dengji,dict1[num].dengji)==True):
                妙蛙种子.dengji=win(妙蛙种子.dengji)
                print("WIN")
                print("恭喜你！成长5级")
                if(dengji2==1):
                    if(妙蛙种子.dengji>=40):
                            dengji2+=1
                            print("恭喜你！妙蛙种子到达40级，进化为妙蛙草")
                elif(dengji2==2):
                    if(妙蛙种子.dengji>=80):
                        dengji2+=1
                        print("恭喜你！妙蛙草到达80级，进化为妙蛙花")
            else:
                妙蛙种子.dengji=lose(妙蛙种子.dengji)
                print("LOSE")
                print("很遗憾，下降一级")
        else:
             if(fight(杰尼龟.shu,dict1[num].shu,杰尼龟.dengji,dict1[num].dengji)==True):
                 杰尼龟.dengji=win(杰尼龟.dengji)
                 print("WIN")
                 print("恭喜你！成长5级")
                 if(dengji3==1):
                    if(杰尼龟.dengji>=40):
                            dengji3+=1
                            print("恭喜你！杰尼龟到达40级，进化为卡咪龟")
                 elif(dengji3==2):
                    if(杰尼龟.dengji>=80):
                        dengji3+=1
                        print("恭喜你！卡咪龟到达80级，进化为水箭龟")
             else:
                 杰尼龟.dengji=lose(杰尼龟.dengji)
                 print("LOSE")
                 print("很遗憾，下降一级")
    if(小火龙.dengji>=100):
        print("恭喜你通关了")
        sys.exit()
    elif (小火龙.dengji<=0):
        print("你的宝可梦已经离开你了")
    if(妙蛙种子.dengji>=100):
        print("恭喜你通关了")
        sys.exit()
    elif (妙蛙种子.dengji<=0):
        print("你的宝可梦已经离开你了")
    if(杰尼龟.dengji>=100):
        print("恭喜你通关了")
        sys.exit()
    elif (杰尼龟.dengji<=0):
        print("你的宝可梦已经离开你了")
    


