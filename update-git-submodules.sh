#!/bin/bash

# Initialize submodules
git submodule init

# Update submodules to the latest remote commit and merge
git submodule update --remote --merge

echo "Submodules initialized and updated successfully."
