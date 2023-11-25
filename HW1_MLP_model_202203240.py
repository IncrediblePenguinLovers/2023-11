from torch.nn as nn

  # torch.nn.module(*args,**kwargs)
  # Base class for all neural network modules.

class SingleLayer(nn.module):

  def __init__(self, learning_rate = 0.1, l1 = 0.01, l2 = 0.01) :

    self.w = None
    self.b = None
    self.learning_rate = learning_rate
    self.l1 = l1
    self.l2 = l2

  def forpass(self, x):



  def backprop(self, x, err):

  def fit(self, x, epochs = 100, x_val, y_val):

    

  
    
  
  
