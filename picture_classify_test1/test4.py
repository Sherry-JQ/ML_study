#encoding=utf-8
# help from #http://python.jobbole.com/81721/
import numpy as np
import urllib
url="http://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"
raw_data=urllib.urlopen(url)
dataset=np.loadtxt(raw_data,delimiter=',')
x=dataset[:,0:7]
y=dataset[:,8]

from sklearn import preprocessing
normalized_x=preprocessing.normalize(x)
standardlized_x=preprocessing.scale(x)

from sklearn import metrics
from sklearn.ensemble import ExtraTreesClassifier
model=ExtraTreesClassifier()
model.fit(x,y)
print (model.feature_importances_)

from sklearn import metrics
from sklearn.svm import SVC
model2=SVC
model2.fit(x,y)
print (model2)
expected=y
predicted=model.predict(x)
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))