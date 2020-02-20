#!/usr/bin/env sh

if [ $1 = "run" ]; then
	MESA_GL_VERSION_OVERRIDE=3.3 PYTHONPATH=. venv/bin/python src/main.py
elif [ $1 = "fmt" ]; then
	black . --exclude src/atlas.py
elif [ $1 = "regen-atlas" ]; then
	venv/bin/python assets/gen_atlas.py assets/background/ice/layers/*.png --extrude=2 --py-out=src/atlas.py --img-out=assets/atlas.png
else
	echo "USAGE: make.sh [run|fmt|regen-atlas]"
fi



