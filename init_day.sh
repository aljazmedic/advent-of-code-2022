#/bin/bash

py=$(which python)
# First argument as a number if given else default to  current day
if [ -z "$1" ]; then
    day=$(date +%d)
else
    day=$1
fi
((day = $day + 0))

# Create new directory
# Get current day of the month
year=$(date +%Y)
# Create directory
day_path="./Day$day"
((day = $day + 0)) # Remove leading zeros
mkdir -p "$day_path"
echo "Created directory for day $day"
base_url="https://adventofcode.com/$year/day/$day"

# Write a readme

if [ -f "$day_path/README.md" ]; then
    echo "README file already exists"
else
    # Generate README file
    cat <<EOF >"$day_path/README.md"
# Day $day

$base_url
Input:
$base_url/input
EOF
fi

cat "$day_path/README.md"

# CUrl the instrucitons
curl -s -b "session=$SESSION" $base_url >"$day_path/INSTRUCTIONS.md"

# Write sol script
if [ -f "$day_path/solution.py" ]; then
    echo "Solution file exists"
else
    cp ./.template/solution.py "$day_path/solution.py"
fi

cp ./.template/t.gitignore "$day_path/.gitignore"

touch "$day_path/input.txt" # Don't copy, just touch
cp ./.template/base.py "$day_path/base.py"

# cd into the directory, run base
cd "$day_path"
$py base.py
