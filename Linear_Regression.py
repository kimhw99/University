# Linear Regression
import numpy as np
import pandas as pd

class linearRegreession:
    def __init__(self):
        self.weights = []
        self.rng = np.random.default_rng()
        
        self.xTrain = 0
        self.yTrain = 0
        
        self.xPredict = 0 # Predict
        self.yPredict = 0 # RMSE

    def train(self, a, n): # n == (0 / 1) ---> Predict (Next_Tmax / Next_Tmin)
        col_mean = np.nanmean(a, axis=0)
        inds = np.where(np.isnan(a))
        a[inds] = np.take(col_mean, inds[1]) #Remove NaN
        
        self.xTrain, self.yTrain = np.hsplit(a, [21])
        self.yTrain = self.yTrain[:,n]

        self.weights = np.zeros((1, (self.xTrain).shape[1]))

        while(self.lossFunction() > 50000):
            model.gradientDescentStochastic(0.00000001)

        rmse = 0

        for i in range(0, self.yTrain.shape[0]):
            rmse = ((self.regression(i) - self.yTrain[i])**2)/self.yTrain.shape[0]

        rmse = rmse**0.5
        print(" - Training Error RMSE: ", round(rmse, 10))

    def regression(self, n):
        a = self.xTrain[n]
        a = a.reshape((21, 1))
        result = np.tensordot(self.weights, a, axes=([-1],[0])) #dot product
        return result[0, 0]

    def regressionPredict(self, n):
        a = self.xPredict[n]
        a = a.reshape((21, 1))
        result = np.tensordot(self.weights, a, axes=([-1],[0]))
        return result[0, 0]

    def lossFunction(self):
        result = 0

        for i in range(0, self.yTrain.size):
            result = result + ((self.regression(i)) - self.yTrain[i])**2

        return result/2

    def gradientDescentStochastic(self, a):
        for i in range(0, 10):
            rand = self.rng.integers(low=1, high=self.yTrain.size)
            # print("*  ", rand)
            self.weights = self.weights + a * (self.yTrain[rand] - self.regression(rand)) * self.xTrain[rand]

    def predict(self, a, n): # n == (0 / 1) ---> Predict (Next_Tmax / Next_Tmin)
        col_mean = np.nanmean(a, axis=0)
        inds = np.where(np.isnan(a))
        a[inds] = np.take(col_mean, inds[1]) # Remove NaN
        
        self.xPredict, self.yPredict = np.hsplit(a, [21]) # Prediction Data
        self.yPredict = self.yPredict[:,n] # RMSE Data

        rmse = 0

        for i in range(0, self.yPredict.shape[0]):
            rmse = ((self.regressionPredict(i) - self.yPredict[i])**2) / self.yPredict.shape[0]

        rmse = rmse**0.5
        print(" - Test Error RMSE: ", round(rmse, 10))


# Get Excel DataSheet
dataPD = pd.read_csv("Regression.csv", usecols = [i for i in range(2, 25)])


for i in range(0, 10):
    print("Trial", i+1, "(Next_Tmax)")
    
    dataNP = dataPD.to_numpy()
    
    np.random.shuffle(dataNP) # Shuffle, Split Data
    dataPredict, dataTrain = np.vsplit(dataNP, [1550])

    model = linearRegreession()
    model.train(dataTrain, 0) # Train
    model.predict(dataPredict, 0) # Predict & RMSE
    
    print("")

print("----------------------------------\n")

for i in range(0, 10):
    print("Trial", i+1, "(Next_Tmin)")
    
    dataNP = dataPD.to_numpy()
    
    np.random.shuffle(dataNP) # Shuffle, Split Data
    dataPredict, dataTrain = np.vsplit(dataNP, [1550])

    model = linearRegreession()
    model.train(dataTrain, 1) # Train
    model.predict(dataPredict, 1) # Predict
    
    print("")
