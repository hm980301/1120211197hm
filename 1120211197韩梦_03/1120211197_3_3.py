#编写程序，从键盘输入a,b,c的值，计算一元二次方程ax^2+bx+c=0的根，根据b^2−4ac的值大于0、等于0及小于0分别进行讨论
import math
# 读取输入，整数或小数
a = float(input("请输入a值："))
b = float(input("请输入b值："))
c = float(input("请输入c值："))

# 判断是否有实数解
if (b ** 2 - 4 * a * c) < 0:  # 无实数解
   print("该二次函数无实数解！！！")
else:  # 有实数解
   x1 = round((- b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a), 2)
   x2 = round((- b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a), 2)
   print("二次函数的解为：")
   print("x1 =", x1)
   print("x2 =", x2)