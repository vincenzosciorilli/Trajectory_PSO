import matplotlib.pyplot as plt

def plot_trajectory(x_best_1, x_best_2, y_best_1, y_best_2, dvx_best, dvy_best, target_position):
    plt.figure(figsize=(8, 6))
    plt.plot(x_best_1, y_best_1, color='b', label='Trajectory 1')
    plt.plot(x_best_2, y_best_2, color='g', label='Trajectory 2')
    plt.plot(0, 0, 'bo', label='Earth')
    plt.plot(target_position[0], target_position[1], 'ro', label='Target')

    # Maneuver point application
    plt.plot(x_best_1[-1], y_best_1[-1], 'rx', label='ΔV1')

    # ΔV vector rapresentation
    plt.quiver(x_best_1[-1], y_best_1[-1], dvx_best, dvy_best, angles='xy', scale_units='xy', scale=1e-3, color='r')

    plt.xlabel("x (m)")
    plt.ylabel("y (m)")
    plt.title("Optimized Orbital Trajectory")
    plt.axis('equal')
    plt.grid()
    plt.legend()
    plt.show()

def plot_fitness(n_iterations, global_best_history):
    plt.figure(figsize=(8, 6))
    plt.plot(range(1, n_iterations+1), global_best_history, color='b', marker='o', label='GBF over Iterations')
    plt.xlabel("Iterations")
    plt.ylabel("Global Best Fitness")
    plt.title("PSO Convergence")
    plt.grid(True)
    plt.legend()
    plt.show()