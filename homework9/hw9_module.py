import numpy as np
import matplotlib.pyplot as plt

# 1st function, horizontal side-by-side
def right_and_left_subplots():
    x = np.linspace(0, 4*np.pi, 10) #domain defined 
    
    #defining functions 
    h_x = np.cos(x)
    k_x = np.sin(x)

    fig, (ax1, ax2) = plt.subplots(1,2, figsize= (10,8)) #creating the figure with two subplots 

    #left subplot
    ax1.plot(x, h_x, label = "h(x) = cos(x)", color = "blue", linestyle = '-')
    ax1.set_label("Plot of h(x) = cos(x)")
    ax1.set_xlabel("x-axis")
    ax1.set_ylabel("y-axis")
    ax1.grid(True)
    ax1.legend()


    #right subplot
    ax2.plot(x, k_x, label = "k(x) = sin(x)", color = "red", linestyle = '-')
    ax2.set_label("Plot of k(x) = sin(x)")
    ax2.set_xlabel("x-axis")
    ax2.set_ylabel("y-axis")
    ax2.grid(True)
    ax2.legend()
    
    #adjust for overlapping (had to look up how to do this)
    plt.tight_layout()

    plt.show()
    
# 2nd function, vertical top-bottom 

def top_and_bottom_subplots():
    x = np.linspace(0, 4*np.pi, 10) #domain defined 

    #defining functions 
    h_x = np.cos(x)
    k_x = np.sin(x)

    fig, (ax1, ax2) = plt.subplots(2,1, figsize= (10,8)) #creating the figure with two subplots 
    
    #top subplot
    ax1.plot(x, h_x, label = "h(x) = cos(x)", color = "blue", linestyle = '-')
    ax1.set_label("Plot of h(x) = cos(x)")
    ax1.set_xlabel("x-axis")
    ax1.set_ylabel("y-axis")
    ax1.grid(True)
    ax1.legend()

    #bottom subplot
    ax2.plot(x, k_x, label="k(x) = sin(x)", color='red', linestyle = '-')
    ax2.set_title("Plot of k(x) = sin(x)")
    ax2.set_xlabel("x-axis")
    ax2.set_ylabel("y-axis)")
    ax2.grid(True)
    ax2.legend()

    #adjust for overlapping (had to look up how to do this)
    plt.tight_layout()

        plt.show()