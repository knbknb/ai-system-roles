# AI LLM Roles

```text
An opinionated list of LLM roles, or personas, grouped by topic.  
A collection of filterable codesnippets, in a TUI (Text User Interface) format.

In a Linux Terminal, use the "find-role" script to search for roles.  
See the "data/roles-grouped-sorted.csv" file for the actual roles, as plain text snippets.
```

This is my personal version of a collection of roles, also known as personas, prompt modifiers, custom instructions, or similar terms. These are for human-AI interactions with LLMs, Large Language Models such as ChatGPT.

The roles are stored in a single file and were classified by me into groups like "Fun+Leisure", "IT-Expert", "Business", and more.

Specifying a role works like this:

> "As a web developer and software tester, be critical of the code input I provide and provide me with a list of issues in the code."

... but you do this on a terminal. Then you can copy this role description, paste it into the LLM's web form, review and extend the prompt. Alternatively, supply your selection as an additional command-line argument to the LLM, or use it in API-calling code.

Processing/Usage is further illustrated in [USAGE.md](./USAGE.md) below, and in the shell script `find-role`.

## Usage

How I use it in my workflow: See [USAGE.md](USAGE.md#my-personal-usage) for an illustrated description, [EXAMPLE.md](./EXAMPLE.md) for simple examples, and my repo [perplexity-api-search](https://github.com/knbknb/perplexity-api-search) for a convoluted example. (TODO also obsolete? due to API changes).

[FOR-AND-AGAINST-PROMPTING.md](./FOR-AND-AGAINST-PROMPTING.md) are my notes about prompting. They mention why role-prompting is becoming _less_ important these days, actually. It even might become obsolete, or counterproductive, for newer Reasoning Models (such as the OpenAI o1 series of LLMs).

## License

CC-0, see [LICENSE](./LICENSE) file.

## Obsolete? Dubious?

I've sporadically used these codesnippets in my work on a PC, in a Linux Terminal, or in Juypyter Notebooks.

**Since late 2024 you can use the super-smart System Message Generator on [playground.openai.com](https://playground.openai.com) or t Anthropic's [Prompt Generator](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prompt-generator) to generate good prompts interactively.**

(In Playground sidebar, click on "Chat". In Main Panel, near "System Message", click on the "sparkling stars" icon.)

**Anyways, for a while it was a great idea to have a such a list of system prompts for LLMs, similar to Browser Bookmarks, similar to Github Gists/Codesnippets.**