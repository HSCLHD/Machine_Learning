import matplotlib.pyplot as plt
from scipy import stats
# linear regression

# use scipy to sketch the line

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))
# It is important to know how the relationship between the values of the x-axis and the values of the y-axis is, 
# if there are no relationship the linear regression can not be used to predict anything.
#This relationship - the coefficient of correlation - is called r

# method 2
# sklearn and panda

# plt.scatter(x, y)
# plt.plot(x, mymodel)
# plt.show()
# print("r is",r)

# Cost function
# m is the number of training examples
m = len(x)

J = 0
i = 0
for i in range(m):
    J = J + ( mymodel[i] - y[i] )/(2*m)
    i += 1

# print(type(mymodel))
