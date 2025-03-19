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

    print("OFF")
    # Write header: <# of vertices> <# of faces> <# of edges>
    print(f"{num_points} 0 0")

    # Write points
    for i in range(num_points):
        x, y, z = points.GetPoint(i)
        print(f"{x} {y} {z}")


if __name__ == "__main__":
    input_file = sys.argv[1]
    vtp_to_poly(input_file)
