from Options.Options import Options
from Objects import Checkbox, Label
from Skins import CheckBoxSkin, HelpSkin, StaticOptionsTitleSkin

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

opts.build()