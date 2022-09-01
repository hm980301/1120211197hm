#读入全部文本内容，返回结果为一个字符串
path1 = "lemontree.txt"
f1 = open(path1,'r',encoding='utf-8')
content = f1.read()
print(content)
f1.close()