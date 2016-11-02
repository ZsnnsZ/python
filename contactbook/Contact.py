# 创建你自己的命令行 地址簿 程序。在这个程序中，你可以添加、修改、删除和搜索你的联系人（朋友、家人和同事等等）以及它们的信息（诸如电子邮件地址和/或电话号码）。这些详细信息应该被保存下来以便以后提取。
#
# 思考一下我们到目前为止所学的各种东西的话，你会觉得这个问题其实相当简单。如果你仍然希望知道该从何处入手的话，那么这里也有一个提示。
#
# 提示（其实你不应该阅读这个提示） 创建一个类来表示一个人的信息。使用字典储存每个人的对象，把他们的名字作为键。使用cPickle模块永久地把这些对象储存在你的硬盘上。使用字典内建的方法添加、删除和修改人员信息。

import os
import sys
import pickle as p

filename = 'contactbook.data'

class Contact:
    def __init__(self,name,tel):
        self.name = name
        self.tel = tel

def showall():
    f = open(filename,'rb')
    conlist = p.load(f)
    f.close()
    for name,tel in conlist.items():
        print(name + '\t' + tel)
    del conlist

def add():
    s = input('Please input similar to jack,13543454567 >>\n')
    s1 = s.split(',')
    temp = Contact(s1[0],s1[1])
    f = open(filename,"rb")
    conlist = p.load(f)
    f.close()
    conlist[temp.name] = temp.tel
    f = open(filename,'wb')
    p.dump(conlist,f)
    f.close()
    del conlist

def select():
    f = open(filename,'rb')
    conlist = p.load(f)
    f.close()
    showall()
    s = input('Please enter the name which you want to select>>\n')
    if s in conlist:
        print (s, ':', conlist[s])
    else:
        print("No Data!")
    del conlist

def delete():
    f = open(filename,'rb')
    conlist = p.load(f)
    f.close()
    showall()
    d = input("Please enter the name which you want to delete>>\n")
    if d in conlist:
        del conlist[d]
    else:
        print("No Data!")
    showall()
    f = open(filename,'wb')
    p.dump(conlist,f)
    f.close()
    del conlist

def main():
    while True:
        selection = input('1.查询 2.添加/修改 3.删除 4.显示所有 5.退出>>\n')
        if selection == '1':
            select()
        elif selection == '2':
            add()
        elif selection == '3':
            delete()
        elif selection == '4':
            showall()
        elif selection == '5':
            sys.exit()
        else:
            print("Don't have this option,please try again!\n")
if os.path.exists('contactbook.data'):
      main()
else:
      f=open('contactbook.data','wb')
      conlist={'zsn':'15912345678'}
      p.dump(conlist,f)
      f.close()
      del conlist
      main()