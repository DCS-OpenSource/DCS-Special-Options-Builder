import os


class Options:
    def __init__(self, path: str):
        if path.endswith(".dlg"):
            self.output_path = os.path.dirname(path)
            self.filename = os.path.basename(path)
        else:
            self.output_path = path
            self.filename = "options.dlg"

        os.makedirs(self.output_path, exist_ok=True)

        self.children = []
        self.skins = []
        self._skin_names = set()
        self.db_entries = []

        self.prefix = """dialog = {
\t["children"] = {
\t\t["containerPlugin"] = {
\t\t\t["children"] = {
"""

        self.suffix = """\t\t\t},
\t\t\t["params"] = {
\t\t\t\t["bounds"] = {
\t\t\t\t\t["h"] = 600,
\t\t\t\t\t["w"] = 974,
\t\t\t\t\t["x"] = 0,
\t\t\t\t\t["y"] = 0,
\t\t\t\t},
\t\t\t\t["enabled"] = true,
\t\t\t\t["text"] = "",
\t\t\t\t["tooltip"] = "",
\t\t\t\t["visible"] = true,
\t\t\t\t["zindex"] = 2,
\t\t\t},
\t\t\t["skin"] = {
\t\t\t\t["params"] = {
\t\t\t\t\t["name"] = "panelSkin",
\t\t\t\t},
\t\t\t},
\t\t\t["type"] = "Panel",
\t\t},
\t},
\t["params"] = {
\t\t["bounds"] = {
\t\t\t["h"] = 851,
\t\t\t["w"] = 1135,
\t\t\t["x"] = 0,
\t\t\t["y"] = 0,
\t\t},
\t\t["draggable"] = true,
\t\t["enabled"] = true,
\t\t["hasCursor"] = true,
\t\t["lockFlow"] = false,
\t\t["modal"] = false,
\t\t["offscreen"] = false,
\t\t["resizable"] = false,
\t\t["text"] = "New dialog",
\t\t["zOrder"] = 0,
\t},
\t["skin"] = {
\t\t["params"] = {
\t\t\t["name"] = "windowSkin",
\t\t},
\t},
\t["type"] = "Window",
}
"""

    def add(self, element):
        self.children.append(element)

        # Auto-register skin if element has one
        if hasattr(element, "skin") and element.skin:
            skin_class = element.skin
            if skin_class.name not in self._skin_names:
                self._skin_names.add(skin_class.name)
                self.skins.append(skin_class())

        if hasattr(element, "to_db"):
            self.db_entries.append(element.to_db())

    def build(self):
        content = ""

        # Write skins first
        for skin in self.skins:
            content += str(skin) + "\n"

        # Then dialog
        content += self.prefix

        for child in self.children:
            content += str(child)

        content += self.suffix

        dlg_path = os.path.join(self.output_path, self.filename)

        with open(dlg_path, "w", encoding="utf-8") as f:
            f.write(content)

        self.build_db()

    def build_db(self):
        content = """local DbOption  = require('Options.DbOption')
local i18n	    = require('i18n')

local _ = i18n.ptranslate

return {
"""

        for entry in self.db_entries:
            content += entry + "\n"

        content += "}\n"

        db_path = os.path.join(self.output_path, "optionsDb.lua")

        with open(db_path, "w", encoding="utf-8") as f:
            f.write(content)