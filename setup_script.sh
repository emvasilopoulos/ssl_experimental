#!/bin/bash

# Install PyTorch
pip3 install torch==2.5.1 torchvision==0.20.1 torchaudio==2.5.1 --index-url https://download.pytorch.org/whl/cu124

# Install ssl_lib
### check if current directory is the root of the project
if [ ! -f "setup.py" ]; then
    echo "Please run this script from the root of the project"
    exit 1
fi
pip3 install -e .
