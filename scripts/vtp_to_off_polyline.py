import vtk
import numpy as np
from scipy.spatial import KDTree
import sys


def read_vtp_points(vtp_file):
    reader = vtk.vtkXMLPolyDataReader()
    reader.SetFileName(vtp_file)
    reader.Update()
    polydata = reader.GetOutput()
    points = polydata.GetPoints()

    return np.array([points.GetPoint(i) for i in range(points.GetNumberOfPoints())])


def compute_edges(points, k=2):
    tree = KDTree(points)
    edges = set()

    for i, point in enumerate(points):
        _, neighbors = tree.query(point, k=k+1)  # k+1 because first neighbor is the point itself
        for j in neighbors[1:]:  # Skip the first one (self)
            edge = tuple(sorted([i, j]))
            edges.add(edge)

    return list(edges)


def print_off_file(points, edges):
    print("OFF")
    print(f"{len(points)} 0 {len(edges)}")

    for point in points:
        print(" ".join(map(str, point)) + "")

    for edge in edges:
        print(f"2 {edge[0]} {edge[1]}")


if __name__ == "__main__":
    vtp_file = sys.argv[1]

    points = read_vtp_points(vtp_file)
    edges = compute_edges(points, k=2)
    print_off_file(points, edges)
