#!/usr/bin/env bash
# helper scipt to prepare a sorted csv file.
# the csv is intended for use with fzf.
# -y 4 sniff-limit
# -c column

# prompts.json is a JSON file with a grouped list of prompts.
# the grouing keys were created by ChatGPT.

< prompts.json \
jq -r 'to_entries | .[] | .key as $k | .value[] | [$k, .] | @csv' \
> prompts-grouped.csv

# add header
sed -i '1i "group","act"' prompts-grouped.csv 

# write new extended csv file: group, name, instructions
csvjoin -y 4 -c "act" prompts-grouped.csv  prompts.csv \
| csvsort -y 4 -c 1,2,3 \
| csvformat -D";" \
> prompts-grouped-sorted.semi.csv

perl -pi -E "s/I want you to/From now on,/g" prompts-grouped-sorted.semi.csv
#perl -pi -E 's/[^"]$/"/g' prompts-grouped-sorted.semi.csv
perl -pi -e 's/([^"])\n/$1"\n/g'  prompts-grouped-sorted.semi.csv
perl -pi -E 's/My first .+$"/"/g' prompts-grouped-sorted.semi.csv
# can be read in by 
#< prompts-grouped-sorted.semi.csv \
# fzf -1 -q "$1" --delimiter "\t" --preview 'echo export ci={1} | fold -s -w $(tput cols)'
