#编程实现统计任意数的20次幂的值和位数
a=int(input('请输入底数：'))
b=int(input('请输入幂数：'))

def power(a,b):
    s=a**b
    return s

print(a,'^',b,'=',power(a,b))
print(len(str(power(a,b))))
