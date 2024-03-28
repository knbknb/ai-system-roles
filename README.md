# AI LLM Personas

An opinionated list of LLM personas, grouped by topic.

This is my personal version of a collection of personas, or prompt modifiers, or custom instructions. These are for AI-systems, not "system personas" in the sense of user interface design.

Check out the `personas-grouped-sorted.csv` file for the actual personas.  

Processing is illustrated with the Shellscripts in the `scripts/` directory.

## Usage

You need to have command-line tools `fzf`, `curl`, `perl`, `fold` and `tput` installed.

## Basic Usage

Download/clone the repo. Make Bash script file `scripts/find-persona` executable.  
Run `scripts/find-persona` without any arguments. A popup will appear with a list of personas. Keep on typing some keywords. The fuzzy-finder `fzf` will narrow down the selection list and show its preview window inside the terminal.

| preview-window of fuzzy-finder `fzf`|
|----------|
|  Inside Terminal, after typing `scripts/find-persona` this should pop up  |
| ![fzf in action](./img/screenshot-terminal-find-persona.png)  |
|  Use the arrow keys to scroll, or type more keywords to narrow down   |

In the screenshot above, the left half of the preview window shows the available personas. The right half shows a persona definition that matches best. The text either contains the keywords just typed, or matches the list of keywords given.

Select one row and press enter. The script will then print the persona definition as a command `export CI=...` to the terminal.  (`CI` is short for "custom instruction" and is the name of the environment variable that I use in my subsequent commands. You can change it to whatever you want.)

Note that the `find-persona` script does _not actually_ export `CI` as an environment variable. You can do that manually if you want to use it in your script. Use copy and paste to do so.

I configured the script this way because

- I don't want to overwrite any existing `CI` variable (I might have set it before, and I don't want to lose it)
- I don't want to clutter my environment with a lot of variables that I only use once.

## Usage with a script

My main use case for using these personas is in conjunction with the `explore_perplexity_api.py`  script from my [perplexity-api-search](https://github.com/knbknb/perplexity-api-search) repo.

Sometimes I call it with the `--persona` option. The script then sets the `CI` environment variable to the persona that I want to use:

```bash

# create popup for selecting a persona 
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

# output will be saved to a file named final-output/rest-api-<MODELNAME>.txt
```

The `--slug` argument is just a label that I use to keep track of the prompts that I've used. It will become part of the output filename. Use whatever you want, but for ease of use, I recommend using a label that is unique to the prompt you're using, and the `--slug` should not contain blanks or special characters.

## More Prompts and Personas

Some good collections, presented with good GUI Design in mind, and with a lot of additional information:

- [Prompt Library](https://docs.anthropic.com/claude/prompt-library) by Anthropic AI for Claude LLM
- [Prompts from top-rated GPTs in the GPTs Store](https://github.com/ai-boost/awesome-prompts) - Curated by AI-Boost

## License

CC-0, see [LICENSE](./LICENSE) file.

## Previously

This is a continuation of the work started in [my awesome-chatgpt-prompts repo](https://github.com/knbknb/awesome-chatgpt-prompts/) which in turn was a fork of [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts).

My fork has diverged to a point where it's no longer compatible with the original repo, so I've started a new one.
