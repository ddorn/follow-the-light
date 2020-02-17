#!/usr/bin/env sh

mv ~/Downloads/pack-result.zip .
unzip pack-result.zip
rm pack-result.zip
./assets/gen_atlas.py ./assets/texture.json > ./src/atlas.py
mv ./assets/texture.png ./assets/atlas.png
