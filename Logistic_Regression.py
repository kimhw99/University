# Logistic Regression
# Uses openpyxl for opening excel file
import numpy as np
import pandas as pd


# Logistic Function
class logisticRegression:
    def __init__(self):
        self.weights = []
        self.rng = np.random.default_rng(3020)
        
        self.xTrain = 0
        self.yTrain = 0
        
        self.xPredict = 0
        

    def train(self, a, m):
        self.xTrain, self.yTrain = np.hsplit(a, [4])
        self.weights = np.zeros((1, (self.xTrain).shape[1]))

        for i in range(1, 100):
            self.gradientAscent(0.5, m)

        for i in range(1, 300):
            self.gradientAscent(0.1, m)

        for i in range(1, 900):
            self.gradientAscent(0.05, m)

        for i in range(1, 2700):
            self.gradientAscent(0.01, m)


    def regression(self, n, m): # m == Iris-setosa | Iris-versicolor | Iris-virginica 
        hx = 1/(1+np.exp(-1 * np.tensordot(self.weights, self.xTrain[n], axes=([-1],[0]))[0])) #h(x)
        y = int(self.yTrain[n, 0] == m) # y == 1 | 0
        return (hx**y) * ((1-hx)**(1-y))
    

    def predict(self, a, m):
        self.xPredict = a
        result = []
        
        for i in range(0, a.shape[0]):
            result.append(self.regressionPredict(i, m))

        return result


    def regressionPredict(self, n, m):
        hx = 1/(1+np.exp(-1 * np.tensordot(self.weights, self.xPredict[n], axes=([-1],[0]))[0])) #h(x)
        return hx


    def logLikelihood(self, m):
        result = 1

        for i in range(0, self.yTrain.size):
            result = result * self.regression(i, m)

        #print(round(result,32))

        return np.log(result)


    def gradientAscent(self, a, m):
        rand = self.rng.integers(low=1, high=self.yTrain.size)
        y = int(self.yTrain[rand, 0] == m) # y == 1 | 0
        hx = 1/(1+np.exp(-1 * np.tensordot(self.weights, self.xTrain[rand], axes=([-1],[0]))[0]))
        
        self.weights = self.weights + a * (y - hx) * self.xTrain[rand]


# Name for Predicted Value
def predictName(a):
    if max(a[0], a[1], a[2]) == a[0]:
        return "Iris-setosa"
    
    elif max(a[0], a[1], a[2]) == a[1]:
        return "Iris-versicolor"
    
    elif max(a[0], a[1], a[2]) == a[2]:
        return "Iris-virginica"


# Get Excel DataSheet
dataPD = pd.read_excel("Classification iris.xlsx")
dataNP = dataPD.to_numpy()

# Trials
for j in range(0, 10):
    np.random.shuffle(dataNP) # Shuffle, Split Data
    dataPredict, dataTrain = np.vsplit(dataNP, [int(dataNP.shape[0]/5)])
    dataPredictX, dataPredictY = np.hsplit(dataPredict, [4])
    
    modelSentosa = logisticRegression()
    modelSentosa.train(dataTrain, "Iris-setosa")

    modelVersicolor = logisticRegression()
    modelVersicolor.train(dataTrain, "Iris-versicolor")

    modelVirginica = logisticRegression()
    modelVirginica.train(dataTrain, "Iris-virginica")

    print("Iteration ", j+1)
    print(f"{'Sento':<10}"f"{'Versi':<10}"f"{'Virgi':<10}"f"{'Prediction':<20}","Guess")
    a= modelSentosa.predict(dataPredictX, "Iris-setosa")
    b= modelVersicolor.predict(dataPredictX, "Iris-versicolor")
    c= modelVirginica.predict(dataPredictX, "Iris-virginica")
    x= 0 # number of accurate predictions

    for i in range(0, len(a)):
        print(f"{str(round(a[i]*100,2))+'%':<10}" f"{str(round(b[i]*100,2))+'%':<10}" f"{str(round(c[i]*100,2))+'%':<10}" f"{predictName([a[i], b[i], c[i]]):<20}", predictName([a[i], b[i], c[i]]) == dataPredictY[i,0], "-", dataPredictY[i,0])
        if(predictName([a[i], b[i], c[i]])==(dataPredict[i])[4]):
            x=x+1

    print("*Accuracy: ", (x/len(a))*100, "%\n")
