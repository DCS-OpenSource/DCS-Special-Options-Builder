import Objects
import Skins
from Options.Options import Options

opts = Options("C:\\Users\\haydn\\Saved Games\\DCS\\Mods\\aircraft\\devAH1G\\Options") # Path to your options folder

headerX = 40
leftColumnX = 56
rightColumnX = 450

currentLineY = 60
lineSpacing = 30
sectionLineSpacing = 50
helpLineSpacing = 20

# Helper functions to manage line spacing
def newLine():
    global currentLineY
    currentLineY += lineSpacing
    return currentLineY

def newSection():
    global currentLineY
    currentLineY += sectionLineSpacing
    return currentLineY

def helpLine():
    global currentLineY
    currentLineY += helpLineSpacing
    return currentLineY



# Title
opts.add(
    Objects.Label(
        optionName="AH1G",
        x=leftColumnX,
        y=currentLineY,
        w=100,
        text="AH-1G Cobra",
        tooltip="",
        skin=Skins.StaticOptionsTitleSkin
    )
)


opts.build()