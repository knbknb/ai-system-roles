# Usage

## Requirements/Dependencies

You need to have the command-line tools `fzf`, `curl`, `perl`, `fold`, and `tput` installed. These are available on most Linux distributions and on macOS via Homebrew or MacPorts.

## Usage as a Shell Script

Install the bash script `find-role` into your path, e.g., in `~/bin`. On the first run, the script will download a single CSV file with my roles/prompts from the repository and store it in `/tmp`.

You do not have to call it `find-role`; you can rename the script to whatever you want.

## Basic Usage

Download or copy the repo. Make the Bash script file `find-role` executable.  
Run `find-role` without any arguments. A window will pop up with a list of roles. Keep typing some keywords. The fuzzy finder `fzf` will shorten the list and show a preview window inside the terminal.  
Pick one row from the left side of the screen and press the enter key.

| Interactive Selection in a Terminal Window:   <br>Preview generated by Fuzzy-Finder <code>fzf</code> |
|----------|
|  Inside Terminal, after typing `find-role`, this should pop up  |
| ![fzf in action](img/screenshot-terminal-find-role.png)  |
|  Terminal-User-Interface (TUI) after executing the `find-role` command    |
| ![fzf in action](img/screenshot-terminal-find-role--grammar.png)  |
|  User typed the keyword "grammar", the list was narrowed down. Use the arrow keys to scroll, or type more keywords to narrow down the list shown on the left half |

In the pictures above:

- The left side shows the available roles.
- The right side shows the best matching role.
- The highlighted text is the selected prompt for the typed keywords. They go into the lower-left corner, near the `>`. (Typing keywords to narrow down the list is optional but recommended for efficiency.)

Using the arrow keys on the keyboard, pick one row and press enter. The selected role definition will appear as a ready-to-run `export` command in the terminal.  
The command `export ROLE=<prompt text>` is about to set a variable `ROLE`. You still have the opportunity to reviewing the role prompt. Then the long prompt text can be cut and pasted for usage in a web form of a chat model. Optionally, save it in a four-letter `$ROLE` environment variable, and use it in terminal commands, or in your script code.

Again, note that the interactive selection did not _immediately_ export `ROLE` as an environment variable. You want to do that yourself, perhaps after renaming the variable. By `export`ing, you can simply use the much shorter `$ROLE` in later commands/interactions with the LLM.

See [EXAMPLE.md](EXAMPLE.md) for more examples.
