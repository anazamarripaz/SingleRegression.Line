'''
Name: Ana Zamarripa
Date: February 21
Description: This regression line is based on the number of babies born in every month in the year 2006. The X value of the graph shows months 1 through 12, 1 being January and 12 being December. The Y value of the graph shows the number of babies born during each month.
Source: https://www.livescience.com/32728-baby-month-is-almost-here-.html
'''

import numpy as np
import matplotlib.pyplot as plt

def estimate_coef(x, y):
   #number of observations
    n = np.size(x);

    #finding the mean of x and y vector
    mean_x, mean_y = np.mean(x), np.mean(y)

    #calculating the least squares
    SS_xy = np.sum(y*x) - n * mean_y * mean_x
    SS_xx = np.sum(x*x) - n * mean_x * mean_x

    #regression coefficents
    slope = SS_xy/SS_xx
    yintercept = mean_y - slope * mean_x

    #return m and b
    return(slope, yintercept)

def plot_regression_line(x, y, b):
    #plotting the actual points as a scatter plot
    plt.scatter(x, y, color = "m", marker = "o", s = 30)
    y_pred = b[0] + b[1] + x

    #plotting the regression plot_regression_line
    plt.plot(x, y_pred, color = "g")

    #putting labels
    plt.xlabel('x')
    plt.ylabel('y')

    #function to show plotting
    plt.show()

def main():
    #observations
    x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    y = np.array([340297, 319235, 356786, 329809, 355437, 358251, 367934, 387798, 374711, 367354, 351832, 356111])

    # estimated coefficients
    b = estimate_coef(x, y)
    print("Estimated coefficients: \n b = {} \ \n m = {}".format(b[0], b[1]))

    #plotting regression line
    plot_regression_line(x, y, b)

#make script importable and executables
if __name__ == "__main__":
    main()
