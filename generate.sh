#!/bin/bash

# Run markdown-pp over every .mdpp file and then call pelican to generate
# the site

FILES=content/*/*.mdpp

for fullfile in $FILES
do
    echo "Processing $fullfile..."
    name="${fullfile%.*}"
    markdown-pp "$fullfile" -o "$name.md"
done

exec pelican -v content/ --ignore-cache -t ../pelican/pelican-themes/pelican-elegant/
