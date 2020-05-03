import matplotlib.pyplot as plt
from sklearn.neural_network import MLPRegressor
import numpy as np
class model():
    def __init__(self):
        self.clf = MLPRegressor(solver='adam', alpha=1e-5, hidden_layer_sizes=(4005,),warm_start=True, random_state=1)
        
    def buildModel(self, train_x, train_y): 
        self.clf.fit(train_x, train_y)

    def predict(self, x, y):
        prediction = self.clf.predict(x)
        print("input: "+str(x))
        print()
        print("output: "+str(y))
        print()
        print("prediction: "+str(prediction))
        fig, axs = plt.subplots(2)
        axs[0].plot(y[0])
        axs[1].plot(prediction[0])
        plt.show()

        print("input: "+str(x[1]))
        print()
        print("output: "+str(y[1]))
        print()
        print("prediction: "+str(prediction))
        fig, axs = plt.subplots(2)
        axs[0].plot(y[1])
        axs[1].plot(prediction[0])
        plt.show()

model = model()

f = open("trainig.txt", "r")
print(f.read()[0])

model.buildModel(trainingData_X, trainingData_Y)
model.predict(testingData_X, testingData_Y)