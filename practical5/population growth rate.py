pop_2020={"UK":66.7,"China":1426,"Italy":59.4,"Brazil":208.6,"USA":331.6}
pop_2024={"UK":69.2,"China":1410,"Italy":58.9,"Brazil":212.0,"USA":340.1}
pop_changes={}

for country in list(pop_2020.keys()):
    percent_change=(float(pop_2024[country])-float(pop_2020[country]))/float(pop_2020[country])*100
    print(f"The percentage population change from 2020 to 2024 of {country} is {percent_change}.")
    pop_changes[country]=float(percent_change)

country_change_list = []
for country, change in pop_changes.items():
    country_change_list.append([country, change])

n = len(country_change_list) 
for i in range(n):
    for j in range(0, n - i - 1):
        if country_change_list[j][1] < country_change_list[j+1][1]:
            country_change_list[j], country_change_list[j+1] = country_change_list[j+1], country_change_list[j]

sorted_changes = country_change_list

print("Sort by population change percentage in descending order ：")
for item in sorted_changes:
    country = item[0]  
    change = item[1]   
    print(f"{country}: {change}")

largest_increase_country = sorted_changes[0][0]
largest_increase_value = sorted_changes[0][1]
largest_decrease_country = sorted_changes[-1][0]
largest_decrease_value = sorted_changes[-1][1]

print(f"The country with the largest population growth：{largest_increase_country} ({largest_increase_value})")
print(f"The country with the largest population decline：{largest_decrease_country} ({largest_decrease_value})")