class Editbox:
    def __init__(
        self,
        optionName: str,
        x,
        y: int,
        w: int = 100,
        h: int = 20,
        default: int = 0,
        tooltip: str = "",
        password: bool = False,
        multiline: bool = False,
        numeric: bool = True,
        acceptDecimalPoint: bool = False,
        textWrapping: bool = False,
        readOnly: bool = False,
        skin=None,
    ):
        self.base_name = optionName
        self.name = f"{optionName}EditBox"

        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.default = default
        self.tooltip = tooltip

        self.password = str(password).lower()
        self.multiline = str(multiline).lower()
        self.numeric = str(numeric).lower()
        self.acceptDecimalPoint = str(acceptDecimalPoint).lower()
        self.textWrapping = str(textWrapping).lower()
        self.readOnly = str(readOnly).lower()

        self.skin = skin

    def _format_value(self, value):
        if isinstance(value, str) and not value.startswith('"'):
            return value
        return value

    def __str__(self):
        x_val = self._format_value(self.x)

        if self.skin:
            skin_block = self.skin.name
        else:
            skin_block = """{
\t\t\t\t\t["params"] = {
\t\t\t\t\t\t["name"] = "editBoxSkin1",
\t\t\t\t\t},
\t\t\t\t}"""

        return f"""\t\t\t\t["{self.name}"] = {{
\t\t\t\t\t["params"] = {{
\t\t\t\t\t\t["bounds"] = {{
\t\t\t\t\t\t\t["h"] = {self.h},
\t\t\t\t\t\t\t["w"] = {self.w},
\t\t\t\t\t\t\t["x"] = {x_val},
\t\t\t\t\t\t\t["y"] = {self.y},
\t\t\t\t\t\t}},
\t\t\t\t\t\t["enabled"] = true,
\t\t\t\t\t\t["password"] = {self.password},
\t\t\t\t\t\t["multiline"] = {self.multiline},
\t\t\t\t\t\t["numeric"] = {self.numeric},
\t\t\t\t\t\t["acceptDecimalPoint"] = {self.acceptDecimalPoint},
\t\t\t\t\t\t["textWrapping"] = {self.textWrapping},
\t\t\t\t\t\t["readOnly"] = {self.readOnly},
\t\t\t\t\t\t["text"] = "",
\t\t\t\t\t\t["tooltip"] = "{self.tooltip}",
\t\t\t\t\t\t["visible"] = true,
\t\t\t\t\t\t["zindex"] = 1,
\t\t\t\t\t}},
\t\t\t\t\t["skin"] = {skin_block},
\t\t\t\t\t["type"] = "EditBox",
\t\t\t\t}},
"""

    def to_db(self):
        return f'\t{self.base_name}\t= DbOption.new():setValue({self.default}):editbox(),'