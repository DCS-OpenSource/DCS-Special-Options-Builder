from Options.Options import Options
from Objects import Checkbox, Label, Slider
from Skins import CheckBoxSkin, HelpSkin, StaticOptionsTitleSkin, HorzSliderSkinOptions

opts = Options("C:\\Users\\haydn\\Saved Games\\DCS\\Mods\\aircraft\\devAH1G\\Options")

leftColumnX = 56

opts.add(
    Label(
        optionName="AH1G",
        x=leftColumnX,
        y=60,
        w=100,
        text="AH-1G Cobra",
        tooltip="",
        skin=StaticOptionsTitleSkin
    )
)

opts.add(
    Checkbox(
        optionName="AH1GShowControls",
        x=leftColumnX,
        y=90,
        state=True,
        text="Show Controls Indicator by Default",
        tooltip="",
        skin=CheckBoxSkin
    )
)

opts.add(
    Label(
        optionName="AH1GShowControls",
        x=leftColumnX,
        y=110,
        text="When enabled, the controls indicator will be visible by default.",
        tooltip="",
        skin=HelpSkin
    )
)

opts.add(
    Slider(
        optionName = "SunvisorBrightness",
        x=leftColumnX,
        y=140,
        text="Sunvisor Brightness",
        max=255, min=0, step=5,
        skin=HorzSliderSkinOptions
    )
)

opts.add(
    Label(
        optionName="SunvisorBrightnessHelp",
        x=leftColumnX,
        y=160,
        text="Adjust Sunvisor Brightness, Smaller Numbers are lighter",
        tooltip="",
        skin=HelpSkin
    )
)

opts.build()