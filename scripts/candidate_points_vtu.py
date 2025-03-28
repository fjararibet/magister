import meshio
import sys


# Read the .vtu file
mesh = meshio.read(sys.argv[1])

# Extract information
right_most = mesh.points[0]
left_most = mesh.points[0]
bottom_most = mesh.points[0]
for p in mesh.points:
    x = p[0]
    y = p[1]
    if y < bottom_most[1]:
        bottom_most = p
    if y < left_most[1]:
        left_most = p
    if y - left_most[1] < 0.01:
        if x < left_most[0]:
            left_most = p
    if y < right_most[1]:
        right_most = p
    if y - right_most[1] < 0.01:
        if x > right_most[0]:
            right_most = p
print(f"{bottom_most=}")
print(f"{left_most=}")
print("left most 2 = ", min(mesh.points, key=lambda p: (p[1], p[0])))
print(f"{right_most=}")
print("right most 2 = ", min(mesh.points, key=lambda p: (p[1], -p[0])))
