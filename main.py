import Objects
import Skins
from Options.Options import Options

opts = Options("C:\\Users\\username\\Saved Games\\DCS\\Mods\\aircraft\\planeName\\Options")

headerX = 40
leftColumnX = 56
rightColumnX = 450

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


#region General Options
opts.add(
    Objects.Label(
        optionName="GENERAL_OPTIONS",
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
        optionName="SHOW_CONTROLS",
        x=leftColumnX,
        y=newLine(),
        state=True,
        text="Show Controls Indicator by Default",
        tooltip="When enabled, the controls indicator will be visible by default.",
        skin=Skins.CheckBoxSkin
    )
)

opts.add(
    Objects.Checkbox(
        optionName="COCKPIT_SHAKE",
        x=rightColumnX,
        y=currentLineY,
        state=False,
        text="Disable Cockpit Shake (INOP - TODO)",
        tooltip="When enabled, the cockpit will not shake during flight.",
        skin=Skins.CheckBoxSkin
    )
)

opts.add(
    Objects.Checkbox(
        optionName="PLACEHOLDER",
        x=leftColumnX,
        y=newLine(),
        state=False,
        text="Placeholder Option (INOP - TODO)",
        tooltip="IDK What this should be, waiting for an idea",
        skin=Skins.CheckBoxSkin
    )
)


opts.add(
    Objects.Checkbox(
        optionName="FORCE_FEEDBACK",
        x=rightColumnX,
        y=currentLineY,
        state=False,
        text="Enable Force Feedback (INOP - TODO)",
        tooltip="When enabled, the joystick will provide force feedback during flight.",
        skin=Skins.CheckBoxSkin
    )
)

#endregion

#region AI Gunner
opts.add(
    Objects.Label(
        optionName="AI_GUNNER",
        x=headerX,
        y=newSection(),
        w=150,
        text="AI Gunner Options",
        tooltip="",
        skin=Skins.StaticOptionsCaptionSkin
    )
)

opts.add(
    Objects.Checkbox(
        optionName="DISABLE_AI_GUNNER",
        x=leftColumnX,
        y=newLine(),
        state=False,
        text="Disable AI Gunner",
        tooltip="When enabled, the AI gunner not be present.",
        skin=Skins.CheckBoxSkin,
        callback=True
    )
)

opts.add(
    Objects.Checkbox(
        optionName="MUTE_AI_GUNNER",
        x=rightColumnX,
        y=currentLineY,
        state=False,
        text="Mute AI Gunner",
        tooltip="When enabled, the AI gunner will be muted.",
        skin=Skins.CheckBoxSkin,
        depends_on="DISABLE_AI_GUNNER",
    )
)

opts.add(
    Objects.Checkbox(
        optionName="OVERRIDE_AI_GUNNER_COALITION_CHECKS",
        x=leftColumnX,
        y=newLine(),
        state=False,
        w=300,
        text="Allow AI Gunner to Target Friendly Units",
        tooltip="I made this for one guy who wanted to be able to shoot his own units with the AI gunner, because hes crazy like that <3",
        skin=Skins.CheckBoxSkin,
        depends_on="DISABLE_AI_GUNNER",
    )
)

#endregion

#region Accessory Options
opts.add(
    Objects.Label(
        optionName="ACCESSORY_OPTIONS_",
        x=headerX,
        y=newSection(),
        w=200,
        text="Accessory Options",
        tooltip="",
        skin=Skins.StaticOptionsCaptionSkin
    )
)

#region Sunvisor Tint

opts.add(
    Objects.Label(
        optionName="VISOR_TINT",
        x=leftColumnX,
        y=newLine(),
        text="Sunvisor Tint:",
        tooltip="",
        skin=Skins.StaticOptionsCaptionSkin
    )
)

opts.add(
    Objects.Label(
        optionName="VISOR_TINT_RED",
        x=leftColumnX + 100,
        y=currentLineY,
        text="R:",
        tooltip="",
        skin=Skins.StaticOptionsCaptionSkin
    )
)


opts.add(
    Objects.Editbox(
        optionName="VISOR_TINT_RED",
        x=leftColumnX + 120,
        y=currentLineY,
        w=50,
        default=3,
        numeric=True,
        tooltip="0-255 value for red tint in sunvisor",
        skin=Skins.EditBoxSkinME
    )
)

opts.add(
    Objects.Label(
        optionName="VISOR_TINT_GREEN",
        x=leftColumnX + 180,
        y=currentLineY,
        text="G:",
        tooltip="",
        skin=Skins.StaticOptionsCaptionSkin
    )
)


opts.add(
    Objects.Editbox(
        optionName="VISOR_TINT_GREEN",
        x=leftColumnX + 200,
        y=currentLineY,
        w=50,
        default=3,
        numeric=True,
        tooltip="0-255 value for green tint in sunvisor",
        skin=Skins.EditBoxSkinME
    )
)

opts.add(
    Objects.Label(
        optionName="VISOR_TINT_BLUE",
        x=leftColumnX + 260,
        y=currentLineY,
        text="B:",
        tooltip="",
        skin=Skins.StaticOptionsCaptionSkin
    )
)


opts.add(
    Objects.Editbox(
        optionName="VISOR_TINT_BLUE",
        x=leftColumnX + 280,
        y=currentLineY,
        w=50,
        default=3,
        numeric=True,
        tooltip="0-255 value for blue tint in sunvisor",
        skin=Skins.EditBoxSkinME
    )
)




#endregion

opts.add(
    Objects.Label(
        optionName="VISOR_BRIGHTNESS",
        x=leftColumnX,
        y=newLine(),
        text="Sunvisor Brightness:",
        tooltip="",
        skin=Skins.StaticOptionsCaptionSkin
    )
)

opts.add(
    Objects.Slider(
        optionName = "VISOR_BRIGHTNESS",
        x=leftColumnX + 120,
        y=currentLineY,
        w=200,
        default=15,
        max=255, min=0, step=5,
        skin=Skins.HorzSliderSkinOptions
    )
)

opts.add(
    Objects.Widget(
        optionName = "VISOR_BRIGHTNESS",
        x=leftColumnX + 290,
        y=currentLineY,
        w=50,
        text="0",
        skin=Skins.StaticOptionsSliderValueSkin
    )
)

opts.add(
    Objects.Label(
        optionName="VISOR_BRIGHTNESS_HELP",
        x=leftColumnX,
        y=helpLine(),
        text="Adjust Sunvisor Brightness, Smaller Numbers are lighter",
        tooltip="",
        skin=Skins.HelpSkin
    )
)


#endregion

#region Advanced Options
opts.add(
    Objects.Label(
        optionName="ADVANCED_OPTIONS",
        x=headerX,
        y=newSection(),
        w=200,
        text="Advanced Options",
        tooltip="",
        skin=Skins.StaticOptionsCaptionSkin
    )
)

opts.add(
    Objects.Label(
        optionName="ADVANCED_OPTIONS_HELP_1",
        x=leftColumnX,
        y=helpLine(),
        w=800,
        text="The options in this section are for advanced users only. Changing these options may cause issues with the mod if you do not know what you are doing.",
        tooltip="",
        skin=Skins.HelpSkin
    )
)

opts.add(
    Objects.Label(
        optionName="ADVANCED_OPTIONS_HELP_2",
        x=leftColumnX,
        y=helpLine(),
        w=800,
        text="For more information on these options, see the manual.",
        tooltip="",
        skin=Skins.HelpSkin
    )
)

#region Dynamic Port Number

opts.add(
    Objects.Label(
        optionName="MULTICREW_PORT",
        x=leftColumnX,
        y=newLine(),
        text="Multicrew Port:",
        tooltip="",
        skin=Skins.StaticOptionsCaptionSkin
    )
)

opts.add(
    Objects.Editbox(
        optionName="MULTICREW_PORT",
        x=leftColumnX + 100,
        y=currentLineY,
        default=25389,
        numeric=True,
        tooltip="Customize Port Number for multicrew",
        skin=Skins.EditBoxSkinME
    )
)

opts.add(
    Objects.Label(
        optionName="MULTICREW_PORT_HELP",
        x=leftColumnX,
        y=helpLine(),
        text="Change the multicrew port number if you have conflicts with other mods or software. Default is 25389.",
        tooltip="",
        skin=Skins.HelpSkin
    )
)

#endregion

#endregion


opts.build()
