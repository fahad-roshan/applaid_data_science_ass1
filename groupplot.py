"""
group graph

"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("D:\\soccer-spi\\spi_global_rankings.csv")
data_ = data.head(20)
print(data.columns)


plt.figure(figsize=(45,20))
teams = np.arange(len(data_["name"]))
width=0.40
plt.xlabel("Clubs",fontsize=40)
plt.ylabel("off and def",fontsize=40)
plt.title("Comparing the def and off rating of each clubs ",fontsize=70)
r1 = plt.bar(teams-0.2,data_["off"],width,color="blue",label="off")
r2 = plt.bar(teams+0.2,data_["def"],width,color="red",label="def")
plt.xticks(teams,data_["name"])
plt.bar_label(r1, padding=3)
plt.bar_label(r2, padding=3)
plt.legend(fontsize=40)
plt.show()
