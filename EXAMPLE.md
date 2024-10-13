# EXAMPLE.md

## My Personal Usage

I [set up](USAGE.md) the shell script `scripts/find-role` such that it does not actually set the environment variable `ROLE` after interactively picking a role prompt. I can  actually export `ROLE` by pressing enter again.

Thus:

- I don't overwrite any existing `ROLE` variable (I might have set it before, and I don't want to lose the previous value).
- I don't fill my environment with variables.

I use these prompts/roles mainly for software development tasks:

1. **Github Copilot Chat:** Tweak Copilot's suggestions by selecting some lines of code in your editor. Call `find-role`, pick a prompt, copy it. Paste the prompt into the Github Copilot Chat Extension for VSCode. Press enter. Github Copilot will explain, rewrite, or work with  the code lines in `#selection`, _according to your prompt._
2. **`llm` cli tool**: Using these prompt together with Simon Willison's [`llm`](https://github.com/simonw/llm/) command-line tool:  I can call `llm` with  
   `llm gpt-4o "$ROLE 'prompt text'"`.  
   This is a great, simple way to interact with AI systems from the command line, and for me was the basis for more complex scripts.
3. **Interacting with Llama models**: The [Perplexity API endpoints](https://docs.perplexity.ai/docs/model-cards)  offer access to fine-tuned variants of Meta's important family of models, the Llama models.  
   Sometimes I use my `explore_perplexity_api.py`  script  to interact with those llama LLMs.
   I call `explore_perplexity_api.py` with the `--role` option.  
   See my [perplexity-api-search](https://github.com/knbknb/perplexity-api-search) for details.

The scripts then set the `ROLE` environment variable to the role that I want to use. Here, _"Education,"CS Bootcamp Instructor"_. This can significantly change the output of the AI system:

## Example of a Terminal Session 

```bash
# EXAMPLE OF A TERMINAL SESSION 
# with the 2 scripts "find-role" and "explore_perplexity_api.py".
# Open two terminal windows side by side, and then:

# Terminal 1: Create fzf preview window, for selecting a role, interactively
`~/ai-system-roles/find-role`
# ... or
`~/bin/find-role`

# the script will print/echo the role definition as an export command
# but will NOT actually set the environment variable:
echo export ROLE='Education,"CS Bootcamp Instructor","From now on, act as an instructor in a computer science bootcamp, teaching algorithms to beginners. You will provide code examples using python programming language. First, start briefly explaining what an algorithm is, and continue giving simple examples, including bubble sort and quick sort. Later, wait for my prompt for additional questions. As soon as you explain and give the code samples. Whenever possible include corresponding visualizations as ASCII art."';

# Terminal 2: copy and paste that output of the find-role script here, 
# modify command as needed:
export ROLE='Education,"CS Bootcamp Instructor","From now on, act as an instructor...';

# call the script that does the heavy lifting (Query LLM and save output to a file)
export PERPLEXITY_API_KEY=your-api-key-here
./explore_perplexity_api.py --prompt "Explain to a non-programmer what a REST-API is" \
   --slug rest-api --role "$ROLE" --role-slug cs-instructor

# output will be saved to a file named final-output/rest-api-<MODELNAME>.md
```

The `--slug` argument to `./explore_perplexity_api.py` is just a label I use to keep track of my interactions with the AI systems and the prompts I've used. The value of `--slug` will become part of the output filename.  
Use any word or phrase you want as a slug, but make sure it is unique to the prompt you're using. The `--slug` should not have spaces or special characters. The same rule applies to the `--role-slug` argument which you can use to test responses to different prompts.

Why all this? It enhances reproducibility and traceability of the AI-generated responses. That is useful when I take a look at the output files, perhaps many months later.

## More Prompts and Personas

Some good collections, presented with both good Prompt Design and GUI Design in mind, and with a lot of additional information:

- [Prompt Library](https://docs.anthropic.com/claude/prompt-library) by Anthropic AI for Claude LLM
- [Prompts from top-rated GPTs in the GPTs Store](https://github.com/ai-boost/awesome-prompts) - Anonymously curated by "AI-Boost". 4.9k Stars on Guthub as of Aug. 2024.

There are many, many more such collections on the web.
