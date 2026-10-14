[← Back to AI/ML Track home](../README.md)

# 🎓 Session Playbook

How to run a great session, even if it is your first time teaching. You do **not** need to be an expert. Teaching something you just learned is one of the best ways to learn it, and you will have a helper beside you.

Start from the [session template](../weekly-sessions/_template/README.md): copy it into a new folder named `week-NN-short-title/`.

---

## 👥 Roles

| Role | Does | Typical person |
|---|---|---|
| **Host** | Plans and leads the session, owns the notebook and notes | Track Lead, maintainer or any member |
| **Helper** | Circulates and unblocks people. Aim for **one helper per 8 learners**. | Maintainers, mentors, returning members |
| **Timekeeper and scribe** | Keeps to time, takes notes and questions for the notes PR | Anyone |
| **Dry-run buddy** | Runs the notebook on a fresh Colab before the session | A helper |

---

## 🗓️ Timeline

| When | Do this |
|---|---|
| **T minus 7 days** | Pick the topic from the [roadmap](../roadmap/semester-roadmap.md). Open a **draft PR** from the template. Write two or three concrete learning objectives. |
| **T minus 5** | Draft the notebook. Prefer built-in or tiny datasets. Run it on a **fresh** Colab and on Kaggle. |
| **T minus 2** | **Dry run** with a helper. Fix every snag. Freeze the content. Post the agenda and pre-work in the track channel. |
| **T minus 1** | Reminder with prerequisites. Check the venue: projector, power, Wi-Fi. Put **offline copies** (notebook and any data) on a USB drive. |
| **Session day** | Arrive 30 minutes early. Open the notebook. Test the projector font size. |
| **T plus 1 to 2 days** | Merge the **notes PR**. Share the feedback link. Thank the helpers. |

---

## ⏱️ Run of show (90 minutes)

| Time | Min | What | Tips |
|---|:-:|---|---|
| 0:00 | 10 | **Arrive and set up** | Helpers fix Colab and login problems now, not mid-session |
| 0:10 | 5 | **Goal and agenda** | State the one thing everyone will be able to do by the end |
| 0:15 | 20 | **Concept and demo** | One idea at a time. Tell a story, show it working, then explain. No more than 20 minutes of talking. |
| 0:35 | 40 | **Hands-on in pairs** | Driver and navigator **swap every 10 minutes**. Helpers circulate. |
| 1:15 | 5 | **🛡️ Responsible AI moment** | Ask one question: who could be affected, and how could this go wrong? |
| 1:20 | 10 | **Share-out and challenge** | Two pairs show something. Explain the take-home challenge and how to ask for help. |

---

## 🧠 Teaching principles

- **Show, then do.** Learners remember what they type, not what they watch.
- **One new idea per 10 minutes.** Everything else is review.
- **Start from a question or a story**, not a definition. "Can a computer read my handwriting?" beats "Supervised learning is...".
- **Make it work first, then explain why.** A running model builds confidence.
- **Celebrate mistakes.** An error message is information. Say so out loud.
- **Stuck for 10 minutes? Ask.** Tell people this at the start and mean it.
- **Pair, don't isolate.** Pairs explain things to each other, which doubles the learning.

### 🎬 The intuition-first standard

Every session and notebook should pass this checklist before it is marked ready. The style is borrowed from [Sebastian Lague's neural network video](https://www.youtube.com/watch?v=hfMk-kjRv4c): start with a concrete puzzle, let people turn the knobs by hand, and bring in each new idea only when the old one hits a wall. [Week 1](../weekly-sessions/week-01-welcome-and-python-for-data/README.md) is the reference example.

| # | The session... | Week 1 example |
|:-:|---|---|
| 1 | **Opens with a concrete puzzle**, not a definition or a tool | "How much tea should we make tomorrow?" |
| 2 | **Builds like a staircase.** Each part uses only what earlier parts taught, and the notebook opens with a table of what each part gives the next | One day by hand → 5 days in NumPy → 120 days → a pandas table → charts → a model |
| 3 | **Shows a picture before a formula.** Every new idea gets a chart or diagram | The scatter plot comes before the line and its formula |
| 4 | **Lets learners be the machine first.** They tune it by hand before the library does it | `try_line()` and sliders, then `np.polyfit` |
| 5 | **Motivates each new idea by a limit of the last one** | Copying a cell is slow → a function; one guess at a time is slow → a loop; 200 guesses → the error valley |
| 6 | **Asks learners to predict before they run.** At least three 🤔 *Predict first* prompts | "More tea on rainy days, or less?" |
| 7 | **Keeps code small and explained.** One idea per cell, about 15 lines at most, and every line that is not obvious has a comment. Plot-only cells say *"just look at the picture"* | The recipe is one line, reused unchanged from 1 day to 120 |
| 8 | **Names things after people have done them**, and ends with a vocabulary table | "The two knobs are the model's *parameters*" |
| 9 | **Has a payoff**: the model is used on something real | Tomorrow's forecast: make about 226 cups |
| 10 | **Breaks the model on screen** in the Responsible AI moment, rather than only discussing it | The 150 mm storm day |
| 11 | **Has a host guide**: beats, what to ask the room, and the snags to expect | The collapsible guide in the Week 1 README |
| 12 | **Spends little time on tools and a lot on ideas.** Teach only the tool skills the session's question needs; the rest goes to [cheat sheets](../resources/cheatsheets/python-data.md) | Week 1 teaches six pandas moves, not the whole library |

### Live-coding tips

- Zoom the font to at least 150%, and use a light or high-contrast theme in a bright room.
- Type slowly and say what you are typing.
- Keep each cell short. Run it, show the output, explain it.
- When something fails, narrate how you debug it. That is the most valuable lesson of the day.

---

## 🌍 Inclusion and accessibility

- **Assume no prior knowledge.** Define each term the first time. Add it to the [glossary](../resources/glossary.md).
- **Mind data costs.** Share datasets in advance and use small ones. Offer files on USB.
- **Mind devices.** Not everyone has a laptop. Pair people up, and check that things work on a phone browser when possible.
- **Language.** Explaining a concept in Swahili as well as English is welcome.
- **Rotate the driver** so quieter members get hands on the keyboard. Notice who has not spoken, and invite them gently.
- **Colour-blind friendly charts** and readable fonts. Add alt text in notes.
- **Breaks.** For sessions over 90 minutes, take five.
- **Recording.** Only with everyone's consent, and never during the share-out of personal projects.

---

## 🧰 Troubleshooting kit

| Problem | Fix |
|---|---|
| Colab is down or slow | Switch to **Kaggle Notebooks**, or run the notebook locally |
| No internet at the venue | Use the **offline copies** and a locally installed environment. A phone hotspot can serve a few people. |
| A library version breaks the notebook | Add a pinned `pip install` cell at the top, and open an issue |
| Someone cannot sign in | Pair them with a neighbour, and fix their account after the session |
| No GPU available | Use the CPU path or a smaller model, and keep the GPU as an optional extra |
| Running out of time | Cut the hands-on, never the Responsible AI moment or the challenge briefing |

---

## 📝 After the session

**Notes PR** (within 48 hours), added to the week's README:

- Slides and recording links (if any)
- Three to five key takeaways
- Questions that came up, with answers
- Corrections to the notebook
- Extra resources people asked for

**Collect feedback:** share the *Session feedback* issue form link.

**Thank people:** helpers, mentors and the venue.

### Mini retrospective (host and helpers, 10 minutes)

| What went well? | What should we change? | Actions (who, by when) |
|---|---|---|
| | | |

Add actions as issues so they do not get lost.
