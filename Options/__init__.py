import os
import pkgutil
import importlib

# Get current package name (Objects / Skins)
package_name = __name__
package_path = os.path.dirname(__file__)

# Iterate through all modules in this folder
for _, module_name, is_pkg in pkgutil.iter_modules([package_path]):
    if is_pkg:
        continue

    # Skip this file
    if module_name == "__init__":
        continue

    # Import module
    module = importlib.import_module(f"{package_name}.{module_name}")

    # Inject everything into package namespace (like `from x import *`)
    for attr in dir(module):
        if not attr.startswith("_"):
            globals()[attr] = getattr(module, attr)