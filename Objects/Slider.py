class Slider:
    def __init__(
        self,
        optionName: str,
        x,
        y: int,
        w: int = 300,
        h: int = 18,
        min: int = 0,
        max: int = 100,
        step: int = 1,
        default: int = 0,
        text: str = "",
        tooltip: str = "",
        skin=None,
        depends_on: str = None,
        callback: bool = False,
    ):
        self.base_name = optionName
        self.name = f"{optionName}Slider"

        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.min = min
        self.max = max
        self.step = step
        self.default = default

        self.text = text
        self.tooltip = tooltip

        self.skin = skin

        self.depends_on = depends_on
        self.callback = callback

    def _format_value(self, value):
        if isinstance(value, str) and not value.startswith('"'):
            return value
        return value

    def __str__(self):
        x_val = self._format_value(self.x)
        skin_name = self.skin.name if self.skin else "HorzSliderSkinOptions"

        return f"""
\t\t\t\t["{self.name}"] = {{
\t\t\t\t\t["params"] = {{
\t\t\t\t\t\t["bounds"] = {{
\t\t\t\t\t\t\t["h"] = {self.h},
\t\t\t\t\t\t\t["w"] = {self.w},
\t\t\t\t\t\t\t["x"] = {x_val},
\t\t\t\t\t\t\t["y"] = {self.y},
\t\t\t\t\t\t}},
\t\t\t\t\t\t["enabled"] = true,
\t\t\t\t\t\t["min"] = {self.min},
\t\t\t\t\t\t["max"] = {self.max},
\t\t\t\t\t\t["step"] = {self.step},
\t\t\t\t\t\t["text"] = "{self.text}",
\t\t\t\t\t\t["tooltip"] = "{self.tooltip}",
\t\t\t\t\t\t["visible"] = true,
\t\t\t\t\t\t["zindex"] = 1,
\t\t\t\t\t}},
\t\t\t\t\t["skin"] = {skin_name},
\t\t\t\t\t["type"] = "HorzSlider",
\t\t\t\t}},
"""

    def to_db(self):
        base = (
            f'{self.base_name}\t= DbOption.new():setValue({self.default})'
            f':slider(DbOption.Range({self.min}, {self.max}))'
        )

        if self.callback:
            base += ':callback(function(v) Update() end)'

        return "\t" + base + ","