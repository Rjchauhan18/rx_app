#!/bin/bash

hugo

git add .

git commit -m "Updates"

git push
# Install Reflex
pip install reflex

# Start the Reflex app
reflex run