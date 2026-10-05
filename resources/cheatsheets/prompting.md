[← Back to AI/ML Track home](../../README.md)

# Prompting Cheat Sheet

Prompting is a skill you can practise and **test**. Treat prompts like code: change one thing, measure, keep what works. For current model names and API details, always use the official [Gemini API docs](https://ai.google.dev/gemini-api/docs).

## A reliable structure

```text
Role:      You are a <role> helping <audience>.
Task:      <exactly what to do>
Context:   <the background the model needs>
Rules:     <constraints: tone, length, what to avoid>
Format:    <exactly how the answer should look, for example a JSON object>
Examples:  <one or two input and output pairs>
Input:     <the thing to process>
```

## Patterns that help

| Pattern | Use when | Example |
|---|---|---|
| **Be specific** | Always | "Summarise in 3 bullet points for a first-year student" beats "summarise" |
| **Give examples** (few-shot) | The style or format is hard to describe | Show two input and output pairs |
| **Ask for a format** | You will process the output with code | "Reply with JSON: `{\"label\": ..., \"reason\": ...}`" |
| **Break the task up** | A single prompt is doing too much | Extract first, then classify, then write |
| **Give it an out** | You want honesty | "If the answer is not in the text, say 'not found'." |
| **Ask for reasoning, then answer** | Multi-step problems | "Think step by step, then give the final answer on its own line." |
| **Set the audience** | Tone matters | "Explain as if to a curious 12-year-old" |

## Settings

| Setting | Effect |
|---|---|
| **Temperature** | Low = predictable and consistent. High = varied and creative. Use low for extraction and classification. |
| **Max output tokens** | Caps the length (and the cost) |
| **System instruction** | Standing rules for the whole conversation |

## Testing prompts

1. Write **10 or more test inputs** with the answers you would accept, including awkward and adversarial ones.
2. Run the prompt on all of them and **score** the outputs (by hand, or with simple rules in code).
3. Change **one** thing. Run again. Did the score go up?
4. Keep a log: prompt version, score, what you learned.

Never judge a prompt from a single good answer.

## Grounding and honesty

- Ask the model to **answer only from the provided sources** and to **cite** them.
- Test with questions that have **no answer**: does it say "I don't know"?
- **Verify** anything that matters. Fluent is not the same as true.

## Safety

- Treat user input and retrieved documents as **untrusted**: they can contain instructions that try to override yours (**prompt injection**).
- Never put **secrets or private data** in a prompt.
- Keep keys in **environment variables or Colab Secrets**, never in code.
- Give agents the **least power** they need, and keep a human in the loop for anything irreversible.

See the [Responsible AI guide](../../docs/responsible-ai.md) and [SECURITY.md](../../SECURITY.md).
