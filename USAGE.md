# Usage

## Usage as a shell script

You need to have command-line tools `fzf`, `curl`, `perl`, `fold` and `tput` installed.

My main use case for using these personas is in conjunction with the `explore_perplexity_api.py`  script from my [perplexity-api-search](https://github.com/knbknb/perplexity-api-search) repo.

Sometimes I call it with the `--persona` option. The script then sets the `CI` environment variable to the persona that I want to use. Here, "Education,"CS Bootcamp Instructor":

```bash
# EXAMPLE OF A TERMINAL SESSION with the scripts

# Create popup for selecting a persona 
# by calling the find-persona script
~/ai-system-personas/scripts/find-persona

# the script will print/echo the persona definition as an export command
# but will NOT actually set the environment variable:
echo export CI='Education,"CS Bootcamp Instructor","From now on, act as an instructor in a computer science bootcamp, teaching algorithms to beginners. You will provide code examples using python programming language. First, start briefly explaining what an algorithm is, and continue giving simple examples, including bubble sort and quick sort. Later, wait for my prompt for additional questions. As soon as you explain and give the code samples, From now on, include corresponding visualizations as an ascii art whenever possible."';

# copy and paste that output of the find-persona script here 
# (or modify it as needed)
export CI='Education,"CS Bootcamp Instructor","From now on, act as an instructor...';

# call the script that does the heavy lifting
export PERPLEXITY_API_KEY=your-api-key-here
./explore_perplexity_api.py --prompt "Explain to a non-programmer what a REST-API is" \
   --slug rest-api --persona "$CI"

# output will be saved to a file named final-output/rest-api-<MODELNAME>.md
```

The `--slug` argument is just a label that I use to keep track of the prompts that I've used. It will become part of the output filename. Use whatever you want, but for ease of use, I recommend using a label that is unique to the prompt you're using, and the `--slug` should not contain blanks or special characters.