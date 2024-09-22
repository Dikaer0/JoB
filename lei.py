class Dog: # 创建Dog类
  def __init__(self, name, age):
    self.name = name
    self.age = age
    ####初始化属性name和age

  def sit(self):
    print(f"{self.name} is now sitting.")
    ####模拟小狗收到命令坐下

  def roll_over(self):
    print(f"{self.name} rolled over!")
    ####模拟小狗收到命令打滚