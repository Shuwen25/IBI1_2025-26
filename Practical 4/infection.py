# 1. Define initial parameters:
#      Initial infected number (initial_infected): User input or custom value (e.g., 1)
#      24-hour growth rate (growth_rate): User input or custom value (e.g., 0.2 for 20%)
#      Total class population (total_people): Fixed at 91 people
#      Initialize current infected number (current_infected) = initial_infected
#      Initialize days counter (days) = 0
# 2. Loop to calculate daily infected numbers:
#    While current_infected < total_people:
#       a. Increment days by 1
#       b. Calculate new infected people for the day = current_infected * growth_rate
#       c. Update current_infected (Note: Infected number cannot exceed total population, and must be integer)
#       d. Output the day number and infected count (keep 1 decimal place or round for real-world scenario)
# 3. After loop ends, output total days required for full infection
# 4. Error handling: Ensure initial infected number/growth rate are positive to avoid invalid input

# Actual Code Start
def calculate_infection_days():
    # Fixed parameter: Total number of students in IBI1 class
    total_people = 91
    
    # Input initial parameters (with error handling to avoid invalid input)
    try:
        initial_infected = float(input("Enter initial number of infected people: "))
        growth_rate = float(input("Enter 24-hour growth rate (e.g., enter 0.2 for 20%): "))
        
        # Validate input legality
        if initial_infected <= 0 or growth_rate < 0:
            print("Error: Initial infected number must be greater than 0, and growth rate cannot be negative!")
            return
        if initial_infected >= total_people:
            print(f"Initial infected number {initial_infected} ≥ total class population {total_people}, all people are already infected!")
            return
        
    except ValueError:
        print("Error: Please enter valid numbers (e.g., 1, 0.2)!")
        return
    
    # Initialize variables
    current_infected = initial_infected
    days = 0
    
    # Print header
    print("\n===== Daily Infected Population Statistics =====")
    print(f"Total class population: {total_people} | Initial infected: {initial_infected} | Daily growth rate: {growth_rate*100}%")
    print("-----------------------------------------------")
    print(f"Day {days} | Infected people: {current_infected:.1f}")
    
    # Loop to calculate daily infected numbers until full infection
    while current_infected < total_people:
        days += 1
        # Calculate new infected people for the day
        new_infected = current_infected * growth_rate
        # Update current infected (not exceeding total population, keep 1 decimal place)
        current_infected = min(current_infected + new_infected, total_people)
        # Output daily infected count
        print(f"Day {days} | Infected people: {current_infected:.1f}")
    
    # Output final result
    print("-----------------------------------------------")
    print(f"Total days required for full infection of IBI1 class ({total_people} people): {days} days")

# Execute the function
calculate_infection_days()
