#1. Some simple math
# Scotland population data calculation (unit: million)
a=5.08 # Populatoion of scotland in 2004
b=5.33 # Populatoion of scotland in 2014
c=5.55 # Populatoion of scotland in 2024
d=b-a # Population change from 2004 to 2014
e=c-b # Populatoion change from 2014 to 2024
# Compare d and e: if e<d , growth slos down; if e>d, growth accelerates; if e=d, growth unchanged
if e<d:
  growth_trend = "slowing down"
elif e>d:
  growth_trend = "speeding up"
else:
  growth_trend = "unchanged"
print(f"Population change 2004-2014: {d} million")
print(f"Population change 2014-2024: {e} million")
print(f"Scotland's population growth trend: {growth_trend}")
# Conclusion: The population increased by 0.25 million from 2004 to 2014, and 0.22 million from 2014 to 2024. 
# Since e (0.22) < d (0.25), the population growth rate is slowing down.

#2.Booleans
X=True
Y=False
W=X or Y
# Truth table for W (X or Y)
# --------------------------
# X      | Y      | W (X or Y)
# --------------------------
# True   | True   | True
# True   | False  | True  # Result for the given X/Y values in this practical
# False  | True   | True
# False  | False  | False
# --------------------------
# Print the result of boolean operation
print(f"Boolean operation result: W={W}")
