# DCS Special Options Builder

## Overview
This tool generates DCS special options files:
- `options.dlg` (UI layout)
- `optionsDb.lua` (logic + values)

It uses Python classes to define UI elements and automatically builds both files.

---

## Basic Usage

```python
from Options.Options import Options
from Objects import Checkbox, Label, Slider, EditBox
from Skins import *

opts = Options("C:/Saved Games/DCS/Mods/aircraft/devAH1G/Options")

opts.add(
    Checkbox(
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

Use a layout helper to manage Y positioning:

```python
layout = Layout(startY=60)

y = layout.newLine()
y = layout.newSection()
y = layout.helpLine()
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
    callback=True
)
```

Generates:
- UI checkbox
- DB entry: `:checkbox()`
- Optional callback + dependency logic

---

### Label

```python
Label(
    optionName="LABEL_NAME",
    x=56,
    y=120,
    text="Display text",
    tooltip="",
    skin=HelpSkin
)
```

Notes:
- UI only
- No DB entry

---

### Slider

```python
Slider(
    optionName="SLIDER_NAME",
    x=56,
    y=140,
    min=0,
    max=255,
    step=5,
    default=20,
    text="Slider label",
    skin=HorzSliderSkinOptions,
    depends_on="OPTION_NAME"
)
```

Generates:
- UI slider
- DB entry: `:slider(DbOption.Range(min, max))`

---

### EditBox

```python
EditBox(
    optionName="PORT",
    x=56,
    y=160,
    default=25389,
    tooltip="Port number",
    numeric=True,
    skin=None,
    depends_on="OPTION_NAME"
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
skin=CheckBoxSkin
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
5. Reload DCS

---

## Future Extensions

- Multi-condition dependencies
- Auto layout columns
- Localization helpers
