[← Back to AI/ML Track home](README.md)

# 🚀 Getting Started

Do this checklist once, ideally before Week 1. It takes about 30 minutes, and **you can do the whole track with nothing but a browser**. Local setup is optional.

## 1. Accounts

- [ ] **GitHub account** with [two-factor authentication](https://docs.github.com/authentication/securing-your-account-with-two-factor-authentication-2fa) turned on
- [ ] Accepted your invitation to the **GDG-TUM** organization
- [ ] **Google account** (a personal one is fine). You need it for Colab, Google Drive and Google AI Studio.
- [ ] **Kaggle account** (free). Used for datasets, notebooks and your first competition entry in Week 3.

> ⚠️ Free tiers have usage limits that change. Check the current limits of each service on its official site before you rely on it.

## 2. Pick your setup

| Path | Best if | What you do |
|------|---------|-------------|
| **A. Browser only** (recommended to start) | Old laptop, tight on storage or data | Open notebooks in [Google Colab](https://colab.research.google.com) or [Kaggle](https://www.kaggle.com/code). Nothing to install. |
| **B. Local Python** | Decent laptop, want to work offline | Follow the steps below |

Not sure? Start with **A**. You can switch later. More detail in the [compute guide](resources/compute-guide.md).

### Path A: browser only

1. Open a notebook from [`weekly-sessions/`](weekly-sessions/README.md). Each one has an **Open in Colab** badge.
2. Click **File → Save a copy in Drive** so your changes are yours.
3. Run cells with **Shift + Enter**.

> The Colab badges work once this repository is public. Until then, download the `.ipynb` file and use **File → Upload notebook** in Colab.

### Path B: local Python

You need **Git** and **Python 3.10 or newer**.

| Tool | Why | Check it works |
|------|-----|----------------|
| **Git** | Version control | `git --version` |
| **Python 3.10+** | The language of ML | `python3 --version` |
| **A code editor** (VS Code recommended) | Writing code and notebooks | Opens a folder |

```bash
# 1. Fork the repo on GitHub, then clone your fork
git clone https://github.com/<your-username>/AI-ML-Track-GDG-on-Campus-TUM.git
cd AI-ML-Track-GDG-on-Campus-TUM

# 2. One command creates a virtual environment and installs everything
make setup

# 3. Start Jupyter
source .venv/bin/activate        # Windows: .venv\Scripts\activate
jupyter lab
```

No `make` (common on Windows)? Run these instead:

```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt
pre-commit install
```

## 3. Configure Git

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

## 4. Join the community

- [ ] Join the track channel (link shared by the core team)
- [ ] Open a **Member Roadmap** issue in the [member-roadmaps](https://github.com/GDG-TUM/member-roadmaps) repo
- [ ] Make your first contribution: [add your profile](members/README.md)

## 5. Know the rules

- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Contributing guide](CONTRIBUTING.md)
- [Security policy](SECURITY.md)
- [Responsible AI guide](docs/responsible-ai.md)
- **Never commit** passwords, API keys, tokens, `.env` files or personal data.

## 6. Optional: a Gemini API key (needed from Week 7)

You will use [Google AI Studio](https://aistudio.google.com) to create a key for the Gemini API in Week 7. **Do not create or paste a key into a notebook before then.** We will show you how to store it safely (Colab Secrets or an environment variable) so it never lands on GitHub.

## ✅ Ready?

Go to [Week 1: Welcome and Python for data](weekly-sessions/week-01-welcome-and-python-for-data/README.md).

**Stuck on setup?** That is normal and we want to help. [Ask a question](https://github.com/GDG-TUM/AI-ML-Track-GDG-on-Campus-TUM/issues/new/choose) or tell the Track Lead.
