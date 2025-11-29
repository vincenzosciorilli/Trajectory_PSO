# Trajectory_PSO
## Introduction
This project implements a Particle Swarm Optimization (PSO) algorithm to optimize the parameters of an orbital maneuver.  
The problem addressed is the following: a spacecraft orbiting a planet (e.g., Earth) must reach a target point in space at a specific time.
For simplicity, Earth is modeled as a point mass generating a central gravitational field, without considering perturbations or non-spherical effects.
The algorithm attempts to determine:
- the time at which to apply the ΔV (velocity impulse),
- the magnitude of the ΔV,
- the angle of application.

The fitness function to be minimized combines two factors:
- the final distance from the target point,
- the magnitude of the ΔV applied to the spacecraft.

This way, the solution balances the effectiveness of the maneuver with the energetic cost required.

The code was developed with the support of Microsoft Copilot, which assisted in the coding and documentation process.

---

## Project Structure
- **main.py**: Main script that runs initialization, PSO, and visualization of results.
- **initialization.py**: Function to generate the swarm of particles.
- **simulation.py**: Orbital dynamics and trajectory simulation.
- **fitness.py**: Fitness function to evaluate solutions.
- **pso.py**: Implementation of the PSO algorithm.
- **visualization.py**: Plots of the trajectory and fitness convergence.
- **animation.py**: Animation of swarm evolution in parameter space.

---

## Expected Output
- **Console**: prints particle parameters and the optimal result.
- **Plots**: orbital trajectory and fitness convergence.
- **Animation**: swarm evolution over iterations, also saved as `swarm_animation.gif`.

---

## Requirements
- Python ≥ 3.8
- Libraries:
  - `numpy`
  - `matplotlib`
  - `scipy`
 
---

## How to Run
 
All source files are contained inside the `Trajectory_PSO` package, including the `__init__.py` file.  

Make sure you have Python 3.8 or higher installed, then install the required libraries with  
`pip install numpy matplotlib scipy`.  

Once the environment is ready, simply launch the simulation by running  
`python Trajectory_PSO/main.py`.


The console will display the particle parameters and the optimal solution, plots will show the orbital trajectory and the fitness convergence, and an animation of the swarm evolution will be generated and saved as `swarm_animation.gif`.

![Figure_1](https://github.com/user-attachments/assets/432245ce-c7ac-4607-b4ea-36d0a3d4d597)

![Figure_2](https://github.com/user-attachments/assets/4e297ee3-bca9-4203-aad9-e3112bc31ee6)

![Figure_3](https://github.com/user-attachments/assets/a5a80486-4198-41db-82de-28a23c9b8dab)

