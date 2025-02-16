from aim5005.features import LabelEncoder
import numpy as np
import unittest
from unittest.case import TestCase

### DO NOT MODIFY EXISTING TESTS

class TestFeatures(TestCase):
    def test_initialize_encoder(self):
        encoder = LabelEncoder()
        assert isinstance(encoder, LabelEncoder), "encoder is not a LabelEncoder object"
        
    def test_encoder_classes_(self):
        encoder = LabelEncoder()
        data = [1, 2, 2, 6]
        expected = np.array([1, 2, 6])
        encoder.fit(data)
        assert (encoder.classes_ == expected).all(), "Classes do not meet expected values. Expected [1, 2, 6], Got: {} ".format(encoder.classes_)
        
    def test_encoder_encoding(self):
        encoder = LabelEncoder()
        data = [1, 2, 2, 6]
        expected = np.array([0, 0, 1, 2])
        encoder.fit(data)
        result = encoder.transform([1, 1, 2, 6])
        assert (result == expected).all(), "Classes do not meet expected values. Expected [0, 0, 1, 2], Got: {} ".format(result)
        
    def test_encoder_encoding_string(self):
        encoder = LabelEncoder()
        data = ['New York', 'London', 'Paris', 'Tokyo']
        expected = np.array([3,0,1,2])
        encoder.fit(data)
        result = encoder.transform(['Tokyo', 'London', 'New York', 'Paris'])
        assert (result == expected).all(), "Classes do not meet expected values. Expected [3, 0, 1, 2], Got: {} ".format(result)
        
    def test_encoder_encoding_multi(self):
        encoder = LabelEncoder()
        data = ['New York', 'London', 'Paris', 'Tokyo', 1, 1, 1, 2, 100]
        expected = np.array([2, 0, 0, 0, 2, 4, 6, 1])
        encoder.fit(data)
        result = encoder.transform([2, 1, 1, 1, 2, 'New York', 'Tokyo', 100])
        assert (result == expected).all(), "Classes do not meet expected values. Expected [2, 0, 0, 0, 2, 4, 6, 1], Got: {} ".format(result)
        
    def test_encoder_encoding_float(self):
        encoder = LabelEncoder()
        data = [3.14, 1.618, 1.414, 2.718]
        expected = np.array([0, 1, 2, 3])
        encoder.fit(data)
        result = encoder.transform([1.414, 1.618, 2.718, 3.14])
        assert (result == expected).all(), "Classes do not meet expected values. Expected [0, 1, 2, 3], Got: {} ".format(result)
        
    def test_encoder_fit_transform(self):
        encoder = LabelEncoder()
        data = [1.414, 1.618, 2.718, 3.14]
        expected = np.array([0, 1, 2, 3])
        result = encoder.fit_transform(data)
        assert (result == expected).all(), "Classes do not meet expected values. Expected [0, 1, 2, 3], Got: {} ".format(result)
    
if __name__ == '__main__':
    unittest.main()