import numpy as np
import pyexotica as exo

exo.Setup.initRos()
solver = exo.Setup.loadSolver('{exotica_baxter}/config/baxter_ik.xml')
problem = solver.getProblem()
scene = problem.getScene()

print("Robot DOF: ", problem.N)

problem.update(np.zeros(problem.N,))

# Publish transforms to visualise in rviz
scene.getSolver().publishFrames()

# Get FK
problem.update(np.zeros(problem.N,))
print("FK: ", problem.Phi.data)
