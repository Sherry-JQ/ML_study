#encoding=utf-8
'''
Created by Sherry for simple Neural Network tests
on 2016.10.22.
'''
import numpy as np
from sklearn import preprocessing
class NeuralNetwork():
    def __init__(self):
        np.random.seed(1)

        #--it is a single neuron,
        #we have 3 input and 1 output,so the original weights are made to
        #a 3*1 matrix,with values in the range -1 to 1 and mean 0
        self.weights=2*np.random.random((3,1))-1

    def __sigmoid(self,x):
        return 1/(1+np.exp(-x))

    def __sigmoid_derivative(self,x):
        return x*(1-x)

    def train(self,trainSetInput,trainSetOutput,numTrain):
        for item in range(numTrain):
            output=self.think(trainSetInput)
            error=trainSetOutput-output
            adjustment=np.dot(trainSetInput.T,error*self.__sigmoid_derivative(output))
            self.weights+=adjustment
            self.weights=preprocessing.normalize(self.weights)

    def think(self,inputs):
        return self.__sigmoid(np.dot(inputs,self.weights))


if __name__=='__main__':
    #instantiation
    nn=NeuralNetwork()
    print 'Random starting weights:'
    print nn.weights

    inputset=np.array([[1,1,1],[1,0,0],[0,1,0],[0,0,0]])
    outputset=np.array([[1,1,0,0]]).T

    nn.train(inputset,outputset,1000)

    print 'Random weights after training:'
    print nn.weights

    print "Considering new situation[1,1,0]?"
    print nn.think(np.array([[1,1,0]]))


