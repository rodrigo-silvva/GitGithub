import random
import matplotlib.pyplot as plt

def random_walk(num_steps, prob_right, num_particles):
    particle_paths = []
    
    for _ in range(0,num_particles):
        posição = [0]
        for _ in range (0,num_steps):
            x=random.random()
            if x<=prob_right:
                posição.append(posição[-1] + 1)
            else:
                posição.append(posição[-1] - 1)
        particle_paths.append(posição)
    create_plot(num_steps, particle_paths)

    return particle_paths
    

def create_plot(num_steps,particle_paths):

    time = [x for x in range (len(particle_paths[0]))]

# Build the plot with all the particles
    for particle_path in particle_paths:
        plt.plot(particle_path,time)
    plt.title('Random Walk - N particles')
    plt.xlabel('Position')
    plt.ylabel('Time')
    plt.show()

num_steps = 100
prob_right = 0.5
num_particles = 10

random_walk (num_steps,prob_right,num_particles)