# 【Pseudocode: Creatinine Clearance (CrCl) Calculator (Cockcroft-Gault Formula)】
# 1. Define core objective: Calculate CrCl using Cockcroft-Gault formula with input validation
# 2. Input parameters (with validation rules):
#      Age: Integer/float, must be < 100 years
#      Weight: Integer/float, must be 20kg < weight < 80kg
#      Gender: String, must be "Male" or "Female" 
#      Creatinine (Cr): Integer/float, must be 0 < Cr < 100 µmol/L
# 3. Input validation logic:
#      Check each parameter against rules; collect invalid parameters in a list
#      If invalid parameters exist: Print the list of invalid variables and exit calculation
#      If all parameters valid: Proceed to calculate CrCl
# 4. Cockcroft-Gault Formula (adapted for µmol/L unit):
#      For Males: CrCl = [(140 - Age) × Weight × 1.23] / Cr
#      For Females: CrCl = [(140 - Age) × Weight × 1.23 × 0.85] / Cr
# 5. Output result: Print CrCl with 2 decimal places (unit: mL/min)
# 6. Error handling: Catch non-numeric input errors 

# Actual Code Start
def calculate_creatine_clearance():
    # Initialize list to store invalid parameters
    invalid_params = []
    
    # Step 1: Input and validate each parameter
    try:
        # Input and validate Age
        age = float(input("Please enter age (years, < 100): "))
        if age >= 100:
            invalid_params.append("age (must be < 100)")
        
        # Input and validate Weight
        weight = float(input("Please enter weight (kg, 20 < weight < 80): "))
        if weight <= 20 or weight >= 80:
            invalid_params.append("weight (must be 20 < weight < 80)")
        
        # Input and validate Gender
        gender = input("Please enter gender (Male/Female): ").strip()
        if gender not in ["Male", "Female"]:
            invalid_params.append("gender (must be 'Male' or 'Female')")
        
        # Input and validate Creatinine (Cr)
        cr = float(input("Please enter creatinine concentration (µmol/L, 0 < Cr < 100): "))
        if cr <= 0 or cr >= 100:
            invalid_params.append("creatinine (Cr) (must be 0 < Cr < 100)")
    
    # Catch non-numeric input errors for age/weight/Cr
    except ValueError:
        print("Error: Age, weight and creatinine must be numeric values (e.g., 35, 60.5, 80)!")
        return
    
    # Step 2: Check if any invalid parameters exist
    if invalid_params:
        print("\nInvalid input detected! Please correct the following parameters:")
        for param in invalid_params:
            print(f"- {param}")
        return  # Exit without calculation
    
    # Step 3: Calculate CrCl using Cockcroft-Gault formula
    if gender == "Male":
        crcl = ((140 - age) * weight * 1.23) / cr
    else:  # Female
        crcl = ((140 - age) * weight * 1.23 * 0.85) / cr
    
    # Step 4: Output the result with 2 decimal places
    print("\n===== Creatinine Clearance (CrCl) Result =====")
    print(f"Age: {age} years")
    print(f"Weight: {weight} kg")
    print(f"Gender: {gender}")
    print(f"Creatinine (Cr): {cr} µmol/L")
    print("---------------------------------------------")
    print(f"Calculated CrCl: {crcl:.2f} mL/min")

# Execute the calculator function
calculate_creatine_clearance()
