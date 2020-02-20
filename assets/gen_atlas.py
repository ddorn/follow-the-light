#!/usr/bin/env python3

from typing import List

import click
import rectpack
from PIL import Image, ImageDraw
from rectpack import newPacker
from rectpack.packer import Packer


def gen_py_string(bin: rectpack.MaxRectsBssf, files: List[str], extrude=0):
    TEMPLATE = r'''# This file is generated by [gen_atlas.py]

import enum

TEX_WIDTH = WW
TEX_HEIGHT = HH

RECTS = [
    #   x,     y,     w,     h
    BUFFER
]
"""
Coordinates of the rectangles of each image in the atlas.
The coordinates increase left and up, as in a standard R² 
coordinate system. Indices corresponds to 4 time the sprite ids.
"""


class Sprite(enum.Enum):
    ENUM'''

    # size
    width = bin.width
    height = bin.height

    # buffer
    buffer = [
        "{x:<{s}}, {y:<{s}}, {w:<{s}}, {h:<{s}},  # {i}".format(
            s=5,
            x=rect.x + extrude,
            y=rect.y + extrude,
            w=rect.width - extrude * 2,
            h=rect.height - extrude * 2,
            i=i
        )
        for i, rect in enumerate(sorted(bin, key=lambda rect: rect.rid))
    ]
    buffer_sep = "\n" + " " * 4  # one tab
    buffer_str = buffer_sep.join(buffer)

    # enum
    enum_sep = "\n" + " " * 4  # one tab
    enum_str = enum_sep.join(
        f"{python_enum_name(name)} = {i}" for (i, name) in enumerate(files)
    )

    code = (
        TEMPLATE.replace("BUFFER", buffer_str)
        .replace("ENUM", enum_str)
        .replace("WW", str(width))
        .replace("HH", str(height))
    )

    return code


def python_enum_name(name: str):
    name = name.rpartition("/")[2].partition(".")[0].upper()

    return name


def extruded(im: Image.Image, ex: int):
    """Expand an image of `ex` pixels on each side, stretching the border"""
    if ex <= 0:
        return im

    w, h = im.size
    new = im.crop((-ex, -ex, w + ex, h + ex))
    nw, nh = new.size

    # Extend the side
    left = im.crop((0, 0, 1, h))
    right = im.crop((w - 1, 0, w, h))
    top = im.crop((0, 0, w, 1))
    bottom = im.crop((0, h - 1, w, h))
    for d in range(ex):
        new.paste(left, (d, ex, d + 1, ex + h))
        new.paste(right, (nw - d - 1, ex, nw - d, ex + h))
        new.paste(top, (ex, d, ex + w, d + 1))
        new.paste(bottom, (ex, nh - d - 1, ex + w, nh - d))

    # Extend the corners
    draw = ImageDraw.Draw(new)
    draw.rectangle((0, 0, ex, ex), im.getpixel((0, 0)))  # top-left
    draw.rectangle((nw - ex, 0, nw, ex), im.getpixel((w - 1, 0)))  # top-right
    draw.rectangle((0, nh - ex, ex, nh), im.getpixel((0, h - 1)))  # bottom-left
    draw.rectangle(
        (nw - ex, nh - ex, nw, nh), im.getpixel((w - 1, h - 1))
    )  # bottom-right

    return new


def combine(bin: rectpack.MaxRectsBssf, images: List[Image.Image]) -> Image.Image:
    """Combine a list of images into an atlas, according to the rects positions"""
    bw, bh = bin.width, bin.height
    atlas = Image.new("RGBA", (bin.width, bin.height))

    for rect in bin:
        x, y = rect.x, bh - rect.y
        atlas.paste(images[rect.rid], (x, y - rect.height, x + rect.width, y))

    return atlas


@click.command()
@click.option(
    "--extrude", default=0, help="Expend the imagepast the border of N pixels"
)
@click.argument("files", nargs=-1)
@click.option("--py-out", default="atlas.py")
@click.option("--img-out", default="atlas.png")
@click.option("--atlas-size", default=(2048, 2048))
def main(files, extrude, img_out, py_out, atlas_size):
    files = sorted(files)
    images = [Image.open(file) for file in files]

    if extrude:
        images = [extruded(im, extrude) for im in images]

    # Packer setup
    packer: Packer = newPacker(rotation=False)
    for i, im in enumerate(images):
        packer.add_rect(*im.size, i)
    packer.add_bin(*atlas_size)

    # Pack all the images in the atlas
    packer.pack()
    atlas = combine(packer[0], images)

    # Output
    atlas.save(img_out)
    py = gen_py_string(packer[0], files, extrude)
    with open(py_out, "w") as f:
        f.write(py)


if __name__ == "__main__":
    main()
