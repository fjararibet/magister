import vtk
import sys


def vtp_to_poly(vtp_filename):
    # Read the VTP file
    reader = vtk.vtkXMLPolyDataReader()
    reader.SetFileName(vtp_filename)
    reader.Update()

    poly_data = reader.GetOutput()
    points = poly_data.GetPoints()

    num_points = points.GetNumberOfPoints()

    # Write header: <# of points> <dimension> <# of attributes> <# of boundary markers>
    print(f"{num_points} 3 0 0")

    # Write points
    for i in range(num_points):
        x, y, z = points.GetPoint(i)
        print(f"{i + 1} {x} {y} {z}")

    # Write zero edges (since it's just a point cloud)
    print("0")

    # Write zero holes (optional)
    print("0")

    # Write zero regions (optional)
    print("0")


if __name__ == "__main__":
    input_file = sys.argv[1]
    vtp_to_poly(input_file)
