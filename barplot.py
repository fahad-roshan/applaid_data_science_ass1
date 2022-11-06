"""
barplot

"""
import pandas as pd
import matplotlib.pyplot as plt

# reading the csv  
data = pd.read_csv("D:\\soccer-spi\\spi_global_rankings.csv")
data_ = data.head(20)
print(data.columns)


# plotting the bar plot
plt.figure(figsize=(45,20))
plt.bar(data_["name"],data_["spi"],color=["blue","indigo","green","pink","orange","black","cyan","chocolate","gold","coral","red","darkblue","lightgreen","darkred","wheat","azure","yellow","crimson","thistle","plum"],edgecolor="black",align="center")
plt.xlabel("SOCCER TEAMS",fontsize=30)
plt.ylabel("SPI",fontsize=30)
plt.title("SPI RATING ",fontsize=40)
plt.show()
