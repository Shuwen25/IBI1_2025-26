import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# set the working directory
os.chdir(r"C:\Users\zsw\OneDrive - International Campus, Zhejiang University\桌面\IBI\week10")  #set the working directory
print("current working path:", os.getcwd())  #check the current working directory
print("files in the current working directory:", os.listdir())  #check the files in the current working directory

# introduce the data set
dalya_data=pd.read_csv("dalys-rate-from-all-causes.csv")  #read the data

print("The first 5 rows of the data set:\n", dalya_data.head(5))  #check the first 5 rows of the data set
print("The information of the data set:\n", dalya_data.info())  #check the information of the data set
print("The statistical summary of the data set:\n", dalya_data.describe())  #check the statistical summary of the data set

# iloc is used to select data by position
print("The first row and the forth column of the data set:\n", dalya_data.iloc[0, 3])  #check the first row and the fourth column of the data set

first_10=dalya_data.iloc[0:10, 2:4]
print("The first ten rows and the third and fourth columns of the data set:\n", first_10)  #check the first ten rows and the third and fourth columns of the data set (Year and DALYs)

# The year of biggest DALYs in Afghanistan in the first 10 rows
# answer: 1990, which is the first row of the data set
afghanistan_max_year=dalya_data.iloc[0:10].loc[dalya_data["Entity"]=="Afghanistan", "Year"].iloc[0] # check the year of biggest DALYs in Afghanistan in the first 10 rows
print("The year of biggest DALYs in Afghanistan in the first 10 rows:", afghanistan_max_year)  #print the year of biggest DALYs in Afghanistan in the first 10 rows

my_columns=[True,True,False,True] # create a boolean list to select the columns of the data set
print("The first 3 rows of the data set with the selected columns:\n", dalya_data.iloc[0:3, my_columns])  #check the first 3 rows of the data set with the selected columns

#loc is used to select data by label
zimbabwe=dalya_data.loc[dalya_data["Entity"]=="Zimbabwe",["Year","DALYs"]]  #select the data of Zimbabwe
print("All the DALYs of Zimbabwe in every year:\n", zimbabwe)  #check all the DALYs of Zimbabwe

zim_first=zimbabwe["Year"].min() #check the first year of the data set of Zimbabwe
zim_last=zimbabwe["Year"].max() #check the last year of the data set of Zimbabwe
print("The first year of the data set of Zimbabwe:", zim_first)  #print the first year of the data set of Zimbabwe
print("The last year of the data set of Zimbabwe:", zim_last)  #print the last year of the data set of Zimbabwe

# The country with the highest/lowest DALYs in 2019
recent_data=dalya_data.loc[dalya_data["Year"]==2019, ["Entity", "DALYs"]]  #select the data of 2019
#check the country with the highest DALYs in 2019
#answer: Lesotho
max_country = recent_data.loc[recent_data["DALYs"] == recent_data["DALYs"].max(), "Entity"].values[0] 
#check the country with the lowest DALYs in 2019
#answer: Singapore
min_country = recent_data.loc[recent_data["DALYs"] == recent_data["DALYs"].min(), "Entity"].values[0] 
print("The country with the highest DALYs in 2019:", max_country)  #print the country with the highest DALYs in 2019
print("The country with the lowest DALYs in 2019:", min_country) #print the country with the lowest DALYs in 2019

# plot the DALYs of country with the lowest DALYs in every year
country_data = dalya_data.loc[dalya_data["Entity"] == min_country] #select the data of the country with the lowest DALYs in every year
plt.plot(country_data["Year"], country_data["DALYs"])  #plot the lowest DALYs in every year
plt.xlabel("Year")  #set the x label
plt.ylabel("DALYs")  #set the y label
plt.title("DALYs of " + min_country + " in every year")  # set the title of the plot
plt.show()  #show the plot


# Extra question: Distribution of DALYs across all countries in 2019
# Line: 63-70
data_2019 = dalya_data[dalya_data["Year"] == 2019]

plt.figure(figsize=(8, 5))
plt.boxplot(data_2019["DALYs"], vert=False)
plt.xlabel("DALYs rate")
plt.title("Distribution of DALYs across all countries in 2019")
plt.tight_layout()
plt.show()
