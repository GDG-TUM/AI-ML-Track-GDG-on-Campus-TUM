# Security Policy

Security in a machine learning club is about more than code. It is also about **keys, data, models and prompts**. This page tells you how to report a problem and how to avoid creating one.

## Reporting a vulnerability or a leak

**Please do not open a public issue** for anything sensitive. Use one of these:

1. **GitHub private reporting:** go to the repository's **Security** tab and click **Report a vulnerability**.
2. **Email** [gdgtum@gmail.com](mailto:gdgtum@gmail.com) with the details.

Include what you found, where, and how to reproduce it. Do **not** include the secret or personal data itself.

We are volunteer students, so we promise to **acknowledge your report within 5 days** and keep you updated until it is resolved. Thank you for helping keep the community safe.

### What counts

- An **API key, token, password or credential** committed anywhere (code, notebook cells, outputs, history)
- **Personal data** about real people in the repository (photos, names, phone numbers, grades, health or financial data)
- A malicious or booby-trapped **notebook, model file or dependency**
- A **vulnerability in a project** built in this track (for example, an exposed demo app or a prompt-injection hole)

## I leaked a secret. What now?

Don't panic, and don't try to hide it. It happens to professionals every week.

1. **Revoke the key first.** Go to the provider (for example Google AI Studio) and delete or rotate it. This is the step that actually protects you.
2. **Tell a maintainer** straight away so we can help.
3. **Create a new key** and store it safely (see below).
4. Only then, remove it from the code. Deleting the commit is **not enough**, because the key stays in Git history and may already have been copied.

## Keeping secrets safe

- Keys live in **environment variables**, a local **`.env` file** (already in `.gitignore`), or **Colab Secrets**. Never in code or notebook cells.
- Commit a **`.env.example`** with fake values so others know what is needed.
- Notebook **outputs** can leak keys and data too. Our `nbstripout` pre-commit hook clears outputs before they reach Git.
- Turn on GitHub **push protection** and **secret scanning** for your own repositories.

## Keeping data safe

- **Never commit personal data.** Anonymise or use public and synthetic datasets. See the [Responsible AI guide](docs/responsible-ai.md).
- Don't commit large datasets or model weights. Link to them (Kaggle, Hugging Face Hub, Drive) and say where they came from.
- If a project needs sensitive data, **talk to a maintainer before you start**. Kenya's Data Protection Act, 2019 applies to personal data about people in Kenya.

## Keeping models and dependencies safe

- **Never load a pickle or an untrusted model file blindly.** Python `pickle` files, and some model formats built on them (such as `torch.load` without `weights_only=True`), can run arbitrary code when opened. Prefer formats like **safetensors**, and only load files from sources you trust.
- Check what a package does before you install it, and watch for look-alike names.
- We use **Dependabot** to keep dependencies and GitHub Actions up to date.

## Keeping LLM apps safe

- **Prompt injection is real.** Text a user (or a web page, or a document) gives your app can try to override your instructions. Treat model input as untrusted.
- Give agents **the least power they need**. An agent that can send emails or delete files needs a human in the loop.
- Never put secrets or private data in a prompt you don't control the destination of.

## Supported versions

We support the **latest release and `main`**. Older cohorts' material is archived, not patched.
