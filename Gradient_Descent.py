
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

x = np.linspace(0,1,300)
y = 0.7*x
noise_y = np.random.normal(0, 0.1, y.shape)
y = y+noise_y


Wts = np.linspace(-5,5, 100)

m = len(x)

error_list = []
for W in Wts:
    y_out = W * x
    error_val = ((y_out - y)**2).sum()/(2*m)
    error_list.append(error_val)



W = 4
Wold = None
Eold = None
alpha = 1
pause_time = 1

plt.ion()
plt.show()
for i in range(1000):
	y_out = W * x
	error_val = ((y_out - y)**2).sum()/(2*len(y))

	plt.gcf().clear()
	plt.plot(Wts,error_list)
	plt.scatter(W, error_val)
	plt.pause(pause_time)

	m = len(x)
	error = y_out - y
	dW = (x*error).sum()/ m

	## This is for plotting slope and change
	Wold = W
	Eold = error_val
	# y = mx+c
	# c = y - mx
	c_plot = error_val - dW * W
	x_plot = np.linspace(W-1, W+1, 50)
	y_plot = dW*x_plot + c_plot
	# plt.scatter(Wold, Eold)
	# plt.plot(x_plot, y_plot)
	#### this plot is upto here

	W = W - alpha* dW
	y_out = W * x
	error_val = ((y_out - y)**2).sum()/(2*len(y))
	print('dW = ', dW)
	print('Cost = ', error_val)
	
	plt.gcf().clear()
	plt.plot(Wts,error_list)
	plt.scatter(W, error_val)
	plt.scatter(Wold, Eold)
	plt.plot(x_plot, y_plot)
	plt.pause(pause_time)



