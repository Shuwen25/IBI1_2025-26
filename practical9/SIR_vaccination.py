# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

#It also makes sense to define a variable N that holds the total number of people in the population.
N=10000

#define vaccine ratio in population
V_ratio=[0, 0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]

plt.figure(figsize=(6,4),dpi=150) #only draw one plot

#define the basic variables of the model, one for each of the population (Susceptible,Infected, and Recovered).
for idx,vax in enumerate(V_ratio):
    I=1
    V=int(vax*N) #extend model to include an additional group of vaccinated people
    S=N-I-V
    R=0
    

    #define beta and gamma. Here, we use 0.3 for beta and 0.05 for gamma.
    beta=0.3
    gamma=0.05

    #create arrays for each of your variables to track how they evolve over time.
    I_list=[I]

    step=1000 #loop over 1000 time points

    for _ in range(step): #_ as a variable only used for step recording
        p_infected=beta*(I/N) #account for infection rate by multiplying beta by the proportion of infected people in the population
        if S <= 0:
            new_infected = 0
        else:
            new_infected=np.random.choice(range(2),S,p=[1-p_infected,p_infected]).sum()
        
        new_recovered=np.random.choice(range(2),I,p=[1-gamma,gamma]).sum()
        
        S-= new_infected
        I+=new_infected-new_recovered
        
        #add new data in the lists
        I_list.append(I)

    #plot results: Plot the numbers of susceptible, infected, and recovered people as a function of time
    plt.plot(I_list,label=str(int(vax*100))+"%",color=cm.viridis(idx*25))
plt.xlabel('Time')
plt.ylabel('Number of people')
plt.legend()
plt.title("SIR model with different vaccination rates")
plt.savefig("SIR vaccination.png",format="png")
plt.show()


