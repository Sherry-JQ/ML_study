#encoding:utf-8
'''
Created by Shelly on 2016.9.10.
This is a test for Tkinter.
The help from http://blog.csdn.net/lemonwyc/article/details/38071281
'''
from Tkinter import *
# def processOk():
#     print "OK button is clicked."
#
# def processCancel():
#     print "Cancel button is clicked."
#
# #create a window
# window=Tk()
# #create two buttons
# btOk=Button(window,text="OK",fg="red",command=processOk)
# btCancel=Button(window,text="cancel",bg="yellow",command=processCancel)
# #注意这个地方，不要写成processCancel(),如果是processCancel()的话，
# #会在mainloop中调用processCancel函数，
# #而不是单击button按钮时触发事件
#
# #pack button on window
# btOk.pack()
# btCancel.pack()
#
# # 创建一个事件循环，监测事件发生，直到窗口关闭
# window.mainloop()

class WidgetsDemo:
    def __init__(self):
        window=Tk()
        window.title('Widgets Demo')

    #frame1
        frame1=Frame(window)
        frame1.pack()
        # cbtBold = Checkbutton()这一句中variable = self.v1表示与v1关联，
        # 默认情况为当该按钮选中时，v1=1，否则v1=0；rbRed = Radiobutton()
        # 这一句中也有类似的，其中value=1表示该按钮选中是v2=1，若选中rbYellow，则v2=2；
        self.v1=IntVar() #self.v1 = IntVar()表示v1是Int型变量
        cbtBold=Checkbutton(frame1,text='Bold',
                            variable=self.v1,command=self.processCheckbutton)
        self.v2=IntVar()
        rbRed=Radiobutton(frame1,text='red',bg='red',
                          variable=self.v2,value=1,command=self.processRadiobutton)
        rbYellow=Radiobutton(frame1,text='yellow',bg='yellow',
                          variable=self.v2,value=2,command=self.processRadiobutton)
        #grid
        cbtBold.grid(row=1,column=1)
        rbRed.grid(row=1,column=2)
        rbYellow.grid(row=1,column=3)

    #frame2
        frame2=Frame(window)
        frame2.pack()
        mylabel=Label(frame2,text='Enter your name:')
        self.name=StringVar()
        entryName=Entry(frame2,textvariable=self.name)
        btGetName=Button(fram2,text="Get Name",command=self.processGetname)
        message=Label(frame2,text="It is a widgets demo.")
        #grid
        mylabel.grid(row=1,column=1)
        entryName.grid(row=1,column=2)
        btGetName.grid(row=1,column=3)
        message.grid(row=2,column=1)

    #frame3
        frame3=Frame(window)
        frame3.pack()
        testImage=PhotoImage(file='E:\\picture\\007.gif')
        label=Label(frame3,image=testImage)
        label.pack()
        canvas = Canvas(frame3,width=280,height=200,bg="white")
        canvas.create_image(100,100,image=testImage)
        #canvas.pack()
        Button(frame3,image=testImage)

    #text
        text=Text(window)
        text.pack()
        text.insert(END,"Tip\nThe best way to learn Tkinter is to read")
        text.insert(END,"these carefully designed examples and use them")
        text.insert(END,"to create your applications.")
        #text.insert(END," ")是指向Text中插入格式化文本，其中END是指将文本插入到当前文本的后面；
        window.mainloop()

    def processCheckbutton(self):
        print "Checkbutton is :","Checked" if self.v1.get()==1 else "unChecked",'.'

    def processRadiobutton(self):
        print 'Red' if self.v2.get()==1 else 'Yellow','is selected.'

    def processGetname(self):
        print "Your name is: ",self.name.get()

WidgetsDemo()