class Slider:
    def __init__(
        self,
        optionName: str,
        x: int,
        y: int,
        w: int = 300,
        h: int = 18,
        max: int = 100,
        min: int = 0,
        step: int = 1,
        text: str = "",
        tooltip: str = "",
        skin=None,
    ):
        self.name = f"{optionName}Slider"
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.max = max
        self.min = min
        self.step = step
        self.text = text
        self.tooltip = tooltip

        # Default skin fallback
        self.skin = skin

    def __str__(self):
        skin_name = self.skin.name if self.skin else "horzSliderSkin_options"

        return f"""
\t\t\t\t["{self.name}"] = {{
\t\t\t\t\t["params"] = {{
\t\t\t\t\t\t["bounds"] = {{
\t\t\t\t\t\t\t["h"] = {self.h},
\t\t\t\t\t\t\t["w"] = {self.w},
\t\t\t\t\t\t\t["x"] = {self.x},
\t\t\t\t\t\t\t["y"] = {self.y},
\t\t\t\t\t\t}},
\t\t\t\t\t\t["pagestep"] = 10,
\t\t\t\t\t\t["range"] = {{
\t\t\t\t\t\t\t["max"] = {self.max},
\t\t\t\t\t\t\t["min"] = {self.min},
\t\t\t\t\t\t}},
\t\t\t\t\t\t["step"] = {self.step},
\t\t\t\t\t\t["enabled"] = true,
\t\t\t\t\t\t["tabOrder"] = 0,
\t\t\t\t\t\t["text"] = "{self.text}",
\t\t\t\t\t\t["tooltip"] = "{self.tooltip}",
\t\t\t\t\t\t["visible"] = true,
\t\t\t\t\t\t["zindex"] = 0,
\t\t\t\t\t}},
\t\t\t\t\t["skin"] = {skin_name},
\t\t\t\t\t["type"] = "HorzSlider",
\t\t\t\t}},
"""
