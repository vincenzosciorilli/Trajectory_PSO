import numpy as np

def particle_initialization(T_max, dv_max):
    # Time of the maneuvre
    t1 = np.random.uniform(0, T_max)

    # ΔV magnitude ≤ dv_max
    dv1 = np.random.uniform(0, dv_max)
    theta1 = np.random.uniform(0, 2 * np.pi)

    return [t1, dv1, theta1]
