# Visualize a cube using VTK
# This tutorial come from https://www.cb.uu.se/~aht/Vis2014/lecture2.pdf
# @luantm: But in that tutorial, the source code is old, I modified in line 15 cube_mapper.SetInputCOnnection( cube.GetOutputPort() )
from vtkmodules.vtkCommonCore import vtkVersion, vtkPoints
import vtk
print (vtkVersion.GetVTKVersion())
from vtkmodules.vtkRenderingAnnotation import vtkAxesActor
from vtkmodules.vtkInteractionWidgets import vtkCameraOrientationWidget
from vtkmodules.vtkRenderingCore import vtkActor, vtkPolyDataMapper, vtkRenderWindow, vtkRenderer, vtkRenderWindowInteractor
from vtkmodules.vtkCommonDataModel import (
    vtkCellArray,
    vtkPolyData,
    vtkTriangle
)
from read_shashini_file import read_data
import sys

input_filename = sys.argv[1]
data = read_data(input_filename)
max_value = 350
min_value = 0
if input_filename == 'winter.csv':
    threshold = 50
else:
    threshold = 150
# print(data[0])
# print(data[1])

def make_polygons_actor(p1, p2, p3, p4, color):
    # Create a triangle
    points = vtkPoints()
    points.InsertNextPoint(p1[0], p1[1], p1[2])
    points.InsertNextPoint(p2[0], p2[1], p2[2])
    points.InsertNextPoint(p3[0], p3[1], p3[2])
    points.InsertNextPoint(p4[0], p4[1], p4[2])

    triangle = vtkTriangle()
    triangle.GetPointIds().SetId(0, 0)
    triangle.GetPointIds().SetId(1, 1)
    triangle.GetPointIds().SetId(2, 2)

    triangle2 = vtkTriangle()
    triangle2.GetPointIds().SetId(0, 1)
    triangle2.GetPointIds().SetId(1, 2)
    triangle2.GetPointIds().SetId(2, 3)

    triangles = vtkCellArray()
    triangles.InsertNextCell(triangle)
    triangles.InsertNextCell(triangle2)

    # Create a polydata object
    trianglePolyData = vtkPolyData()

    # Add the geometry and topology to the polydata
    trianglePolyData.SetPoints(points)
    trianglePolyData.SetPolys(triangles)

    mapper = vtkPolyDataMapper()
    mapper.SetInputData(trianglePolyData)
    actor = vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor( color[0], color[1], color[2])
    return actor

axes = vtkAxesActor()




# Create a renderer and add actor to it
renderer = vtkRenderer()
renderer.SetBackground(0.0, 0.0, 0.0)



import math
from colour import Color
colors = list(  Color("red").range_to(Color("blue"), 100))
def get_color(number, min_value, max_value):
    try:
        index_f = (number - min_value) / (max_value - min_value)
        index = int(index_f * 100)

    
        color = colors[index]
        return ( color.get_red() , color.get_green() , color.get_blue())
    except:
        print('ERROR', number)
        return (0, 0, 0)

# def get_color_scale(number):
#     if number > 258 and number < 261:
#         return get_color(number, 258, 261)
#     else:
#         return (0, 0, 0)
#         return get_color(number, min_value, max_value)


for item in data:
    if item[0][1] > 0 and item[-1] > threshold:
        color = get_color(item[-1], min_value, max_value)
        # color = get_color_scale(item[4])
        poly = make_polygons_actor(
            item[0], # vertices 1
            item[2], # vertices 2
            item[6], # vertices 3
            item[8], # vertices 4
            (color[0], color[1], color[2]) # color
        )
        renderer.AddActor(poly)
    if item[0][1] < 0 and item[-1] < threshold:
        color = get_color(item[-1], min_value, max_value)
        # color = get_color_scale(item[4])
        poly = make_polygons_actor(
            item[0], # vertices 1
            item[2], # vertices 2
            item[6], # vertices 3
            item[8], # vertices 4
            (color[0], color[1], color[2]) # color
        )
        renderer.AddActor(poly)
    # if item[0][1] < 0: # or True and item[-1] < threshold:
    #     color = get_color(item[-1], min_value, max_value)
    #     # color = get_color_scale(item[4])
    #     poly = make_polygons_actor(
    #         item[0], # vertices 1
    #         item[1], # vertices 2
    #         item[2], # vertices 3
    #         item[3], # vertices 4
    #         (color[0], color[1], color[2]) # color
    #     )
    #     renderer.AddActor(poly)
# renderer.AddActor(axes)

# Create a render window
render_window = vtkRenderWindow()
render_window.SetWindowName(input_filename)
render_window.SetSize(400, 400)
render_window.AddRenderer(renderer)

# Create an interactor
interactor = vtkRenderWindowInteractor()
interactor.SetRenderWindow(render_window)

cam_orient_manipulator = vtkCameraOrientationWidget()
cam_orient_manipulator.SetParentRenderer(renderer)
# Enable the widget.
cam_orient_manipulator.On()

# init the interactor and start rendering loop
interactor.Initialize()
render_window.Render()
interactor.Start()
