from features import MinMaxScaler, StandardScaler, LabelEncoder
from sklearn.preprocessing import LabelEncoder
import numpy as np

encoder = LabelEncoder()
le = LabelEncoder()

encoder.fit([1,2,3,4,5])
result = encoder.transform([1,2,3,4])
print(result)

encoder.fit([1,2,3,4,5,'NYC','SGP'])
result = encoder.transform([1,2,3,4,'SGP'])
print(result)

encoder.fit([1,2,3,4,5,'NYC','SGP'])
result = encoder.transform([1,2,3,4])
print(result)


try:
    encoder.fit([1,2,3,4,5])
    result = encoder.transform([1,2,3,4,'NYC'])
    print(result)
   
except ValueError:
    print('- ValueError')
    
encoder.fit([1,2,3,4,5])
result = encoder.transform([1.1, 2.2, 3.3, 4.4])
print(result)

try:
    encoder.fit([1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5])
    result = encoder.transform([1,3,1,1,5])
    print(result)
   
except ValueError:
    print('- ValueError')
    
try:
    encoder.fit([1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5])
    result = encoder.transform([1,3,1,1,5,6])
    print(result)
   
except ValueError:
    print('- ValueError')
    
except KeyError:
    print('- KeyError')
    
result = encoder.fit_transform([1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5])
print(result)

vec = [1, 3, 4, 6, 'paris', 'nyc', 'london']
result = encoder.fit_transform(vec)
result_true = le.fit_transform(vec)
print('-', result, result_true, np.all(result==result_true))

vec = [1, 2.2, 3.4556, 1, 3, 9]
result = encoder.fit_transform(vec)
result_true = le.fit_transform(vec)
print('-', result, result_true, np.all(result==result_true))

vec = ['paris', 'london', 'new york', 'tokyo']
result = encoder.fit_transform(vec)
result_true = le.fit_transform(vec)
print('-', result, result_true, np.all(result==result_true))

vec = ['New York', 'London', 'Paris', 'Tokyo']
encoder.fit(vec)
le.fit(vec)
result = encoder.transform(['Tokyo', 'London', 'New York', 'Paris'])
result_true = le.transform(['Tokyo', 'London', 'New York', 'Paris'])
print('-', result, result_true, np.all(result==result_true))

vec = [1, 2, 2, 6]
encoder.fit(vec)
le.fit(vec)
result = encoder.transform([1, 1, 2, 6])
result_true = le.transform([1, 1, 2, 6])
print('-', result, result_true, np.all(result==result_true))

vec = ['New York', 'London', 'Paris', 'Tokyo', 1, 1, 1, 2, 100]
encoder.fit(vec)
le.fit(vec)
result = encoder.transform([2, 1, 1, 1, 2, 'New York', 'Tokyo', 100])
result_true = le.transform([2, 1, 1, 1, 2, 'New York', 'Tokyo', 100])
print('-', result, result_true, np.all(result==result_true))