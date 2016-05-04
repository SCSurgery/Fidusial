# -*- coding: UTF-8 -*-
from __main__ import vtk, qt, ctk, slicer
import math
import os
import numpy
import pickle
import json

#
# Load Files
#
class Fidusial():
  def __init__(self, parent):
    parent.title = "Tarea 3"
    parent.categories = ["Tareas"]
    parent.dependencies = []
    parent.contributors = ["Camilo Quiceno Q y Nicolas Buitrago Roldan"] # replace with "Firstname Lastname (Org)"
    parent.helpText = """
    Aprender a manipular fiducial
    """
    parent.acknowledgementText = """
    Desarrollado por Camilo Quiceno Y Nicolas Buitrago
    """ # replace with organization, grant and thanks.
    self.parent = parent


class FidusialWidget:
  def __init__(self, parent = None):
    if not parent:
      self.parent = slicer.qMRMLWidget()
      self.parent.setLayout(qt.QVBoxLayout())
      self.parent.setMRMLScene(slicer.mrmlScene)
    else:
      self.parent = parent
      self.layout = self.parent.layout()
    if not parent:
      self.setup()
      self.parent.show()

  def setup(self):
	sampleCollapsibleButton = ctk.ctkCollapsibleButton() #Se crea boton colapsable
	sampleCollapsibleButton.text = "Marcadores (Click derecho para dejar de insertar)" #Se asigna label del boton colapsable
	sampleCollapsibleButton.collapsed = False #Aparecen sin colapsar
	self.layout.addWidget(sampleCollapsibleButton) #Se crea layout dentro del boton colapsable

	sampleFormLayout = qt.QFormLayout(sampleCollapsibleButton)

	layout1Button = qt.QPushButton("Agregar Marcador") #Se crea boton pulsable, con texto "Apply"
	layout1Button.toolTip = "Al presionar puede insertar un marcador en la escena, click derecho para dejar de insertar" #Información que aparece si dejas el mouse encima
	sampleFormLayout.addWidget(layout1Button) #Se añade el boton al layout del boton colapsable
	layout1Button.connect('clicked(bool)',self.onApply)

	layout2Button = qt.QPushButton("Crear Regla") #Se crea boton pulsable, con texto "Apply"
	layout2Button.toolTip = "Al presionar  puede insertar una regla en la escena, click derecho para dejar de insertar" #Información que aparece si dejas el mouse encima
	sampleFormLayout.addWidget(layout2Button) #Se añade el boton al layout del boton colapsable
	layout2Button.connect('clicked(bool)',self.onApply2)

	layout3Button = qt.QPushButton("Crear Region ROI") #Se crea boton pulsable, con texto "Apply"
	layout3Button.toolTip = "Al presionar no puede insertar una region ROI en la escena, click derecho para dejar de insertar" #Información que aparece si dejas el mouse encima
	sampleFormLayout.addWidget(layout3Button) #Se añade el boton al layout del boton colapsable
	layout3Button.connect('clicked(bool)',self.onApply3)


  def onApply(self):
  	print "Crear Marcador"
	placeModePersistence = 1
	slicer.modules.markups.logic().StartPlaceMode(placeModePersistence)#se crea marcador por medio de un click con el mouse
  
  def onApply2(self):
  	print "Crear regla"
	selectionNode = slicer.mrmlScene.GetNodeByID("vtkMRMLSelectionNodeSingleton")
	 # place rulers
	selectionNode.SetReferenceActivePlaceNodeClassName("vtkMRMLAnnotationRulerNode")
	 # to place ROIs use the class name vtkMRMLAnnotationROINode
	interactionNode = slicer.mrmlScene.GetNodeByID("vtkMRMLInteractionNodeSingleton")
	placeModePersistence = 1
	interactionNode.SetPlaceModePersistence(placeModePersistence)
	 # mode 1 is Place, can also be accessed via slicer.vtkMRMLInteractionNode().Place
	interactionNode.SetCurrentInteractionMode(1)

  def onApply3(self):
  	print "Crear ROI"
	selectionNode = slicer.mrmlScene.GetNodeByID("vtkMRMLSelectionNodeSingleton")
	 # place rulers
	selectionNode.SetReferenceActivePlaceNodeClassName("vtkMRMLAnnotationROINode")
	 # to place ROIs use the class name vtkMRMLAnnotationROINode
	interactionNode = slicer.mrmlScene.GetNodeByID("vtkMRMLInteractionNodeSingleton")
	placeModePersistence = 1
	interactionNode.SetPlaceModePersistence(placeModePersistence)
	 # mode 1 is Place, can also be accessed via slicer.vtkMRMLInteractionNode().Place
	interactionNode.SetCurrentInteractionMode(1)

    


