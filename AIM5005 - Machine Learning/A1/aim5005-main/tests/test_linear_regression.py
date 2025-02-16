from aim5005.linear_regression import LinearRegresion
import pytest
import random
random.seed(10)

def test_initialize_linear_regression():
    lr = LinearRegresion()
    assert isinstance(lr, LinearRegresion), "lr is not a LinearRegression object"
    
def test_lr_fits():
    x = [i for i in range(-100, 110, 10)]
    y = [0.1*i+5 for i in x]
    lr = LinearRegresion()
    lr.fit(x, y)
    
    assert round(lr.beta, 3) == 0.105, "beta is not 0.105"
    assert round(lr.intercept, 1) == 5.0, "coef is not 5.0"
    
def test_lr_predicts():
    x = [i for i in range(-100, 110, 10)]
    y_noise = [0.1*i+5 + random.uniform(-5,5) for i in x]
    lr = LinearRegresion()
    lr.fit(x, y_noise)
    
    assert (round(lr.beta, 3) > 0.08) and (round(lr.beta) < 0.110), "beta is outside range (.08, .110)"
    assert (lr.intercept > 3.0) and (lr.intercept < 7.0), "intercept is outside acceptable range (3,7)"
    
def test_lr_predict():
    x = [i for i in range(-100, 110, 10)]
    y_noise = [0.1*i+5 + random.uniform(-5,5) for i in x]
    lr = LinearRegresion()
    lr.fit(x, y_noise)
    y_hat = lr.predict(x)
    
    assert round(y_hat[6], 2) == 1.04, f"Got {y_hat[6]} expected 1.11"
    assert round(y_hat[7], 2) == 1.97, f"Got {y_hat[7]} expected 1.97"