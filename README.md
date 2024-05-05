# AI LLM Personas

```text
An opinionated list of LLM personas, grouped by topic. 
See the "personas-grouped-sorted.csv" file for the actual personas.
```

This is my personal version of a collection of personas, or prompt modifiers, or custom instructions. These are for AI-systems, not "system personas" in the sense of user interface design.

Processing/Usage is illustrated with the Shellscripts in the `scripts/` directory.

## Basic Usage

Download/clone the repo. Make Bash script file `scripts/find-persona` executable.  
Run `scripts/find-persona` without any arguments. A popup will appear with a list of personas. Keep on typing some keywords. The fuzzy-finder `fzf` will narrow down the selection list and show its preview window inside the terminal.

| preview-window of fuzzy-finder `fzf`|
|----------|
|  Inside Terminal, after typing `scripts/find-persona` this should pop up  |
| ![fzf in action](./img/screenshot-terminal-find-persona.png)  |
|  Use the arrow keys to scroll, or type more keywords to narrow down the list shown in left half  |

In the screenshot above,

- the left half of the preview window shows the available personas.
- the right half shows a persona definition that matches best.
- the highlighted text contains the selected promptfor the keyword(s) just typed.

Select one row and press enter. The script will then print the persona definition as a command `export CI=...` to the terminal.  (`CI` is short for "`C`ustom `I`nstruction" and is the name of the environment variable that I use in my subsequent commands. You can change it to whatever you want.)

Note that the `find-persona` script does _not actually export_ `CI` as an environment variable. You can do that manually if you want to use it in your script. Use copy and paste to do so.

I configured the script this way because

- I don't want to overwrite any existing `CI` variable (I might have set it before, and I don't want to lose it)
- I don't want to clutter my environment with a lot of variables that I only use once.

## Advanced Usage

How I use it in my workflow: See [USAGE.md](./USAGE.md), and my repo [perplexity-api-search](https://github.com/knbknb/perplexity-api-search)

## More Prompts and Personas

Some good collections, presented with good GUI Design in mind, and with a lot of additional information:

- [Prompt Library](https://docs.anthropic.com/claude/prompt-library) by Anthropic AI for Claude LLM
- [Prompts from top-rated GPTs in the GPTs Store](https://github.com/ai-boost/awesome-prompts) - Curated by AI-Boost

## License

CC-0, see [LICENSE](./LICENSE) file.

## Previously

This is a continuation of the work started in [my awesome-chatgpt-prompts repo](https://github.com/knbknb/awesome-chatgpt-prompts/) which in turn was a fork of [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts).

My fork has diverged to a point where it's no longer compatible with the original repo, so I've started a new one.
