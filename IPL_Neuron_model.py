class IPL_Neuron_model :

  def __init__ (self) : # i think i don't understand w and b represent self.w and self.b
                        # 꼭 이렇게 표현해줘야 하는가 싶긴 해 self.w, self.b

    self.w = 1
    self.b = 1

  def forpass (self, x) :

    y_hat = self.w * x + self.b
    return y_hat

  def backprop (self, x, err) :
    
    w_grad = x * err
    b_grad = 1 * err
    return w_grad, b_grad

  def fit (self, x, y, epochs = 100) :

    for i in range(epochs) :

      for j in i :

        for x_i, y_i in zip(x, y) :

          y_hat = forpass(x_i)
          err = y_i - y_hat
          w_grad, b_grad = backprop(x_i, err)
          self.w -= w_grad
          self.b -= b_grad
                            

    
    

    

  
    
  
  
