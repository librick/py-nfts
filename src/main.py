#!/usr/bin/env python3
# Generate toaster oven NFTs
# MIT License, do whatever you want
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import os
from pathlib import Path
from base64 import b64encode
from secrets import token_bytes  

class LineWriter:
    def __init__(self):
        self.lineNum = 0
    def write(self, text):
        lineGap = 32
        offsetX = 64
        offsetY = 64 + self.lineNum*(64+lineGap)
        fontPath = os.path.join(os.getcwd(), "./res/UbuntuMono-Bold.ttf")
        fontSize = 84
        font = ImageFont.truetype(fontPath, fontSize)
        color = (255,0,255)
        draw.text((offsetX, offsetY), text, color, font=font)
        self.lineNum += 1

imgPath = os.path.join(os.getcwd(), "./res/toaster-oven.png")
img = Image.open(imgPath)
draw = ImageDraw.Draw(img)
seed = token_bytes(32)
b64 = b64encode(seed).decode()
drawer = LineWriter()
drawer.write("toaster oven")
drawer.write(b64encode(bytes("toaster oven", "utf-8")).decode())
drawer.write(b64)

outpath = os.path.join(os.getcwd(), "nfts")
Path(outpath).mkdir(parents=True, exist_ok=True)
img.save(f'nfts/nft-0x{seed.hex()}.png')
