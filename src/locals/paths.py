from os import path

TOP_LEVEL_DIR = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))
SHADERS_DIR = path.join(TOP_LEVEL_DIR, "shaders")
ASSETS_DIR = path.join(TOP_LEVEL_DIR, "assets")

print("Top level:", TOP_LEVEL_DIR)
print("Assets :", ASSETS_DIR)
print("Shaders:", SHADERS_DIR)
