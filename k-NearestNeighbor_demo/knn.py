#encoding:utf-8
'''
Create by Sherry on 2016.12.9.
This is a demo for KNN.
The help from https://github.com/wepe/MachineLearning
'''
from numpy import *
import operator
def createData():
    trainData=array([[1.0,1.0],[1.1,1.1],[0,0],[0.1,0],[0.9,0.9]])
    labelData=['A','A','B','B','A']
    return trainData,labelData

def classfy(inX,dataSet,labels,k):
    dataSetSize=dataSet.shape[0] #shape[0]得出dataSet的行数，即样本个数
    diffSet=tile(inX,(dataSetSize,1))-dataSet #差: tile(A,(m,n))将数组A作为元素构造m行n列的数组
    aqDiffMat=diffSet**2 #array形如[[0,0],[0.01,0.01],[1,1],[0.01,0]]
    sqDistances=aqDiffMat.sum(axis=1)  #array.sum(axis=1)按行累加，axis=0为按列累加
    distances=sqDistances**0.5#array形如[[0],[0.013],[1.41],[0.1]]
    sortedDistIndex=distances.argsort()

    classcount={}
    for i in range(k):
        votelLabel=labels[sortedDistIndex[i]]
        classcount[votelLabel]=classcount.get(votelLabel,0)+1 #get(key,x)从字典中获取key对应的value，没有key的话返回0
        #此处get(votelLabel,0)第一次循环，classcount[A]没有key返回0，classcount[A]=1
        #此后再次遇到votelLabel=A时，会将value+=1...
    sortedClasscount=sorted(classcount.iteritems(),key=operator.itemgetter(1),reverse=True)
    # 对字典进行排序
    # >>> d = {'data1':3, 'data2':1, 'data3':2, 'data4':4}
    # >>> sorted(d.iteritems(), key=itemgetter(1), reverse=True)
    # [('data4', 4), ('data1', 3), ('data3', 2), ('data2', 1)]
    #sorted()函数，按照第二个元素即value的次序逆向（reverse=True）排序
    return sortedClasscount[0][0]

train,label=createData()
result=classfy([0,0],train,label,4)#k取奇数错误率会下降，此例中k=4会分类结果会出错
print result


import matplotlib.pyplot as plt
fig=plt.figure()
ax=fig.add_subplot(111)
trainMat=mat(train)
ax.scatter(trainMat[:,0],trainMat[:,1])
plt.show()
