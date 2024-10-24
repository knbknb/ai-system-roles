# AI LLM Roles

```text
An opinionated list of LLM roles, or personas, grouped by topic. 
See the "data/roles-grouped-sorted.csv" file for the actual roles.
```

This is my personal version of a collection of roles, also known as personas, prompt modifiers, custom instructions, or similar terms. These are for human-AI interactions with LLMs, Large Language Models such as ChatGPT.

The roles are stored in a single file and they were classified by me into groups like "Fun+Leisure", "IT-Expert", "Business", and more.

Specifying a role works like this:

> "As a web developer and software tester, be critical of the code input I provide and provide me with a list of issues in the code."

... but you do this on a terminal. Then you can copy and paste this role description and put it into the LLM's web form. Alternatively, supply this as an additional command-line argument to the LLM.

Processing/Usage is further illustrated in [USAGE.md](./USAGE.md) below, and in the Shellscripts `find-role`.

## Usage

How I use it in my workflow: See [USAGE.md](USAGE.md#my-personal-usage), [EXAMPLE.md](./EXAMPLE.md), and my repo [perplexity-api-search](https://github.com/knbknb/perplexity-api-search).

[FOR-AND-AGAINST-PROMPTS.md](./FOR-AND-AGAINST-PROMPTS.md) is a critical re-assessment of how important these roles actually are.

## License

CC-0, see [LICENSE](./LICENSE) file.
