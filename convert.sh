#!/bin/bash

mkdir -p output/
cp -r input/* output/
find ./output/ -type f -name "*.png" -exec python3 rgb2bgr.py {} \;
