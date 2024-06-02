import random as r

hp=114514
hpe=114514
bh=0
power=0
step=3

#角色名称
name="被憎恶的守护骑士"
enemy="『代行者』"

#技能名称
c1="痛苦恩赐"
c2="以『守护骑士』之名"
c3="保护的决心"

#技能台词
c1t="我将这痛苦赐予你"
c2t="堵上守护骑士的名号，我绝不退缩！"
c3t="就算被人厌恶，也不会改变我作为守护骑士的决心！"

#基础行动
def 攻击(w):
  global hpe
  hpe=hpe-w
def 受击(y):
  global hp
  hp=hp-y
  
#进阶行动
def 守护之心(x):
  global bh
  bh=bh+x
def 终极技能(w):
  global power
  if power==3:
    global hpe
    print(c3t)
    ls=1234*w
    hpe=hpe-ls
    power=0
    print("造成了",ls,"点巨量伤害")
    main()
  else:
    print("能量不足！")
    main()
def 充能(y):
  global power
  ls=power+y
  if ls<=3:
    power=ls
  else:
    power=3
def 胜负判断():
  if hp<=0:
    print("你输了！")
    exit()
  elif hpe<=0:
    print("你赢了！")
    exit()
#对手行动
def 对手():
  ls=r.randint(0,59)
  a=r.randint(ls,150)
  受击(a)
  print("对手对你造成了",a,"点伤害，叠加了一层守护之心")
  守护之心(1)

#主界面
def main():
  对手()
  胜负判断()
  print()
  print(name,"剩余生命值",hp)
  print(enemy,"剩余生命值",hpe)
  print("“守护之心”层数",bh)
  print("充能(满3可释放终极技能)",power)
  print("剩余行动点数",step)
  print()
  战斗()
def 战斗():
  print()
  global step
  b=r.randint(0,59)
  a=r.randint(b,200)
  print("1◎普通攻击：",c1)
  print("2◎技能：",c2)
  print("3◎终极技能：",c3)
  choice=int(input("输入你的选择："))
  if choice==1:
    ls=step+1
    if ls<=3:
      step=ls
    print(c1t)
    print()
    攻击(a*5)
    print("造成了",a*5,'点伤害')
    充能(choice)
    main()
  elif choice==2:
    ls=step-1
    if ls<=0:
      print("行动点数不足！")
      main()
    else:
      step=ls
      print(c2t)
      print()
      攻击(a*10)
      print("造成了",a*10,"点伤害")
      充能(choice)
      main()
  else:
    终极技能(bh)

main()