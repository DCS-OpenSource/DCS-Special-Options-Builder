from Options.Options import Options
from Objects import Checkbox
from Skins import CheckBoxSkin

opts = Options("C:\\Users\\haydn\\Saved Games\\DCS\\Mods\\aircraft\\devAH1G\\Options")

opts.add(
    Checkbox(
        optionName="AH1GShowControls",
        x=56,
        y=90,
        state=True,
        text="Show Controls Indicator by Default",
        tooltip="",
        skin=CheckBoxSkin
    )
)

opts.build()