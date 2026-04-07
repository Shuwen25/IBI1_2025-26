# Pseudocode
# 1. Get age, weight, gender, creatinine
# 2. Check if inputs are valid
# 3. Calculate CrCl using Cockcroft-Gault formula
# 4. Show result

# Get inputs
age = float(input("Age: "))
weight = float(input("Weight (kg): "))
gender = input("Gender (Male/Female): ")
cr = float(input("Creatinine (µmol/L): "))

# Check inputs
valid = True
if age >= 100:
    print("Age must be < 100")
    valid = False
if weight <= 20 or weight >= 80:
    print("Weight must be between 20 and 80")
    valid = False
if gender not in ["Male", "Female"]:
    print("Gender must be Male or Female")
    valid = False
if cr <= 0 or cr >= 100:
    print("Creatinine must be between 0 and 100")
    valid = False

# Calculate if valid
if valid:
    if gender == "Male":
        crcl = ((140 - age) * weight * 1.23) / cr
    else:
        crcl = ((140 - age) * weight * 1.23 * 0.85) / cr

    print("\nCrCl =", round(crcl, 2), "mL/min")
