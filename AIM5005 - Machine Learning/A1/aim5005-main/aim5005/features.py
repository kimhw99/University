import numpy as np
from typing import List, Tuple
### YOU MANY NOT ADD ANY MORE IMPORTS (you may add more typing imports)

class MinMaxScaler:
    def __init__(self):
        self.minimum = None
        self.maximum = None
        
    def _check_is_array(self, x:np.ndarray) -> np.ndarray:
        """
        Try to convert x to a np.ndarray if it'a not a np.ndarray and return. If it can't be cast raise an error
        """
        if not isinstance(x, np.ndarray):
            x = np.array(x)
            
        assert isinstance(x, np.ndarray), "Expected the input to be a list"
        return x
        
    
    def fit(self, x:np.ndarray) -> None:   
        x = self._check_is_array(x)
        self.minimum=x.min(axis=0)
        self.maximum=x.max(axis=0)
        
    def transform(self, x:np.ndarray) -> list:
        """
        MinMax Scale the given vector
        """
        x = self._check_is_array(x)
        diff_max_min = self.maximum - self.minimum
        
        # TODO: There is a bug here... Look carefully! 
        return (x-self.minimum)/(self.maximum-self.minimum)
    
    def fit_transform(self, x:list) -> np.ndarray:
        x = self._check_is_array(x)
        self.fit(x)
        return self.transform(x)
    
    
class StandardScaler:
    def __init__(self):
        self.mean = None
        self.std = None
        #raise NotImplementedError
        
    def _check_is_array(self, x:np.ndarray) -> np.ndarray:
        """
        Try to convert x to a np.ndarray if it'a not a np.ndarray and return. If it can't be cast raise an error
        """
        if not isinstance(x, np.ndarray):
            x = np.array(x)
            
        assert isinstance(x, np.ndarray), "Expected the input to be a list"
        return x
        
    def fit(self, x:np.ndarray) -> None:   
        x = self._check_is_array(x)
        self.mean=x.mean(axis=0)
        self.std=x.std(axis=0)
        
    def transform(self, x:np.ndarray) -> list:
        x = self._check_is_array(x)
        return (x-self.mean)/(self.std)
    
    def fit_transform(self, x:list) -> np.ndarray:
        x = self._check_is_array(x)
        self.fit(x)
        return self.transform(x)
        
class LabelEncoder:
    def __init__(self):
        self.classes_ = None
        #raise NotImplementedError
        
    def _check_is_array(self, x:np.ndarray) -> np.ndarray:
        """
        Try to convert x to a np.ndarray if it'a not a np.ndarray and return. If it can't be cast raise an error
        """
        if not isinstance(x, np.ndarray):
            x = np.array(x)
            
        assert isinstance(x, np.ndarray), "Expected the input to be a list"
        assert x.ndim==1, "y should be a 1d array, got an array of shape " + str(x.shape) + " instead"
        
        return x
    
    def classes_(self, x):
        x = self._check_is_array(x)
        self.classes_ = np.array(sorted(np.array(list(set(x)))))
        return self.classes_
        
    def fit(self, x:np.ndarray):
        x = self._check_is_array(x)
        self.classes_ = np.array(sorted(np.array(list(set(x)))))
        
    def transform(self, x:np.ndarray):
        x = self._check_is_array(x)
        assert isinstance(self.classes_ , np.ndarray), "No classes detected, fit encoder to data first"
        
        class_dict, n = dict(), 0
        x = x.astype(self.classes_.dtype)
        result = np.zeros(x.shape[0], dtype=int)
        
        for c in self.classes_:
            class_dict[c] = n
            n += 1
            
        for i in range (0, x.shape[0]):
            result[i] = class_dict[x[i]]
            
        return result
        
    def fit_transform(self, x:list):
        x = self._check_is_array(x)
        self.fit(x)
        return self.transform(x)