import numpy as np
np.seterr(divide = 'ignore') 
import matplotlib
import matplotlib.pyplot as plt
SMALL_SIZE = 12
matplotlib.rc('font', size=SMALL_SIZE)
matplotlib.rc('axes', titlesize=SMALL_SIZE)

def plot_bce():
    figure, axis = plt.subplots(ncols=2,nrows=1,figsize=(14,5))
    y = np.linspace(0,1,10000)
    ### plot loss when label is y=1 ###
    log_y_1 = -np.log(y)


    axis[0].plot(y,log_y_1,label="loss")
    axis[0].set_title("Correct Label y = 1")
    axis[0].set_xlabel("$\hat{y}$")
    axis[0].set_ylabel("$-log(\hat{y})$")
    axis[0].grid("on")
    axis[0].axvline(x=0,ymin=0,ymax=1,  color='red', linestyle='--', label="Missed labeled")
    axis[0].axvline(x=1,ymin=0,ymax=1,  color='green', linestyle='--', label="Correctly labeled")
    axis[0].legend(loc='upper right')
    ### plot loss when label is y=0###
    log_y_0 = -np.log(1-y)

    axis[1].plot(y,log_y_0,label="loss")
    axis[1].set_title("Correct Label y = 0")
    axis[1].set_xlabel("$\hat{y}$")
    axis[1].set_ylabel("$-log(\hat{y})$")
    axis[1].grid("on")
    axis[1].axvline(x=1,ymin=0,ymax=1,  color='red', linestyle='--', label="Missed labeled")
    axis[1].axvline(x=0,ymin=0,ymax=1,  color='green', linestyle='--', label="Correctly labeled")
    axis[1].legend(loc='upper left')

    plt.show()
