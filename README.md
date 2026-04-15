# DCS Special Options Builder

## Overview
This tool generates DCS special options files:
- `options.dlg` (UI layout)
- `optionsDb.lua` (logic + values)

It uses Python classes to define UI elements and automatically builds both files.

---

## Basic Usage

```python
import Objects
import Skins
from Options.Options import Options

opts = Options("C:/Saved Games/DCS/Mods/aircraft/devAH1G/Options")

opts.add(
    Objects.Checkbox(
        optionName="TEST_OPTION",
        x=56,
        y=100,
        text="Test Option"
    )
)

opts.build()
```

---

## Layout System

Several helper functions and variables are provided to manage rows and columns

```python
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
```

---

## Widgets

### Checkbox

```python
Checkbox(
    optionName="OPTION_NAME",
    x=56,
    y=100,
    state=True,
    text="Label text",
    tooltip="Tooltip text",
    skin=CheckBoxSkin,
    depends_on="OTHER_OPTION",
    callback=True # if this checkbox should disable other options (link depends_on in other widgets to the name of this widget)
)
```

Generates:
- UI checkbox
- DB entry: `:checkbox()`
- Optional callback + dependency logic

---

### Label

```python
Objects.Label(
    optionName="LABEL_NAME",
    x=56,
    y=120,
    text="Display text",
    tooltip="",
    skin=Skins.HelpSkin
)
```

Notes:
- UI only
- No DB entry

---

### Slider

```python
Objects.Slider(
    optionName="SLIDER_NAME",
    x=56,
    y=140,
    min=0,
    max=255,
    step=5,
    default=20,
    text="Slider label",
    skin=Skins.HorzSliderSkinOptions,
    depends_on="OPTION_NAME" # Match the name of callback=True widget so its disabled
)
```

Generates:
- UI slider
- DB entry: `:slider(DbOption.Range(min, max))`

---

### Widget

```python
Objects.Widget(
    optionName = "SLIDER_NAME", # Widget Name needs to match slider to show slider value
    x=100,
    y=140,
    w=50,
    text="0",
    skin=Skins.StaticOptionsSliderValueSkin
)
```

Generates:
- UI widget that displays slider value

---

### EditBox

```python
Objects.EditBox(
    optionName="PORT",
    x=56,
    y=160,
    default=25389,
    tooltip="Port number",
    numeric=True,
    skin=Skins.EditBoxSkinME,
    depends_on="OPTION_NAME"  # Match the name of callback=True widget so its disabled
)
```

Generates:
- UI edit box
- DB entry: `:editbox()`

---

## Skins

Skins are defined as classes:

```python
class CheckBoxSkin:
    name = "CheckBoxSkin"

    def __str__(self):
        return '''local CheckBoxSkin = {
    ["params"] = {
        ["name"] = "checkBoxSkin_options",
    },
}'''
```

Use in widgets:
```python
skin=Skins.CheckBoxSkin
```

---

## Dependencies

Disable widgets based on another checkbox:

```python
Checkbox("MASTER", ..., callback=True)

Checkbox(
    "CHILD",
    ...,
    depends_on="MASTER"
)
```

Generates:
```lua
config.CHILDCheckbox:setEnabled(not config.MASTERCheckbox:getState())
```

---

## Output Files

### options.dlg
- UI layout
- Skins + widgets

### optionsDb.lua
- Option definitions
- Callbacks
- Update logic

---

## Notes

- `optionName` must be unique
- UI names automatically append:
  - Checkbox → `Checkbox`
  - Slider → `Slider`
  - EditBox → `EditBox`
- DB keys use raw `optionName`

---

## Recommended Workflow

1. Define layout
2. Add widgets
3. Use dependencies where needed
4. Call `opts.build()`
5. Run `main.py`
6. Restart DCS

---
