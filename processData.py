import numpy as np
import math
import matplotlib.pyplot as plt


class processData():
    def __init__(self, dataInput, dataOutput):
        self.dataInput = dataInput
        self.dataOutput = dataOutput
        self.newData = []
        self.x_train = [[]]
        self.y_train = [[]]
        
       


    def cut(self, data):
        splitNum = math.floor(len(data)/(self.dataInput+self.dataOutput))
        compNum = 0
        counter = 0
        row = []
        for i in range(len(data)):
            if counter == self.dataInput+self.dataOutput:
                counter = 0
                compNum += 1
                self.newData.append(row)
                row = []
            row.append(data[i])
            counter+=1     
            
        return self.newData

    def split(self, array):
        x_train = [[]]
        y_train = [[]]
        for data in array:
            counter = 0
            row_x = []
            row_y = []
            for i in range(len(data)):
                if counter < 33:
                    row_x.append(data[i])
                else:
                    row_y.append(data[i])
                counter+=1
            x_train.append(row_x)
            y_train.append(row_y)
           
        x_train = x_train[1:]
        y_train = y_train[1:]
        return x_train, y_train

    def splitValidation(self, newData):
        trainData = []
        testData = []
        lenghtData = len(newData)
        testSize = math.floor(lenghtData/40)
        for i in range(lenghtData):
            if i<testSize:
                testData.append(newData[i])
            else:
                trainData.append(newData[i])
        return trainData, testData


