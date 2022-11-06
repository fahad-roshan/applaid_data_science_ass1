"""
top 20 ranked teams in football with thier corresponding leagues

"""

import pandas as pd
import matplotlib.pyplot as plt

# reading the csv file data
data = pd.read_csv("D:\\soccer-spi\\spi_global_rankings.csv")
data_ = data.head(20)


#mapping the league to a correspinding number and create a new column
data_["league1"] = data_["league"].map({"Barclays Premier League":0,"Dutch Eredivisie":1,"French Ligue 1":2,"German Bundesliga":3,"Italy Serie A":4,"Spanish Primera Division":5,"Portuguese Liga":6}).astype(float)
print(data_["league1"])
print(data_)

# grouping the data's in column league and taking its count 
d = data_.groupby(["league"])
d = d["rank"].count()

print(d)

#plotting the pie chart
plt.figure()
plt.pie(d,labels=["Barclays Premier League","Dutch Eredivisie","French Ligue 1","German Bundesliga","Italy Serie A","Spanish Primera Division","Portuguese Liga"],autopct="%1.1f%%")
plt.title("The first 20 rated Teams and their corresponding league")
plt.legend(loc = "upper left",shadow=False,prop={"size":6})
plt.show()
