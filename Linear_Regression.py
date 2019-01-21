
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time


# Points from 0 to 1 
x = np.linspace(0,1,300)
# Y = m*X + c
# let m=0.7, c= 2
y = 0.7*x + 2
# plot x and y

# plt.scatter(x,y)

noise_x = np.random.normal(-0.05, 0.05, x.shape)
x = x+noise_x

noise_y = np.random.normal(-0.05, 0.05, y.shape)
y = y+noise_y

# plt.scatter(x,y)

W = 50. # equal to slope
b = 0. #equal to y-intercept

learning_rate = 0.3


plt.ion()
plt.show()


for i in range(1000):
    y_out = W*x + b

    plt.gcf().clear()
    plt.scatter(x,y_out)
    plt.scatter(x, y)
    
    
    error_val = ((y_out - y)**2).sum()/(2*len(y))

    error = y_out - y
    m = len(x)
    dW = (x*error).sum()/ m
    db = error.sum()/ m
    
    W = W - learning_rate* dW
    b = b - learning_rate* db
    
    print('error=',error_val)
    print('W = {}  b = {}'.format(W,b))
    
    # plt.show()
    plt.pause(0.1)
    

print('W = ',W)
print('b = ',b)

