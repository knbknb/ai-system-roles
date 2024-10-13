#!/usr/bin/env bash

# Preprocess the anthropic-prompts.json file

# classification categories:
 csvlook -K 1   -y 3  < data/roles-grouped-sorted.csv | csvcut -d\| -c 2 -H | sort -u | grep "^ "

# ...classification was done by chatgpt-4o... - manual, interactive process

# re-order the columns and create a new CSV file
< anthropic-prompts-classif.json \
    jq -r  ' sort_by(.[0], .[1]) | map([.[0], .[1] + ": " + .[2], .[3]]) | .[] | @csv ' \
> anthropic-prompts-classif.csv