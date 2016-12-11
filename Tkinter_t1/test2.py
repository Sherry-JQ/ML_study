#encoding:utf-8
'''
Create by shelly on 2016.9.10.
This is a GUI_demo for Tkinter.
'''
from Tkinter import *
import Tkinter as tk
from PIL import Image, ImageTk  # pillow 模块
root=tk.Tk() # 这句必须先于 ImageTk.PhotoImage 执行。
class mywindow:
    def __init__(self):
        root.title('Code Demo')

    #frame1-direction
        frame1=Frame(root)
        frame1.pack()
        label1=Label(frame1,text="Image Direction:")
        self.pathname=StringVar()
        entryGetPath=Entry(frame1,textvariable=self.pathname)
        btOk=Button(frame1,text="next",command=self.progressLoadpath)#!!!!
        #grid
        label1.grid(row=1,column=1)
        entryGetPath.grid(row=1,column=2)
        btOk.grid(row=1,column=3)

    #frame2-showImage (此步骤后续可加各种处理后的图片效果0.0)
        frame2=Frame(root)
        frame2.pack()
        #im=Image.open(r'E:\\picture\\007.gif')
        im=Image.open(r'E:\\picture\\007.gif')
        testImage=ImageTk.PhotoImage(im)
        label2_image=Label(frame2,image=testImage)
        #self.response1=label2_image.pack()
        #label2_image.pack()#后续加入其它图片后此处可改为用grid

    #frame3-change name and save
        frame3=Frame(root)
        frame3.pack()
        label3_showResult=Label(frame3,text='The result is:')
        self.imageName=StringVar()
        entryGetResult=Entry(frame3,textvariable=self.imageName)
        #grid
        label3_showResult.grid(row=1,column=1)
        entryGetResult.grid(row=1,column=2)

        root.mainloop()

    def progressLoadpath(self):
        label2_image.pack()

    def processSaveNameChange(self):
        return


mywindow()