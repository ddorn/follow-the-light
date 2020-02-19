#!/usr/bin/env sh

echo $1

if [[ $1 = "run" ]]; then
	MESA_GL_VERSION_OVERRIDE=3.3 PYTHONPATH=. ./venv/bin/python ./src/main.py
elif [[ $1 = "fmt" ]]; then
	black . --exclude src/atlas.py
elif [[ $1 = "regen-atlas" ]]; then
	cd assets
	mv ~/Downloads/pack-result.zip .
	unzip pack-result.zip
	rm pack-result.zip
	./assets/gen_atlas.py ./assets/texture.json > ./src/atlas.py
	mv ./assets/texture.png ./assets/atlas.png
	cd -
else
	echo "USAGE: make.sh [run|fmt|regen-atlas]"
fi



