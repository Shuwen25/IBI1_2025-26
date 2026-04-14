# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

#It also makes sense to define a variable N that holds the total number of people in the population.
N=10000

#define the basic variables of the model, one for each of the population (Susceptible,Infected, and Recovered).
I=1
S=N-I
R=0

#define beta and gamma. Here, we use 0.3 for beta and 0.05 for gamma.
beta=0.3
gamma=0.05

#create arrays for each of your variables to track how they evolve over time.
S_list=[S]
I_list=[I]
R_list=[R]

step=1000 #loop over 1000 time points

for _ in range(step): #_ as a variable only used for step recording
    p_infected=beta*(I/N) #account for infection rate by multiplying beta by the proportion of infected people in the population
    new_infected=np.random.choice(range(2),S,p=[1-p_infected,p_infected]).sum()
    new_recovered=np.random.choice(range(2),I,p=[1-gamma,gamma]).sum()

    S-=new_infected
    I+=new_infected
    R+=new_recovered

    #add new data in the lists
    S_list.append(S)
    I_list.append(I)
    R_list.append(R)

#plot results: Plot the numbers of susceptible, infected, and recovered people as a function of time
plt.figure(figsize=(6,4),dpi=150)
plt.plot(S_list,label="Suspectible")
plt.plot(I_list,label="Infected")
plt.plot(R_list,label="Recovered")
plt.xlabel('Time')
plt.ylabel('Number of people')
plt.legend()
plt.title("SIR model")
plt.savefig("SIR model.png",format="png")


