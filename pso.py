import numpy as np
from simulation import trajectory_simulation
from fitness import fitness_function

def run_pso(swarm, state0, mu_earth, T_max, target_position, n_iterations, dv_max, initial_distance):
    w = 0.5
    c1 = 1.5
    c2 = 1.5
    alpha = 500

    n_particles = len(swarm)
    positions = np.array(swarm, dtype=np.float64)
    velocities = np.zeros_like(positions)
    positions_history = np.zeros((n_iterations, n_particles, positions.shape[1]))

    personal_best_positions = positions.copy()
    personal_best_scores = []
    global_best_history = []
    trajectories = []

    print("Swarm trajectory initialization\n")

    for p in positions:
        result = trajectory_simulation(p.tolist(), state0, mu_earth, T_max, target_position)
        if result[0] is None:
            score = 1e10 # Penalty for invalid trajectory
            x_traj_1, x_traj_2, y_traj_1, y_traj_2 = [], [], [], []
        else:
            x_traj_1, x_traj_2, y_traj_1, y_traj_2, distance_final = result
            score = fitness_function(distance_final, dv1=p[1], alpha=alpha)
        personal_best_scores.append(score)
        trajectories.append((x_traj_1, x_traj_2, y_traj_1, y_traj_2))

    global_best_index = np.argmin(personal_best_scores)
    global_best_position = personal_best_positions[global_best_index].copy()
    global_best_score = personal_best_scores[global_best_index]
    x_best_1, x_best_2, y_best_1, y_best_2 = trajectories[global_best_index]


    distance_best = initial_distance

    particle_index = global_best_index
    iteration_index = 0

    print("Trajectory optimization in progress")

    for iteration in range(n_iterations):
        print(f"\n--- Iteration {iteration+1} ---")
        for i in range(n_particles):
            r1 = np.random.rand(positions.shape[1])
            r2 = np.random.rand(positions.shape[1])

            velocities[i] = (
                w * velocities[i]
                + c1 * r1 * (personal_best_positions[i] - positions[i])
                + c2 * r2 * (global_best_position - positions[i])
            )

            positions[i] += velocities[i]

            # Adjusting parameters
            t1, dv1, theta1 = positions[i]

            t1 = np.clip(t1, 0, T_max)
            dv1 = np.clip(dv1, 0, dv_max)
            theta1 = theta1 % (2 * np.pi)

            positions[i][:] = [t1, dv1, theta1]

            result = trajectory_simulation(positions[i].tolist(), state0, mu_earth, T_max, target_position)
            if result[0] is None:
                score = 1e10 # Penalty for invalid trajectory
                continue

            x_traj_1, x_traj_2, y_traj_1, y_traj_2, distance_final = result
            score = fitness_function(distance_final, dv1=positions[i][1], alpha=alpha)

            if score < personal_best_scores[i]:
                personal_best_scores[i] = score
                personal_best_positions[i] = positions[i].copy()

            if score < global_best_score:
                global_best_score = score
                global_best_position = positions[i].copy()
                particle_index = i
                iteration_index = iteration
                x_best_1 = x_traj_1
                x_best_2 = x_traj_2
                y_best_1 = y_traj_1
                y_best_2 = y_traj_2
                distance_best = distance_final

            print(f" - Particle {i+1}: t1= {positions[i][0]:.2f} s, ΔV= {positions[i][1]:.2f} m/s, θ= {positions[i][2]:.2f} rad, Final distance to target: {distance_final:.2f} m")
            print(f"Fitness score: {score:.2f}")
        
        positions_history[iteration] = positions.copy()
        global_best_history.append(global_best_score)

    return global_best_position.tolist(), global_best_score, iteration_index, particle_index, x_best_1, x_best_2, y_best_1, y_best_2, distance_best, positions_history, global_best_history