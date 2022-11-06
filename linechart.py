"""
off vs def vs team ranking 
"""

import pandas as pd
import matplotlib.pyplot as plt

# reading the csv file
data = pd.read_csv("D:\\soccer-spi\\spi_global_rankings.csv")

# taking the first 20 data from the data set
data_ = data.head(20)

# plotting the graph 
plt.figure(figsize=(40,15))
plt.plot(data_["name"],data_["def"],"-p",linewidth=4,color="black",markersize=30,markerfacecolor="red",label="def")  
plt.plot(data_["name"],data_["off"],"-p",linewidth=4,color="blue",markersize=30,markerfacecolor="green",label="off")
plt.xlabel("Teams",fontsize=40)  # labelling the x axis
plt.ylabel("def and off",fontsize=40) # labelling the y axis
plt.title("line plot",fontsize=60) # giving the title
plt.legend(fontsize=50) # giving the legend
plt.show()