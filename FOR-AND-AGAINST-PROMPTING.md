# FOR AND AGAINST PROMPTING

## Synopsis

The following is from a conversation about prompt engineering, featuring multiple perspectives from experts at Anthropic.

See podcast video [AI prompt engineering: A deep dive](https://www.youtube.com/watch?v=T9aRN5JkmL8) from September 2024.

## Summary

### What prompt engineering entails

- Letting users get things done that they wouldn't be able to do otherwise.
- a way of communicating clearly with models. Transform a complex task or piece of information and make it accessible to an educated layperson.
- Needs experimentation and iteration.
- Allow users to revert to a clean slate and refine prompts.
- Avoid overcomplicating things. Just write a clear description of the task. "We write essays and treat them like code".  Do not build crazy abstractions.
- Podcast Participants gave no strict, formal definition of what a prompt is. (See Appendix of [The Prompt Report: A Systematic Survey of Prompting Techniques](https://arxiv.org/abs/2406.06608) for many such definitions.)

### Prompts in enterprise applications

- An engineering aspect comes from integrating the workflow into the customers' larger systems as a whole.
- It often involves more than just a single prompt.
- More features like the availability of RAG, tools, and APIs also matter in enterprise applications.
- Latency issues, rate limits, and upload limits.
- Engineers need to perform well in a _3-role_ relationship: the user, the model, and the prompt engineer.

### What makes a good prompt engineer?

- Actually enjoy the process of interacting with the model. Pushing it to its limits.
- Clear communication, clear specifications, and understanding the task.
- The ability to iterate, often for very long conversations.
- The ability to provide a full fact set to the model, but not too much.
- Anticipate edge cases or potential misinterpretations, being aware of one's own assumptions.
- Closely read/look at the model's output and adjust the prompt accordingly. Experiment further.
- Learn something from the interaction (thinking and reflecting) itself, not necessarily from the LLM's output.
- Know when to stop grinding and polish the prompt. The mythically perfect prompt is almost never necessary.
- Describe in general terms how those edge cases should be handled.
- Give the model the option to provide "a way out" gracefully, if it cannot do the task. Allow it to saying "I don't know", that's a valid answer.
- Can work with text prompts but also with images even if the techniques are different (multi-shot prompting does not work as well for images).
- For API tasks, can balance polishing the code and polishing the prompt.
- For API tasks, can get the prompt right such that it can be called millions of times and still work reliably (unlike one-off personal tasks).
- Know how to interact with an unfinished pretrained model; they are different from a fine-tuned model. Know the difference between prompting a consumer model (reliability) and a research model (focus on diversity).
- Know how to apply meta-prompting: e.g., give an LLM a paper about a new prompt engineering technique and ask it to summarize it and give examples, a template, questions for other models, etc.

Participants note the importance of understanding real-world inputs, as users may not provide perfectly structured inputs, unlike typical evaluation cases. Often the input is even incomprehensible, minimalistic, when users fall into (bad) chatting habits from talking to humans (no punctuation, many typos, implicit assumptions, unclear instructions that even a fellow human would not understand...).

### The nature of prompts

- Should be seen as natural language code or something else.
- Describe the task really well with nuance and context, important to _you_.

### The effectiveness of providing models with context or roles

Model reliability, the potential of models to handle varied inputs, and how to craft prompts that are robust enough for enterprise-level deployment. There’s a focus on understanding the psychology of models, emphasizing the need for detailed communication, and stepping back to analyze the complete set of information required for tasks.

- (e.g., telling a model it's a teacher grading an assignment) and the extent to which models should be treated as intelligent entities that can be honest about tasks.

### Evolution of Prompt Engineering

- Past: More reliance on "hacks" and tricks. "Persona engineering" getting less common.
- Present: Sophisticated interactions, better models, emphasis on clearer communication.
- Ongoing Shift: Moving from individual clever solutions to structured, repeatable systems.
  - Chain-of-thought prompts and now reasoning prompts just work; this needs some time to get used to. Full understanding of why is not always possible.
  - Jailbreaking the model, getting it to do things it wasn't designed to do, can be insightful. Needs some knowledge of how the LLM works internally.

Models gradually improve at handling complex prompts. Prompt engineering is akin to programming, where precision and version control are crucial.

### The future of prompt engineering

Models are getting better at understanding tasks; there will always be a need for clear specifications, and prompt engineering might evolve rather than disappear.

- Example: For math tasks. "Thinking step by step" is now part of the training process and "native" to the model. Users do not have to ask for it anymore.

That models cannot do any assigned task at all becomes rarer, less of a problem.

- No need to hide complexity from the model; it can handle it. The more context, the better.
- Increasing importance of meta-prompting.

There is potential for models to assist more in prompt creation, and asking back well-formed questions, making the process more collaborative.

- Introspection skills of the users might become more important, as the model can ask back for clarification.
- LLMs might become so powerful at interviewing and understanding that the LLM figuring out what the user wants can be a rich but unfamiliar experience. They might know a lot from previous interactions, getting better at understanding the user's intent, knowing things magically.

Overall, the conversation is an in-depth exploration of prompt engineering, its challenges, best practices, and future directions, offering a mix of technical insights, practical advice, and philosophical musings about interacting with AI models.

--------------------------------------------

(not in the conversation, but related)

### Evolution of LLMs

The evolution of LLMs can be roughly mapped as follows:

- Language Modeling (Basic Next Token Prediction)
- Completion/Generation
- Instruction Following
- Chat/Dialogue
- Reasoning/Tool Use
- Multimodal (Current/Emerging)
- Cross-modal reasoning

However, it's important to note that:

- These capabilities often overlap and develop in parallel.
- Earlier capabilities continue to improve alongside newer ones.
- The boundaries between these stages aren't always clear-cut.
- Different models might develop these capabilities in slightly different orders.

- Multimodal and cross-modal reasoning require different prompts and interactions than earlier stages.
  - Example: Image prompts: ask the model to assign a high-school grade to an image—surprisingly, that works well.
  - A larger framework and research opportunities are described in [The Metacognitive Demands and Opportunities of Generative AI](https://arxiv.org/abs/2312.10893)
  
The evolution is more like a continuous spectrum rather than discrete steps, with each new capability building upon and enhancing previous ones.

## References

- [AI prompt engineering: A deep dive](https://www.youtube.com/watch?v=T9aRN5JkmL8) - Source of the conversation.
- [The Metacognitive Demands and Opportunities of Generative AI](https://arxiv.org/abs/2312.10893) Tankelevitch, Lev and Kewenig, Viktor and Simkute, Auste and Scott, Ava Elizabeth and Sarkar, Advait and Sellen, Abigail and Rintel, Sean. in: Proceedings of the CHI Conference on Human Factors in Computing Systems, ACM, 2024, 1–24.
  - Everything on a more abstract level.
  - A much deeper dive into prompting and interacting with Generative AI.
- [The Prompt Report: A Systematic Survey of Prompting Techniques](https://arxiv.org/abs/2406.06608) - In the appendix of this report, there is a list of prompt definitions from various sources.
