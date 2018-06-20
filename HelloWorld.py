# Classic Hello World example

from win32com.client import Dispatch, GetActiveObject, GetObject

# Start up an Illustrator application
# app = Dispatch('Photoshop.Application')

# Or get Reference to already running Illustrator application instance
app = GetActiveObject("Illustrator.Application")

docRef = app.Documents.Add()
rectRef = docRef.PathItems.Rectangle(700, 50, 100, 100)
areaTextRef = docRef.TextFrames.AreaText(rectRef)
areaTextRef.Contents = "Hello World!"