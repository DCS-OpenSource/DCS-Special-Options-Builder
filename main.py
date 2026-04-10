import Objects
import Skins
from Options.Options import Options

opts = Options("C:\\Users\\haydn\\Saved Games\\DCS\\Mods\\aircraft\\devAH1G\\Options")

headerX = 40
leftColumnX = 56

currentLineY = 60
lineSpacing = 30
sectionLineSpacing = 50
helpLineSpacing = 20

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

#region Pilot Head Accessory Options
opts.add(
    Objects.Label(
        optionName="PilotHeadAccessoryOptions",
        x=headerX,
        y=newSection(),
        w=200,
        text="Pilot Head Accessory Options",
        tooltip="",
        skin=Skins.StaticOptionsCaptionSkin
    )
)

opts.add(
    Objects.Label(
        optionName="SunvisorBrightness",
        x=leftColumnX,
        y=newLine(),
        text="Sunvisor Brightness:",
        tooltip="",
        skin=Skins.StaticOptionsCaptionSkin
    )
)

opts.add(
    Objects.Slider(
        optionName = "SunvisorBrightness",
        x=leftColumnX + 120,
        y=currentLineY,
        w=200,
        text="",
        max=255, min=0, step=5,
        skin=Skins.HorzSliderSkinOptions
    )
)

opts.add(
    Objects.Widget(
        optionName = "SunvisorBrightness",
        x=leftColumnX + 290,
        y=currentLineY,
        w=50,
        text="0",
        skin=Skins.StaticOptionsSliderValueSkin
    )
)

opts.add(
    Objects.Label(
        optionName="SunvisorBrightnessHelp",
        x=leftColumnX,
        y=helpLine(),
        text="Adjust Sunvisor Brightness, Smaller Numbers are lighter",
        tooltip="",
        skin=Skins.HelpSkin
    )
)
#endregion

#region General Options
opts.add(
    Objects.Label(
        optionName="GeneralOptions",
        x=headerX,
        y=newLine(),
        w=100,
        text="General Options",
        tooltip="",
        skin=Skins.StaticOptionsCaptionSkin
    )
)

opts.add(
    Objects.Checkbox(
        optionName="AH1GShowControls",
        x=leftColumnX,
        y=newLine(),
        state=True,
        text="Show Controls Indicator by Default",
        tooltip="When enabled, the controls indicator will be visible by default.",
        skin=Skins.CheckBoxSkin
    )
)
#endregion



opts.build()