#!/bin/bash
# SPDX-License-Identifier: LGPL-2.1-or-later

# Directory paths
input_dir="../man"
output_dir="in-progress"

echo "---------------------"
echo "Converting xml to rst"
echo ""
python3 main.py --dir ${input_dir} --output ${output_dir} --file *.xml

# Clean and build
# rm -rf build

# echo "--------------------"
# echo "Building Sphinx Docs"
# echo "--------------------"
# make man
