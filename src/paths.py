from pathlib import Path

TOP_LEVEL_DIR = Path(__file__).parent.parent
SHADERS_DIR = TOP_LEVEL_DIR / "src" / "render" / "shaders"
ASSETS_DIR = TOP_LEVEL_DIR / "assets"

print("Top level:", TOP_LEVEL_DIR)
print("Assets :", ASSETS_DIR)
print("Shaders:", SHADERS_DIR)
