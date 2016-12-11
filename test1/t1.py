#encoding=utf-8
## import numpy as np
#
# #Numbers
# x=3
# y=2.5
# print type(x),type(y)
# print x**x,y*y,x*2,y+1
# x+=1
# y*=2
# print "x+=1:",x
# print "y*=2:",y
#
# #Booleans
# t=True
# f=False
# print type(t),type(f)
# print t and f,t or f,not t,t != f           # "！=" means XOR
#
# #String
# hello="hello"
# world='world'
# print hello,world
# print hello+' '+world+'!'
# hw2016='%s %s %d'%(hello,world,2016)
# print hw2016
# s='shelly'
# print s.capitalize(),s.upper(),s.center(10)
# print s.center(8,'b'),s.rjust(8,"a")
# print s.replace('ll','(ll)')
#
# #List
# xs=[3,1,2]
# print xs[0],xs[1],xs[2],xs[-1],xs[-2],xs[-3]          #[-1]means the last one
# xs[2]='zz'        #change
# print xs,xs[-1]
# xs.append("sb")   #add
# print xs,xs[-1]
# xs.pop()          #xs.pop()默认为xs.pop(-1)，即去掉最后一个
# print xs
#
# #List_slicing
# nums=range(5)    #def range(start=None, stop=None, step=None)
# print nums
# print nums[:],nums[:-2],nums[2:],nums[1:3]
# nums[2:4]=[22,33]
# print nums
#
# #List_loops
# mylist=['apple','banana','cat']
# for item in mylist:          #item随意命名
#     print item
# for idx,item2 in enumerate(mylist):   #enumerate可取下标
#     print '#%d: %s'%(idx+1,item2)
#
# #List_comprehension
#    #for
# mylist2=['dog','pig','mouse','lion']
# klist=[]
# for x in mylist2:
#     klist.append(x)
# print klist
#    #comprehension
# mylist3=range(5)
# squares3=[x**2 for x in mylist3]
# squares4=[x**2 for x in mylist3 if x%2==0]
# print squares3,squares4
#
# #Dict--for(key,value)
# d={'one':1,'two':"double",'three':"三"}
# print d['two'],d.get('four','error!')
# d['pig']='p'        #add
# print d.get('pig')
# del d["pig"]        #del
# print d.get('pig')
#
# #Dict_loops
#    #for
# d={'person':2,'dog':4,"spider":8}
# print d
# print d.items()
# for a,b in d.items():
#     print 'constract %s to %d'%(a,b)
# for item in d:
#     print "A %s has %d legs" %(item,d[item])
#
#    #comprehension
# nums=range(5)
# outdict={"%d 's square is" %(x):x**2 for x in nums if x%2==0}
# print outdict
#
# #turple
# d={(x,x+1): x  for x in range(10)}
# t=(5,6)
# print d,type(t),d[t],d[(1,2)],d[(0,1)]
# aturple=('a','c','e')
# bturple=('g','i',aturple)
# print bturple,bturple[2],bturple[2][0]

# #def
# def hello(name,flag=False):
#     if flag:
#         print "Hello,%s"%(name.capitalize())
#     else:
#         print "HELLO,%s"%(name.upper())
# hello('shelly')
# hello('zera',flag=True)
#
# #class
# class Greeter:
#     def __init__(self,n):
#         self.name=n
#     def greet(self,flag=False):
#         if flag:
#             print 'Hello,%s'%(self.name.capitalize())
#         else:
#             print 'HELLO,%s'%(self.name.upper())
# g=Greeter('Debbie')
# g.greet()
# g.greet(flag=True)
#
# #class_inherit
# class person:
#     name=" "
#     age=0
#     __weight=0 #私有变量
#     def __init__(self,n,a,w):
#         self.name=n
#         self.age=a
#         self.__weight=w
#     def speak(self):
#         print '%s is speaking:I am %d years old'%(self.name,self.age)
#
# p=person('Tom',20,100)
# p.speak()
#
# class student(person):
#     grade=1
#     def __init__(self,n,a,w,g):
#         person.__init__(self,n,a,w)
#         self.grade=g
#     def speak2(self):
#         print '%s is speaking:I am %d years old,and I am in grade %d'%(self.name,self.age,self.grade)
# s=student('Tommy',18,90,2)
# s.speak2()
#
# class outimage:
#     sex=" " #"female or male"
#     height=160
#     def __init__(self,s,h):
#         self.sex=s
#         self.height=h
#
# class simple(student,outimage):
#     def __init__(self,n,a,w,g,s,h):
#         student.__init__(self,n,a,w,g)   #调用父类的构函
#         outimage.__init__(self,s,h)
#     def speak(self):                     #覆写父类的方法
#         print '%s is %d cm height'%(self.name,self.height)
# si=simple('Tomas',22,130,3,'male',180)
# si.speak()
#
# #numpy
# import numpy as np
# a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# b=a[:2,-2:]
# print a,a.shape,a.dtype
# print b,b.shape
# print a[0,3]
# b[0,1]=44
# print a[0,3]
# print a[[0,1,2],[0,1,2]]
# print np.array([a[0,0],a[1,1],a[2,2]])
# bool_idx=a>2
# print bool_idx
# print np.reshape( a[a>2],(2,5))
# print np.tile( a[a>2],(4,2))
##

# #encoding:utf-8
# def guess_number_while(number):
#     running=True
#     while running:
#         guess=int(raw_input("Please input a number: (0--20)"))
#         if guess==number:
#             print "You are right!"
#             running=False
#         elif guess<0:
#             print "error"
#         elif guess>20:
#             print "error"
#         else:#else可要可不要
#             if guess<number:
#                 print "Sorry,it is a little lower than that"
#             elif guess>number:
#                 print "Sorry,it is a little higher than that"
#     else:#running is False时执行
#         print "Game over."
# #guess_number_while(11)
# def guess_number_for(number):
#     running=True
#     if running:
#         guess=int(raw_input("Please input a number: (0--20)"))
#         if guess>=0 and guess<=20:
#             if guess==number:
#                 print "You are right!"
#                 running=False#不会第二次执行到if running，因此这句没用
#             elif guess<number:
#                 print "Sorry,it is a little lower than that.Game over."
#             elif guess>number:
#                 print "Sorry,it is a little higher than that.Game over."
#         else:
#             print "Error!Game over."
#     else:
#         print "Congratulations!Game over."#并不会执行到这句，因为根if仅执行一次（running=True）
#     print "Bye~"
# #guess_number_for(9)
#
# def maxinum(x,y):
#     if x>y:
#         print 'The max is',x
#     else:
#         print 'The max is',y
# #maxinum(2,3)
# def maxinum_return(x,y):
#     '''
#     This is a define.
#
#     To make the max.
#     End
#     '''
#     if x>y:
#         return x
#     else:
#         return y
# print 'The max is',maxinum_return(3,4)
# print maxinum_return.__doc__

# #module
# import sys
# print 'The command line arguments are:'
# for i in sys.argv:
#     print i
# print '\n\nThe PythonPath is',sys.path,'\n'

# import mymodule
# mymodule.sayhi()
# print 'Version:',mymodule.version

# from mymodule import sayhi,version
# sayhi()
# print 'Version:',version

# class Person:
#     def sayhi(self,name):
#         print "hi,%s"%name
# p=Person()
# p.sayhi('zera')

# mylove='''
# You are my sunshine,
# and I want to be your sunshine.
# '''
# f=file("love.txt","w")
# f.write(mylove)
# f.close()
# f=file('love.txt','r')
# while True:
#     myline=f.readline()
#     if len(myline)==0:
#         break
#     print myline,
# f.close()
#
import cPickle as p
shoplistfile='shoplist.data'
shoplist=['I','love','you']
f=file(shoplistfile,'w')
p.dump(shoplist,f)
f.close()
del shoplist
f=file(shoplistfile)#only read
storedlist=p.load(f)
print storedlist
# import sys
# try:
#     s=raw_input('Enter something -->')
# except EOFError:
#     print '\nWhy did you do an EOF on me?'
#     sys.exit()
# except:
#     print '\nSome error/exception occurred.'
# print 'Done'

