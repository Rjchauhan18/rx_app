#!/bin/bash

hugo

git add .

git commit -m "Updates"

git push
# Install Reflex
# pip3 install reflex

# Start the Reflex app
reflex run