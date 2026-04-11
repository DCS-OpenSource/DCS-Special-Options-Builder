class Checkbox:
    def __init__(
        self,
        optionName: str,
        x: int,
        y: int,
        w: int = 300,
        h: int = 18,
        state: bool = True,
        text: str = "",
        tooltip: str = "",
        skin=None,
    ):
        self.name = f"{optionName}Checkbox"
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.state = str(state).lower()
        self.text = text
        self.tooltip = tooltip

        # Default skin fallback
        self.skin = skin

    def to_db(self):
        return f'\t{self.name.replace("Checkbox", "")}\t= DbOption.new():setValue({self.state}):checkbox(),'

    def __str__(self):
        skin_name = self.skin.name if self.skin else "CheckBoxSkin"

        return f"""\t\t\t\t["{self.name}"] = {{
\t\t\t\t\t["params"] = {{
\t\t\t\t\t\t["bounds"] = {{
\t\t\t\t\t\t\t["h"] = {self.h},
\t\t\t\t\t\t\t["w"] = {self.w},
\t\t\t\t\t\t\t["x"] = {self.x},
\t\t\t\t\t\t\t["y"] = {self.y},
\t\t\t\t\t\t}},
\t\t\t\t\t\t["enabled"] = true,
\t\t\t\t\t\t["state"] = {self.state},
\t\t\t\t\t\t["tabOrder"] = 0,
\t\t\t\t\t\t["text"] = "{self.text}",
\t\t\t\t\t\t["tooltip"] = "{self.tooltip}",
\t\t\t\t\t\t["visible"] = true,
\t\t\t\t\t\t["zindex"] = 0,
\t\t\t\t\t}},
\t\t\t\t\t["skin"] = {skin_name},
\t\t\t\t\t["type"] = "CheckBox",
\t\t\t\t}},
"""