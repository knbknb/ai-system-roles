# EXAMPLE.md

## Review before exporting

I [set up](USAGE.md) the shell script `scripts/find-role` such that you must review the output the script returns. The `find-role` script  does _not actually set_ the environment variable `ROLE` after interactively picking a role prompt. _After reviewing_, export environment variable `ROLE` by pressing "enter" again.

This way:

- No shell commands are issued without your consent.
- We don't overwrite any pre-existing `ROLE` variable (I might have set it before, and I don't want to lose its previous value).
- We don't needlessly fill the shell environment with variables that might not be used, or trip us up later.

## My Personal Usage

I use these prompts/roles mainly for these tasks:

1. **Interacting with LLMs via the Browser**: Classic mode of interaction with LLMs such as ChatGPT.
2. **GitHub Copilot Chat:** Tweak Copilot's suggestions by selecting some lines of code in your editor. Call `find-role`, pick a prompt, copy it. Paste the prompt into the GitHub Copilot Chat Extension for VSCode and press enter. GitHub Copilot will explain, rewrite, or work with  the code lines in `#selection`, _according to your prompt_.
3. **`llm` cli tool**: I often use these prompts together with Simon Willison's [`llm`](https://github.com/simonw/llm/) command-line tool. I can call `llm` with  
   `llm gpt-4o "$ROLE 'prompt text'"`.  
   This is a great, simple way to interact with AI systems from the command line, and for me was the basis for more complex scripts.

The scripts then set the `ROLE` environment variable to the role that I want to use. Here I use the role labeled _"Education,"CS Bootcamp Instructor"_. This can significantly change the output of the AI system.

## Illustrated Example of a Terminal Session

```bash
# EXAMPLE OF A TERMINAL SESSION 
# with the 2 scripts "find-role" and (optionally) "explore_perplexity_api.py".
# Open two terminal windows side by side, and then:

# Terminal 1: Create fzf preview window for selecting a role, interactively
`. ~/ai-system-roles/find-role`
# ... or
`. ~/bin/find-role`

# ...select a line from the list of roles, 
# as shown in the fzf preview window, see screemshot above...

# the script will print/echo the role definition as an export command
# but will NOT actually set the environment variable:
echo export ROLE='Education,"CS Bootcamp Instructor","From now on, act as an instructor in a computer science bootcamp, teaching algorithms to beginners. You will provide code examples using the Python programming language. First, start briefly explaining what the user asked for, and continue giving simple examples. Later, wait for my prompt for additional questions. Then you explain and give code examples. Whenever possible include corresponding visualizations as ASCII art."';

# Terminal 2: copy and paste that output of the find-role script here, 
# modify command as needed:
export ROLE='Education,"CS Bootcamp Instructor","From now on, act as an instructor...';

# call the llm cli tool, 
# output will be shown in terminal and also saved to a file 
export OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
llm -m 4o-mini -s "$ROLE"  "Explain to a non-programmer what a REST-API is"  | tee > /var/tmp/rest-explanation.txt
```

## More Prompts and Personas

Some good collections, presented with both good Prompt Design and GUI Design in mind, and with a lot of additional information:

- [Prompt Library](https://docs.anthropic.com/claude/prompt-library) by Anthropic AI for Claude LLM
- [Prompts from top-rated GPTs in the GPTs Store](https://github.com/ai-boost/awesome-prompts) - Anonymously curated by "AI-Boost". 4.9k Stars on GitHub as of Aug. 2024. There a re many collections like this on the web.
- [Prompt Engineering](https://github.com/NirDiamant/Prompt_Engineering) - Curated by Nir Diamant. Useful and comprehensive set of tutorials and implementations. 1.9k Stars on GitHub as of Nov. 2024.
