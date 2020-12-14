# pampla
Parametric analysis of masonry panels using a limit analysis approach

This repository has a python package called "Sapienza" and two python files:

1. 001_masonry_panels.py
2. open_vtk.py

001_masonry_panels can be used to generate the geometry of all the tested masonry panels. It uses the functions defined in the masonry_panels module 
within the Sapienza package. It requires that the user specifies brick lenght, brick height, number of horizontal bricks and number of vertical bricks.
The script generates the polylines in Autocad. 

open_vtk.py is an script used to generate .png files with the collapse mechanism of every masonry panel. The script opens the .vtk file generated 
with ALMA 2.0, interacts with paraview and creates a .png file.
