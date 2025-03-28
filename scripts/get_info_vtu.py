import meshio
import sys
import numpy as np
np.set_printoptions(threshold=np.inf)  # Disable truncation


# Read the .vtu file
mesh = meshio.read(sys.argv[1])

# Extract information
print("Points:\n", mesh.points)
print("Cells:\n", mesh.cells)
print("Point Data:\n", mesh.point_data)
print("Cell Data:\n", mesh.cell_data)
print("Field Data:\n", mesh.field_data)
