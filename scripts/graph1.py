import matplotlib.pyplot as plt
 
# function to add value labels
def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i], ha = 'center')
 
if __name__ == '__main__':
    # creating data on which bar chart will be plot
    x = ['default','next_line','berti','sangam','ipcp']
    y = [0.50375,0.663,0.709,0.71,0.7208]
    plt.figure(figsize = (10,10))
    # making the bar chart on the data
    plt.ylim(0,1)
    
    plt.bar(x, y,width=0.23)
    
     
    # calling the function to add value labels
    addlabels(x, y)
     
    # giving title to the plot
   
     
    # giving X and Y labels
    plt.xlabel("PREFETCHERS")
    plt.ylabel("Average IPC value")
     
    # visualizing the plot
    plt.show()
