# Pseudocode
# 1. Total students in class: 91
# 2. Input initial infected and daily growth rate
# 3. Simulate each day's new infections
# 4. Print day number and infected count
# 5. Print total days when everyone is infected

total = 91

# Get user inputs
initial = float(input("Initial infected people: "))
rate = float(input("Daily growth rate (e.g. 0.2 = 20%): "))

# Basic input check
if initial <= 0 or rate < 0:
    print("Please enter valid positive numbers.")
else:
    current = initial
    days = 0

    # Clear table header
    print("\nDay    Infected People")
    print(f"Day {days:2d}    {current:.1f}")

    # Daily simulation
    while current < total:
        days += 1
        current = current * (1 + rate)
        
        # Make sure we don't go over total people
        if current > total:
            current = total
        
        print(f"Day {days:2d}    {current:.1f}")

    # Final result
    print(f"Total days to infect all {total} students: {days}")
