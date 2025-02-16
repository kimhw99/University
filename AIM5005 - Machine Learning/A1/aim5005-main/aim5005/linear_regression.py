import numpy as np
from typing import List, Tuple
from aim5005.prep import correlation

class LinearRegresion:
    def __init__(self):
        self.intercept = None
        self.beta = None
    
    def predict(self, x:List[float]) -> float:
        """ Given values, x, predict the y value
        """
        return self.intercept + self.beta * np.array(x)
    
    def fit(self, x: List[float], y:List[float]) -> None:
        self.intercept, self.beta = self.least_squares_fit(x, y)
    
    def least_squares_fit(self, x: List[float], y:List[float]) -> Tuple[float, float]:
        x, y = np.array(x), np.array(y)
        beta = correlation(x,y) * np.std(y)/ np.std(x)  
        intercept = np.mean(y) - beta * np.mean(x)
        return (intercept, beta)