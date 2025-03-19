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


def write_poly_file(points, edges):
    # num_vertices, dimension, num_attributes, num_boundary_markers
    print(f"{len(points)} 2 0 0")

    for i, point in enumerate(points):
        print(f"{i+1} {point[0]} {point[1]}")

    print(f"{len(edges)} 0")  # num_segments, num_boundary_markers

    for i, edge in enumerate(edges):
        print(f"{i+1} {edge[0]+1} {edge[1]+1}")

    print("0")  # Number of holes
    print("0")  # Number of regions


if __name__ == "__main__":
    vtp_file = sys.argv[1]

    points = read_vtp_points(vtp_file)
    edges = compute_edges(points, k=2)
    write_poly_file(points, edges)
