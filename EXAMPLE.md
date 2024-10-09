# EXAMPLE.md

## My Personal Usage

I [set up](USAGE.md) the shell script `scripts/find-persona` such that it does not actually set the environment variable `CI` after interactively picking a persona prompt. I can  actually export `CI` by pressing enter again.

Thus:

- I don't overwrite any existing `CI` variable (I might have set it before, and I don't want to lose the previous value).
- I don't fill my environment with variables.

I use these prompts/personas mainly for software development tasks:

1. **Github Copilot Chat:** Tweak Copilot's suggestions by selecting some lines of code in your editor. Call `find-persona`, pick a prompt, copy it. Paste the prompt into the Github Copilot Chat Extension for VSCode. Press enter. Github Copilot will explain, rewrite, or work with  the code lines in `#selection`, _according to your prompt._
2. **My `explore_perplexity_api.py`  script** from the [perplexity-api-search](https://github.com/knbknb/perplexity-api-search) repo:  
   Sometimes I call `explore_perplexity_api.py` with the `--persona` option.  
The scripts then set the `CI` environment variable to the persona that I want to use. Here, _"Education,"CS Bootcamp Instructor"_. This can significantly change the output of the AI system:

```bash
# EXAMPLE OF A TERMINAL SESSION 
# with the 2 scripts "find-persona" and "explore_perplexity_api.py".
# Open two terminal windows side by side, and then:

# Terminal 1: Create fzf preview window, for selecting a persona, interactively
~/ai-system-personas/scripts/find-persona

# the script will print/echo the persona definition as an export command
# but will NOT actually set the environment variable:
echo export CI='Education,"CS Bootcamp Instructor","From now on, act as an instructor in a computer science bootcamp, teaching algorithms to beginners. You will provide code examples using python programming language. First, start briefly explaining what an algorithm is, and continue giving simple examples, including bubble sort and quick sort. Later, wait for my prompt for additional questions. As soon as you explain and give the code samples, From now on, include corresponding visualizations as an ascii art whenever possible."';

# Terminal 2: copy and paste that output of the find-persona script here, 
# modify command as needed:
export CI='Education,"CS Bootcamp Instructor","From now on, act as an instructor...';

# call the script that does the heavy lifting (Query LLM and save output to a file)
export PERPLEXITY_API_KEY=your-api-key-here
./explore_perplexity_api.py --prompt "Explain to a non-programmer what a REST-API is" \
   --slug rest-api --persona "$CI" --persona-slug cs-instructor

# output will be saved to a file named final-output/rest-api-<MODELNAME>.md
```

The `--slug` argument to `./explore_perplexity_api.py` is just a label I use to keep track of my interactions with the AI systems and the prompts I've used. The value of `--slug` will become part of the output filename.  
Use any word or phrase you want as a slug, but make sure it is unique to the prompt you're using. The `--slug` should not have spaces or special characters. The same rule applies to the `--persona-slug` argument which you can use to test responses to different prompts.

Why all this? It enhances reproducibility and traceability of the AI-generated responses. That is useful when I take a look at the output files, perhaps many months later.
