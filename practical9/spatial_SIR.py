#import necessary library
import numpy as np
import matplotlib.pyplot as plt

#make array of all susceptible population
population=np.zeros((100,100))

#address the person with those exact coordinates in our population array and change their status from 0 (susceptible) to 1 (infected).
outbreak=np.random.choice(range(100),2)
population[outbreak[0],outbreak[1]]=1

#set parameters
beta=0.3
gamma=0.05

#8 dirctions of the indinfected people
directions = [(-1,-1), (-1,0), (-1,1),
              (0,-1),          (0,1),
              (1,-1),  (1,0), (1,1)]

#start simulation
for step in range(100):
    new_pop = population.copy()

    #traverse every individual
    for i in range(100):
        for j in range(100):

            # if it is infected people
            if population[i, j] == 1:

                # try to infect neighbors
                for dx, dy in directions:
                    ni = i + dx
                    nj = j + dy
                    if 0 <= ni < 100 and 0 <= nj < 100:
                        if new_pop[ni, nj] == 0:  # only susceptible people can be infected
                            if np.random.rand() < beta:
                                new_pop[ni, nj] = 1 

                # recovery
                if np.random.rand() < gamma:
                    new_pop[i, j] = 2  # 2 = recovered people

    population = new_pop


#use heat map
plt.figure(figsize=(6,4),dpi=150)
plt.imshow(population,cmap='viridis',interpolation='nearest')
plt.title("Spatial SIR Model")
plt.savefig("spatial_SIR.png", format="png")
plt.show()

