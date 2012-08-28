#!/bin/bash

DIRECTORY="oxygen"
PREFIX="themes"

export PATH="/opt/local/bin:/opt/bin:$PATH"

qrcgen/qrcgen.py "$DIRECTORY" "$PREFIX"
