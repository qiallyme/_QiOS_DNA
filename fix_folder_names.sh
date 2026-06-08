#!/bin/bash

echo "Starting folder doc rename..."

find . -type f -name "_folder.md" | while read file; do
    dir=$(dirname "$file")
    folder=$(basename "$dir")

    newfile="$dir/_${folder}.md"

    if [ -f "$newfile" ]; then
        echo "Skipping (already exists): $newfile"
    else
        echo "Renaming: $file → $newfile"
        mv "$file" "$newfile"
    fi
done

echo "Rename complete."

# Cleanup check
echo "Checking for leftover _folder.md files..."
remaining=$(find . -type f -name "_folder.md")

if [ -z "$remaining" ]; then
    echo "All files successfully renamed."
else
    echo "WARNING: Some _folder.md files remain:"
    echo "$remaining"
fi

