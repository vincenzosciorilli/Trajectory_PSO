import numpy as np
from initialization import particle_initialization
from pso import run_pso
from visualization import plot_trajectory
from visualization import plot_fitness
from animation import animate_swarm

# ---------------------------------------------------------------------
# Problem Setup

mu_earth = 3.986e14  # [m^3/s^2]

r0 = np.array([6.571e6, 0])    # [m]  
v0 = np.array([0, 7.784e3])    # [m/s] Circular orbital velocity at 200 km altitude
state0 = np.hstack((r0, v0))

target_position = np.array([10e6, 0]) 
initial_distance = np.linalg.norm(r0 - target_position)

# --------------------------------------------------------------------
# Swarm Initialization

dv_max = 4000  # [m/s]
T_max = 5000   # [s]
n_particles = 30
swarm = [particle_initialization(T_max, dv_max) for _ in range(n_particles)]

print("\nSwarm initialization:")
for i, p in enumerate(swarm):
    t1, dv1, theta1 = p
    print(f"- Particle {i+1}: t1={t1:.2f}s, ΔV={dv1:.2f} m/s, θ={theta1:.2f} rad")
print()

# --------------------------------------------------------------------------------------------------------
# Running PSO

n_iterations = 30
best_particle, best_fitness, iteration_index, particle_index, x_best_1, x_best_2, y_best_1, y_best_2, distance_best, positions_history, global_best_history = run_pso(
    swarm, state0, mu_earth, T_max, target_position, n_iterations, dv_max, initial_distance
)

print("\nPSO Results:")
print(f"| Best fitness: {best_fitness:.2f} m - Iteration {iteration_index+1}, Particle #{particle_index+1}, Final distance to target = {distance_best:.2f} m")
print(f"| Optimal Parameters: t1={best_particle[0]:.2f}s, ΔV={best_particle[1]:.2f} m/s, θ={best_particle[2]:.2f} rad\n")

# ----------------------------------------------------------------------------------------------------------
# Results Visualization

dvx_best = best_particle[1]*np.cos(best_particle[2])
dvy_best = best_particle[1]*np.sin(best_particle[2])

plot_trajectory(x_best_1, x_best_2, y_best_1, y_best_2, dvx_best, dvy_best, target_position)
plot_fitness(n_iterations, global_best_history)

#-----------------------------------------------------------------------------------------------------------
# Animation of Swarm Evolution

animate_swarm(positions_history, T_max, dv_max, n_iterations)