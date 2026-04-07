heart_rate=(72,	60,	126, 85, 90, 59, 76, 131, 88, 121, 64)
Number_of_patients=len(heart_rate)
Mean_heart_rate=sum(heart_rate)/Number_of_patients
print(f"There are {Number_of_patients} joining the analysis. Their main heart rate is {Mean_heart_rate}")

Low_heart_rate=0
Normal_heart_rate=0
High_heart_rate=0
for i in heart_rate:
    if i < 60:
        Low_heart_rate+=1
    elif i > 120:
        High_heart_rate+=1
    else:
        Normal_heart_rate+=1
print(f"The number of people who have low heart rate is {Low_heart_rate}.")
print(f"The number of people who have normal heart rate is {Normal_heart_rate}.")
print(f"The number of people who have high heart rate is {High_heart_rate}.")

category_dict = { "low heart rate": Low_heart_rate,"normal heart rate": Normal_heart_rate,"high heart rate": High_heart_rate}
most_common_category = max(category_dict, key=category_dict.get)
print(f"Most people have {most_common_category} (count: {category_dict[most_common_category]})")

import matplotlib.pyplot as plt

labels=category_dict.keys()
sizes=category_dict.values()

plt.pie(sizes, labels=labels,autopct="%1.1f%%",shadow=False, startangle=90)
plt.axis("equal")
plt.title("Heart Rate Category Distribution")
plt.show()