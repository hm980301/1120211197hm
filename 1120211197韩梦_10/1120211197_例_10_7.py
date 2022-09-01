#去除每行首尾的空格/换行符
path1 = "students.txt"
f1 = open(path1,'r',encoding='utf-8')
for line1 in f1.readlines():
    newline1 = line1.rstrip()
    newwords1 = newline1.split(",")
    print(newwords1)
f1.close()