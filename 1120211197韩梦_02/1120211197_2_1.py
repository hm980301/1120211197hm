#数字输出：编程实现，从键盘输入一个5位数字，分别输出它的个位数和千位数
a = input()

print("万位是: %s" % str(a)[0])
print("千位是: %s" % str(a)[1])
print("百位是: %s" % str(a)[2])
print("十位是: %s" % str(a)[3])
print("个位是: %s" % str(a)[4])

