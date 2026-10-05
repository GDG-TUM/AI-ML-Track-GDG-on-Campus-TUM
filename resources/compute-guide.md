[← Back to AI/ML Track home](../README.md)

# 🖥️ Compute Guide

**You do not need a GPU or a powerful laptop for this track.** Everything in the core curriculum runs for free in your browser. This page helps you choose a setup, avoid losing work and cope with expensive data.

> [!WARNING]
> **Free tiers change.** Usage limits, GPU availability and rules are set by Google and Kaggle, and they change without notice. Check the official pages for the **current** terms, and never rely on a free GPU being there at a deadline.

## Choose your setup

| | **Google Colab** | **Kaggle Notebooks** | **Local Python** |
|---|---|---|---|
| **Cost** | Free tier | Free | Free |
| **Install needed** | None | None | Python, Git |
| **GPU** | Often available, not guaranteed | Available with usage limits | Only if your laptop has one |
| **Datasets** | Upload or download each session | Attach hosted datasets in one click | Download once, keep forever |
| **Works offline** | No | No | **Yes** |
| **Best for** | Our notebooks, first-time learners | Competitions, big datasets | Offline work, long projects |

**Not sure? Start with Colab**, move to Kaggle for competitions, and add a local setup if you want to work offline.

## Google Colab tips

- **Save a copy first:** *File → Save a copy in Drive*, or save to GitHub. Unsaved Colab sessions disappear.
- **Sessions disconnect** when idle or when the free limit runs out. Save often and keep notebooks able to **Restart and run all**.
- **GPU:** *Runtime → Change runtime type → GPU*. If none is available, use the CPU or try later. Please **turn the GPU off** when you do not need it, since free capacity is shared.
- **Secrets:** use the **🔑 Secrets** panel in the left sidebar for API keys. Never paste a key into a cell.
- **Install a library:** `!pip install package-name` in a cell, then restart the runtime if asked.
- **Files vanish** when the session ends. Mount Drive or download results you want to keep.

## Kaggle Notebooks tips

- **Attach datasets** from the right-hand panel, so there is no download at all.
- **Internet is off by default** in some notebooks. Turn it on in settings when you need to install packages or call an API, and note that competitions may restrict it.
- **GPU use is limited per week**, and the limit is published on Kaggle. Check it before a big run.
- **Save a version** (*Save & Run All*) to keep a record of what ran and what it produced.

## Local setup

```bash
git clone https://github.com/<your-username>/AI-ML-Track-GDG-on-Campus-TUM.git
cd AI-ML-Track-GDG-on-Campus-TUM
make setup                      # or: python3 -m venv .venv && pip install -r requirements-dev.txt
source .venv/bin/activate
jupyter lab
```

- Always work inside a **virtual environment** (`.venv`), never in the system Python.
- 8 GB of RAM is comfortable, and 4 GB is workable for our notebooks. Close other programs.
- No GPU? That is fine. The notebooks that need one say so and have a Colab path.

## 📶 If data bundles are expensive

- **Download once, on campus Wi-Fi**, and keep a copy on a USB drive or phone. Share with teammates.
- **Prefer Kaggle** for big datasets: they are already next to the compute, so you download nothing.
- **Use small datasets** while you develop. Sample 10% of the data, get everything working, then scale up once.
- **Work offline** with a local setup once your libraries and data are in place.
- **Pre-download pretrained models** at the venue, not at home.
- Ask the Track Lead: we keep **offline copies** of session notebooks and small datasets, and can share them in the room.

## 💻 If your laptop is old or slow

- Use **Colab or Kaggle**. Their computers do the work, and your laptop just needs a browser.
- Use a **lightweight browser** with fewer tabs open.
- **Phone-friendly:** Kaggle and Colab run on a phone browser well enough to read and run a notebook, though typing code is painful. Pair with a friend who has a laptop.
- Tell the Track Lead if you are blocked. We would much rather solve it than have you drop out.

## 🔋 Power cuts and unreliable internet

- **Save often.** Download your notebook (*File → Download .ipynb*) before long runs.
- Commit small pieces of work to Git so a lost session costs minutes, not hours.
- Keep a **charged battery** and a **phone hotspot plan** for emergencies.

## 💰 Never pay by accident

- You never need to pay for compute in this track.
- If you use a cloud service for a project, set a **budget alert first** and **delete resources when you finish**. See the [Cloud Track](https://github.com/GDG-TUM/Cloud-Track-GDG-on-Campus-TUM) for how.
- Be careful with API keys: a leaked key can run up a bill. See the [security policy](../SECURITY.md).

## 🌱 Be a good citizen

Free compute is shared. Don't run jobs you don't need, don't try to bypass limits, and prefer **small models and short runs**. They are friendlier to everyone, and to the planet.
