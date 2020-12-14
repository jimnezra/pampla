from paraview.simple import *
import os

mypath = "/home/jimnezra/ALMA/lamspy/Alex_parametric_02" + "/fri_test/output/"
onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
onlyvtkfiles = [f for f in onlyfiles if "vtk" in f]

# # create a new 'Legacy VTK Reader'
# vtk = LegacyVTKReader(FileNames=[mypath + onlyvtkfiles[1]])

for f in onlyvtkfiles:
    ### Opening vtk file
    vtk = LegacyVTKReader(FileNames=[mypath + f])
    
    #### disable automatic camera reset on 'Show'
    paraview.simple._DisableFirstRenderCameraReset()

    # # create a new 'Legacy VTK Reader'
    # vtk = LegacyVTKReader(FileNames=['/home/jimnezra/ALMA/lamspy/Alex_parametric_02/fri_027/output/eng_1-1_1-1.vtk'])

    # get active view
    renderView1 = GetActiveViewOrCreate('RenderView')
    # uncomment following to set a specific view size
    # renderView1.ViewSize = [1220, 463]

    # get layout
    layout1 = GetLayout()

    # show data in view
    vtkDisplay = Show(vtk, renderView1, 'GeometryRepresentation')

    # get color transfer function/color map for 'cell_scalars'
    cell_scalarsLUT = GetColorTransferFunction('cell_scalars')
    cell_scalarsLUT.RGBPoints = [1.0, 0.231373, 0.298039, 0.752941, 1.0001220703125, 0.865003, 0.865003, 0.865003, 1.000244140625, 0.705882, 0.0156863, 0.14902]
    cell_scalarsLUT.ScalarRangeInitialized = 1.0

    # trace defaults for the display properties.
    vtkDisplay.Representation = 'Surface'
    vtkDisplay.ColorArrayName = ['CELLS', 'cell_scalars']
    vtkDisplay.LookupTable = cell_scalarsLUT
    vtkDisplay.OSPRayScaleArray = 'Displacement'
    vtkDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
    vtkDisplay.SelectOrientationVectors = 'Displacement'
    vtkDisplay.ScaleFactor = 144.0
    vtkDisplay.SelectScaleArray = 'cell_scalars'
    vtkDisplay.GlyphType = 'Arrow'
    vtkDisplay.GlyphTableIndexArray = 'cell_scalars'
    vtkDisplay.GaussianRadius = 7.2
    vtkDisplay.SetScaleArray = ['POINTS', 'Displacement']
    vtkDisplay.ScaleTransferFunction = 'PiecewiseFunction'
    vtkDisplay.OpacityArray = ['POINTS', 'Displacement']
    vtkDisplay.OpacityTransferFunction = 'PiecewiseFunction'
    vtkDisplay.DataAxesGrid = 'GridAxesRepresentation'
    vtkDisplay.PolarAxes = 'PolarAxesRepresentation'

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    vtkDisplay.ScaleTransferFunction.Points = [-7.769074983343671e-08, 0.0, 0.5, 0.0, 0.042742181569337845, 1.0, 0.5, 0.0]

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    vtkDisplay.OpacityTransferFunction.Points = [-7.769074983343671e-08, 0.0, 0.5, 0.0, 0.042742181569337845, 1.0, 0.5, 0.0]

    # reset view to fit data
    renderView1.ResetCamera()

    #changing interaction mode based on data extents
    renderView1.InteractionMode = '2D'
    renderView1.CameraPosition = [720.0, 720.0, 10000.0]
    renderView1.CameraFocalPoint = [720.0, 720.0, 0.0]

    # get the material library
    materialLibrary1 = GetMaterialLibrary()

    # show color bar/color legend
    vtkDisplay.SetScalarBarVisibility(renderView1, True)

    # update the view to ensure updated data information
    renderView1.Update()

    # get opacity transfer function/opacity map for 'cell_scalars'
    cell_scalarsPWF = GetOpacityTransferFunction('cell_scalars')
    cell_scalarsPWF.Points = [1.0, 0.0, 0.5, 0.0, 1.000244140625, 1.0, 0.5, 0.0]
    cell_scalarsPWF.ScalarRangeInitialized = 1

    # create a new 'Warp By Vector'
    warpByVector1 = WarpByVector(Input=vtk)
    warpByVector1.Vectors = ['POINTS', 'Displacement']

    # show data in view
    warpByVector1Display = Show(warpByVector1, renderView1, 'GeometryRepresentation')

    # trace defaults for the display properties.
    warpByVector1Display.Representation = 'Surface'
    warpByVector1Display.ColorArrayName = ['CELLS', 'cell_scalars']
    warpByVector1Display.LookupTable = cell_scalarsLUT
    warpByVector1Display.OSPRayScaleArray = 'Displacement'
    warpByVector1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    warpByVector1Display.SelectOrientationVectors = 'Displacement'
    warpByVector1Display.ScaleFactor = 144.0042724609375
    warpByVector1Display.SelectScaleArray = 'cell_scalars'
    warpByVector1Display.GlyphType = 'Arrow'
    warpByVector1Display.GlyphTableIndexArray = 'cell_scalars'
    warpByVector1Display.GaussianRadius = 7.200213623046875
    warpByVector1Display.SetScaleArray = ['POINTS', 'Displacement']
    warpByVector1Display.ScaleTransferFunction = 'PiecewiseFunction'
    warpByVector1Display.OpacityArray = ['POINTS', 'Displacement']
    warpByVector1Display.OpacityTransferFunction = 'PiecewiseFunction'
    warpByVector1Display.DataAxesGrid = 'GridAxesRepresentation'
    warpByVector1Display.PolarAxes = 'PolarAxesRepresentation'

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    warpByVector1Display.ScaleTransferFunction.Points = [-7.769074983343671e-08, 0.0, 0.5, 0.0, 0.042742181569337845, 1.0, 0.5, 0.0]

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    warpByVector1Display.OpacityTransferFunction.Points = [-7.769074983343671e-08, 0.0, 0.5, 0.0, 0.042742181569337845, 1.0, 0.5, 0.0]

    # hide data in view
    Hide(vtk, renderView1)

    # show color bar/color legend
    warpByVector1Display.SetScalarBarVisibility(renderView1, True)

    # update the view to ensure updated data information
    renderView1.Update()

    # change representation type
    warpByVector1Display.SetRepresentationType('Surface With Edges')

    # Properties modified on warpByVector1Display
    warpByVector1Display.EdgeColor = [0.0, 0.0, 0.0]

    LoadPalette(paletteName='WhiteBackground')

    # Hide orientation axes
    renderView1.OrientationAxesVisibility = 0

    # hide color bar/color legend
    warpByVector1Display.SetScalarBarVisibility(renderView1, False)

    # Properties modified on warpByVector1
    source = GetActiveSource()
    x = max(source.PointData.GetArray('Displacement').GetRange())
    # y = source.PointData.GetArray()
    # print(y)
    if x < 0.01:
        warpByVector1.ScaleFactor = x * 6000000
    elif 0.01 <= x and x < 0.1:
        warpByVector1.ScaleFactor = x * 60000
    else:
        warpByVector1.ScaleFactor = x * 10000
    # warpByVector1.ScaleFactor = y/100.0/x

    # update the view to ensure updated data information
    renderView1.Update()

    # reset view to fit data
    renderView1.ResetCamera()

    # current camera placement for renderView1
    if "1-1.vtk" in f:
        renderView1.InteractionMode = '2D'
        renderView1.CameraPosition = [741.3710937499998, 725.6964721679689, 4008.3318936541677]
        renderView1.CameraFocalPoint = [741.3710937499998, 725.6964721679689, 0.0]
        renderView1.CameraParallelScale = 857.3823414624383
    elif "1-2.vtk" in f:
        renderView1.InteractionMode = '2D'
        renderView1.CameraPosition = [720.4325561445802, 1440.1165771484375, 6221.592745328376]
        renderView1.CameraFocalPoint = [720.4325561445802, 1440.1165771484375, 0.0]
        renderView1.CameraParallelScale = 1610.2666933626608
    else:
        renderView1.InteractionMode = '2D'
        renderView1.CameraPosition = [729.2392578124918, 362.4145507812426, 3146.3315357276147]
        renderView1.CameraFocalPoint = [729.2392578124918, 362.4145507812426, 0.0]
        renderView1.CameraParallelScale = 814.3305236529689

    # save screenshot
    fpng = f.replace("vtk", "png")
    SaveScreenshot(mypath + fpng, renderView1, ImageResolution=[1220, 463])

    #### saving camera placements for all active views

    # current camera placement for renderView1
    renderView1.InteractionMode = '2D'
    renderView1.CameraPosition = [741.3710937499998, 725.6964721679689, 4008.3318936541677]
    renderView1.CameraFocalPoint = [741.3710937499998, 725.6964721679689, 0.0]
    renderView1.CameraParallelScale = 857.3823414624383

    ### Resetting the session
    ResetSession()

#     #### uncomment the following to render all views
#     # RenderAllViews()
#     # alternatively, if you want to write images, you can use SaveScreenshot(...).

    

