import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

initial_pos1 = 1
initial_pos2 = 4 
initial_velocity1 = 0.05
initial_velocity2 = -0.1
mass1 = 1.0
mass2 = 1.5
num_frames = 1000
boxsize = 5
pos1 = initial_pos1
pos2 = initial_pos2
vel1 = initial_velocity1
vel2 = initial_velocity2


def balls_colision (vel1,mass1,vel2,mass2):
    vel1, vel2= (vel1*(mass1-mass2)+2*vel2*mass2)/(mass1+mass2), (vel2*(mass2-mass1)+2*vel1*mass1)/(mass1+mass2)  
    return vel1,vel2
def wall_colision_1 (vel1):
    vel1=-vel1
    return vel1
def wall_colision_2 (vel2):
    vel2=-vel2
    return vel2


def simulate_collision(initial_pos1,initial_pos2,initial_velocity1,initial_velocity2,mass1,mass2,num_frames,boxsize):
    pos1 = [initial_pos1]
    pos2 = [initial_pos2]
    vel1 = initial_velocity1
    vel2 = initial_velocity2

    for i in range(1, num_frames):
        pos1.append(pos1[-1] + vel1)
        pos2.append(pos2[-1] + vel2)

        if pos1[-1] > pos2[-1]:
            vel1, vel2 = balls_colision(vel1, mass1, vel2, mass2)
        elif pos1[-1] < 0:
            vel1 = wall_colision_1(vel1)
        elif pos2[-1] > boxsize:
            vel2 = wall_colision_2(vel2)

    create_animation(pos1, pos2, boxsize)

def create_animation(positions1, positions2, boxsize):
    num_frames = len(positions1)
    
    fig, ax = plt.subplots()
    ax.set_xlim(0, boxsize)
    ax.set_ylim(-0.1, 0.1)
    
    ball1, = ax.plot(positions1[0], 0, 'bo', markersize=10)
    ball2, = ax.plot(positions2[0], 0, 'ro', markersize=10)

    def update(frame):
        ball1.set_xdata(positions1[frame])
        ball2.set_xdata(positions2[frame])
        return ball1, ball2

    ani = FuncAnimation(fig, update, frames=num_frames, blit=True)
    plt.show()


simulate_collision(initial_pos1,initial_pos2,initial_velocity1,initial_velocity2,mass1,mass2,num_frames,boxsize)

