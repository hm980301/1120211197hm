#编程实现，分别输入身高和体重，输出BMI值，并保留1位小数 BMI值 = 体重（公斤）/ （ 身高(米) * 身高(米) ）


#请使用 input 获取键盘输入
height =float(input("你的身高（米）："))
#请使用 input 获取键盘输入
weight =float(input("你的体重（公斤）："))
bmi = weight / (height ** 2)
print(bmi)
