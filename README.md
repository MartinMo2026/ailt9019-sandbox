# ailt9019-sandbox

AILT9019 AI Literacy II · sandbox for tutorials and exercises.

## Owner
- **Student:** Martin Mo (`@MartinMo2026`)
- **Course:** AILT9019 — AI Literacy for Computing and Data Science (AI Literacy II)
- **Semester:** 2026–27 Sem 1, HKU

## Setup
- **Python:** 3.13.x (WorkBuddy-managed) on `PATH` as `python`; system `py` launcher points to 3.14.7
- **Git:** configured with GitHub noreply email
- **AI coding tool:** WorkBuddy (used during W1 setup; CodeBuddy or TRAE also accepted by course)

## Hello line
> Hello from Martin, testing my AILT9019 setup.

## Contents
- `hello.py` — minimal first script, prints a greeting. Run with `python hello.py`.
- `final_price.py` — Worked Example 3: a `final_price(price, discount)` function. Run with `python final_price.py`.
- `check_env.py` — Worked Example 4: safely check whether an env var exists (prints `True`/`False`, never the value). Run with `python check_env.py`.
- `grades.py` — core grade calculation logic: `compute_average`, `letter_grade` (now with emoji prefix).
- `main.py` — `grades.py` CLI wrapper. Run with `python main.py` and enter scores one at a time, then `done`.

## Progress
- W0 Worked Examples 1–4 — done (hello, read error, function, env var).
- W1 Tutorial 1 Exercise 1 — done: added emoji prefix to letter grades (`🌟 A`, `👍 B`, `📚 C`, `📝 D`, `💪 F`).

## Goal of this repo
- Practice the vibe-coding loop: describe → inspect → run → test → revise.
- Each tutorial / week leaves a small, runnable change here, with a short README note.
- Final course project will live in a separate team repository (assigned after W3, 16 Sep).

## Workflow
- Save early, save often. After every meaningful change: run `./save.sh "short message about what now works"` from the repo folder.
- The script stages, commits, and pushes in one go. One sentence per commit, focused on *what now works*.
- First-time only: if `bash` complains about permissions, run `chmod +x save.sh` once in Git Bash.
