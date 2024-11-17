# AI LLM Roles

```text
An opinionated list of LLM roles, or personas, grouped by topic. 
See the "data/roles-grouped-sorted.csv" file for the actual roles.
```

This is my personal version of a collection of roles, also known as personas, prompt modifiers, custom instructions, or similar terms. These are for human-AI interactions with LLMs, Large Language Models such as ChatGPT.

The roles are stored in a single file and were classified by me into groups like "Fun+Leisure", "IT-Expert", "Business", and more.

Specifying a role works like this:

> "As a web developer and software tester, be critical of the code input I provide and provide me with a list of issues in the code."

... but you do this on a terminal. Then you can copy this role description, paste it into the LLM's web form, review and extend the prompt. Alternatively, supply your selection as an additional command-line argument to the LLM, or use it in API-calling code.

Processing/Usage is further illustrated in [USAGE.md](./USAGE.md) below, and in the shell script `find-role`.

## Usage

How I use it in my workflow: See [USAGE.md](USAGE.md#my-personal-usage) for an illustrated description, [EXAMPLE.md](./EXAMPLE.md) for simple examples, and my repo [perplexity-api-search](https://github.com/knbknb/perplexity-api-search) for a convoluted example.

[FOR-AND-AGAINST-PROMPTING.md](./FOR-AND-AGAINST-PROMPTING.md) are my notes about prompting. They mention why role-prompting is becoming _less_ important these days, actually.

## License

CC-0, see [LICENSE](./LICENSE) file.