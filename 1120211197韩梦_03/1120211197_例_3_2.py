#编写程序，使用for语句计算1～10000的偶数自然数之和。
total = 0
for iNum in range(2,10001,2):
    total += iNum
print("1~10000的总和为：{}".format(total))