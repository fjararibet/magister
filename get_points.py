import vtk
import sys

filename = sys.argv[1]

# Read the VTP file
reader = vtk.vtkXMLPolyDataReader()
reader.SetFileName(filename)
reader.Update()

# Get the polydata
polydata = reader.GetOutput()

# Get and print vertex coordinates
points = polydata.GetPoints()
if points:
    for i in range(points.GetNumberOfPoints()):
        print(points.GetPoint(i))
else:
    print("No points found in the file.")

lines = polydata.GetLines()
if lines.GetNumberOfCells() > 0:
    print("Segments (lines) found:")
    id_list = vtk.vtkIdList()
    lines.InitTraversal()
    while lines.GetNextCell(id_list):
        for i in range(id_list.GetNumberOfIds() - 1):
            p1 = polydata.GetPoint(id_list.GetId(i))
            p2 = polydata.GetPoint(id_list.GetId(i + 1))
            print(f"Segment: {p1} -> {p2}")
else:
    print("No line segments found.")
