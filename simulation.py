import numpy as np
from scipy.integrate import solve_ivp

def orbital_dynamics(t, state, mu):
    x, y, vx, vy = state
    r = np.array([x, y])
    d = np.linalg.norm(r)
    ax = -mu * x / d**3
    ay = -mu * y / d**3
    return [vx, vy, ax, ay]

def trajectory_simulation(particle, state0, mu_earth, T_max, target):
    t1, dv1, theta1 = particle

    # First integration: from 0 to t1
    t_span1 = (0, t1)

    if t1 <= 0 or T_max <= t1:
        return None, None, np.inf # Invalid trajectory

    sol1 = solve_ivp(orbital_dynamics, t_span1, state0, args=(mu_earth,), t_eval=np.linspace(*t_span1, 500), method='RK23', rtol=1e-10, atol=1e-13)
    if sol1.status != 0 or sol1.y is None or sol1.y.shape[1] == 0:
        return None, None, np.inf # Invalid trajectory
    
    # Apply ΔV in polar coordinates
    x, y = sol1.y[0][-1], sol1.y[1][-1]
    vx, vy = sol1.y[2][-1], sol1.y[3][-1]
    vx += dv1 * np.cos(theta1)
    vy += dv1 * np.sin(theta1)
    state1 = [x, y, vx, vy]

    # Second integration: from t1 to T_max
    t_span2 = (t1, T_max)

    sol2 = solve_ivp(orbital_dynamics, t_span2, state1, args=(mu_earth,), t_eval=np.linspace(*t_span2, 500), method='RK23', rtol=1e-10, atol=1e-13)
    if sol2.status != 0 or sol2.y is None or sol2.y.shape[1] == 0:
        return None, None, np.inf

    # Full trajectory
    x_traj_1 = sol1.y[0] 
    x_traj_2 = sol2.y[0]
    y_traj_1 = sol1.y[1]
    y_traj_2 = sol2.y[1]

    # Final distance from target
    x_final, y_final = sol2.y[0][-1], sol2.y[1][-1]
    distance = np.linalg.norm([x_final - target[0], y_final - target[1]])

    return x_traj_1, x_traj_2, y_traj_1, y_traj_2, distance
