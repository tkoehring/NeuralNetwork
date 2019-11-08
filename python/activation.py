## Acticvation Functions
from math import exp

def linear(val):
    return val

def tanh(val):
    return (exp(2*val) - 1) / (exp(2*val) + 1)

def relu(val):
    if(val > 0):
        return val
    else:
        return 0
    
def sigmoid(val):
    return exp(val) / (exp(val) + 1)

## Derivative of Activation Functions ##

def linear_d(val):
    return 1

def tanh_d(val):
    1 - tanh(val)**2
    
def relu_d(val):
    if(val < 0):
        return 0
    else:
        return 1

def sigmoid_d(val):
    return sigmoid(val)*(1 - sigmoid(val))

