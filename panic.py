#书之68页
#以及书之82页
#将Don't panic替换为on tap

phrase="Don't panic!"
plist=list(phrase)
print(phrase)
print(plist)



#for i in range(4):
#    plist.pop()#先去掉最后的nic!
#plist.pop(0)
#去掉第一位的D
#plist.remove("'")#去掉Don后的'
#现在是ont pa 一共六位
#plist.extend([plist.pop(5),plist.pop(4)])#第五位是p，第六位是a
#现在是ont ap
#plist.insert(2,plist.pop(3))
#把空格粘贴到on之后
#new_phrase=''.join(plist)
#将列表转换为字符串


#下面两行代码可替换上面注释掉的代码，实现同样的功能
new_phrase=''.join(plist[1:3])#注意第二个stop值不被包括在其中，如第四个字符不包括在new_phrase中
new_phrase=new_phrase+''.join([plist[5],plist[4],plist[-5],plist[-6]])





print(plist)
print(new_phrase)

