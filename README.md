<p align="center"><h1> AI System Personas</h1></p>

An opinionated list of AI System personas, grouped by topic.

This is my personal version of a collection of personas, or prompt modifiers, or custom instructions.

Check out the `personas-grouped-sorted.csv`.  files for the actual personas.  

Processing is illustrated with the files in the `scripts/` directory.

## Usage

## Basic Usage

Download/clone the repo. Make Bash script file `scripts/find-persona` executable.  
Run `scripts/find-persona` without any arguments. A popup will appear with a list of personas. Keep on typing some keywords. The fuzzy-finder `fzf` will narrow down the selection list.

| fuzzy-finder in action |
|----------|
|   After typing `scripts/find-persona` this should pop up  |
| ![fzf in action](./img/screenshot-terminal-find-persona.png)  |
|   inside Terminal  |

Select one row and press enter. The script will then print the persona as an `export CI=...` to the terminal.  (`CI` is short for "custom instruction" and is the name of the environment variable that I use in my subsequent commands. You can change it to whatever you want.)

Note that the `find-persona` script does not actually export `CI` as an environment variable. You can do that manually if you want to use it in your script. Use copy and paste to do so.  
I configured it this way because

- I don't want to overwrite any customizations I#ve applied to any preexisting CI` variables,
- I don't want to clutter my environment with a lot of variables that I only use once.

## Usage with a script

my main use case for using these personas is in my script `explore_perplexity_api.py` from the [explore-perplexity-api](https://github.com/knbknb/explore-perplexity-api) repo.

Sometimes I call it with the `--persona` option. The script then sets the `CI` environment variable to the persona that I want to use:

```bash
# define persona
export CI="From now on, acts as a computer science teacher...." 
# call the script
./explore_perplexity_api.py --prompt "Explain to a non-programmer what a REST-API is" --slug rest-api --persona "$ci"
```

## License

CC-0, see [LICENSE](./LICENSE) file.

## Previously

This is a continuation of the work started in [my awesome-chatgpt-prompts repo](https://github.com/knbknb/awesome-chatgpt-prompts/) which in turn was a fork of [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts).

My fork has diverged to a point where it's no longer compatible with the original repo, so I've started a new one.
