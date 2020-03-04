#!/usr/bin/env sh

if [ $1 = "run" ]; then
	MESA_GL_VERSION_OVERRIDE=3.3 PYTHONPATH=. venv/bin/python src/__main__.py
elif [ $1 = "fmt" ]; then
	black . --exclude src/graphism/atlas.py
elif [ $1 = "regen-atlas" ]; then
	venv/bin/python assets/gen_atlas.py assets/player/*.png assets/background/*/*.png --extrude=2 --py-out=src/graphism/atlas.py --img-out=assets/atlas.png --trim --fix-alpha
else
	echo "USAGE: make.sh [run|fmt|regen-atlas]"
fi



