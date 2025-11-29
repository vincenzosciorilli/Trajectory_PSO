import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

def animate_swarm(positions_history, T_max, dv_max, n_iterations):
    """
    Animate the swarm evolution in 3D parameter space:
    - x-axis: maneuver time t1 [s]
    - y-axis: ΔV magnitude [m/s]
    - z-axis: maneuver angle θ [rad]
    """
  
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    def update(frame):
        ax.clear()
        ax.set_xlim(0, T_max)
        ax.set_ylim(0, dv_max)
        ax.set_zlim(0, 2*np.pi)
        ax.set_xlabel("t1 [s]")
        ax.set_ylabel("ΔV [m/s]")
        ax.set_zlabel("θ [rad]")
        ax.set_title(f"Iteration {frame+1}")

        data = positions_history[frame] 
        ax.scatter(data[:,0], data[:,1], data[:,2], c='blue', marker='o')

    ani = FuncAnimation(fig, update, frames=n_iterations, interval=500, repeat=False)
    ani.save("swarm_animation.gif", writer="pillow", fps=2)
    
    plt.show()