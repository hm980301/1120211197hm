#利用python的print()函数写一篇作文
#要求必须覆盖以下列表操作
#评分标准：文字优美，包含知识点越多越好！
#记一次有趣的生日排队
#今天，是我的生日。
#我在一个星期前就和我的好朋友们说好了，让他们来我家参加我的生日派对。
#我的好朋友有{}个，第1个好朋友是{}，第2个好朋友是{}，剩下的好朋友们是{}。
#当然，如果按名字排序的话，那就是{}了。
#但是，昨天，{}告诉我说，他不能来参加我的生日派对了，因为{}
#那我只能把他从我的嘉宾名单中删除咯。现在，能来的就剩下这些{}了。
#人数好像有些不够啊，那我再叫一些人来吧。对了，把{}和{}给叫过来好了，这些的话，就有这些人来了{}。
friend_list=["Judy","Bob","Sun","John","Elle","Sindy"]
print("今天，是我的生日。")
print("我在一个星期前就和我的好朋友们说好了，让他们来我家参加我的生日派对")
print("我的好朋友有{}个".format(len(friend_list)))
print("第1个好朋友是{}".format(friend_list[0]))
print("第2个好朋友是{}".format(friend_list[1]))
print("剩下的好朋友们是{}".format(friend_list[2:]))
friend_list.sort()
print("当然，如果按名字排序的话，那就是{}了。".format(friend_list))
result="出差无法赶来"
name1="Sindy"
print("但是，昨天，{}告诉我说，他不能来参加我的生日派对了，因为{}".format(name1,result))
friend_list.remove("Sindy")
print("那我只能把他从我的嘉宾名单中删除咯。现在，能来的就剩下这些{}了".format(friend_list))
print("人数好像有些不够啊，那我再叫一些人来吧。")
friend_list.append("Mile")
friend_list.append("Lisa")
print("对了，把{}和{}给叫过来好了，这些的话，就有这些人来了{}。".format(friend_list[-2],friend_list[-1],friend_list))

