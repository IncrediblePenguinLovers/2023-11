class IPL_Neuron_model :

  def __init__ (self) : # 꼭 이렇게 표현해줘야 하는가 싶긴 해 self.w, self.b

    self.w = 1
    self.b = 1

  def forpass (self, x) :

    a = self.w * x + self.b
    return a

  def backprop (self, x, y) :

    err = y - a
    w_grad = x * err
    b_grad = 1 * err
    return w_grad, b_grad

  def fit (self, x, y, epochs = 100) :

    for i in range(epochs) :

      for j in i :

        for x_i, y_i in zip(x, y) :

          a = forpass(x_i)
          w_grad, b_grad = backprop(x_i, y_i)
          w -= w_grad
          b -= b_grad
                            

    
    

    

  
    
  
  
