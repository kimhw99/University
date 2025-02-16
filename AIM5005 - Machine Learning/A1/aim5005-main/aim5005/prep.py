import numpy as np
from typing import List, Tuple

def center(x:List[float]) -> List[float]:
    """
    Subtract the mean so that the result is centered around 0
    """
    mean_val = np.mean(x)
    return [x - mean_val for x in x]

def covariance(x: List[float], y:List[float]) -> float:
    """
    Measures how much two variables vary from their means
    """
    assert len(x) == len(y)
    
    return np.dot(center(x), center(y)) / (len(x) - 1)

def correlation(x: List[float], y:List[float]) -> float:
    """
    A measure of how much variance there is in x and y around the means. 
    The correlation will always be between -1 and 1. 
    1 is perfect correlation and 0 is no correlation at all
    """
    std_x = np.std(x)
    std_y = np.std(y)
    if std_x > 0 and std_y > 0:
        return covariance(x, y)/std_x/std_y
    else:
        return 0