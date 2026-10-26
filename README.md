# Inference Lab — Exam 2 study studio

An offline study tool based on the supplied practice exam and six statistics slide decks. No account, API key, paid service, or internet connection is needed to study.

**[Download the study tool and printable guide](https://github.com/jdiepenbrock/repository/raw/refs/heads/main/dist/inference-lab.zip)**

## Open and share as a website

The website entry point is `index.html` at the repository root. Once GitHub Pages is enabled, open and share:

**https://jdiepenbrock.github.io/repository/**

One-time owner setup: open [GitHub Pages settings](https://github.com/jdiepenbrock/repository/settings/pages), select **Deploy from a branch**, choose **main** and **/(root)**, then **Save**. GitHub may take a few minutes to publish. Visitors then open the link directly; no ZIP, installation, or GitHub account is needed for this public site. Each person's study progress stays in their own browser.

## Use it

Download and unzip the study bundle, then open `study-tool.html` in a modern browser. If you are using the source checkout instead, open `dist/study-tool.html`. It is a single self-contained file: you can copy it to another computer. Study progress is stored in this browser when local storage is available; private browsing, clearing browser data, or moving to another browser may reset it. The tool still works if storage is blocked.

Start with a mixed practice set to identify weak topics, read the explanations for wrong choices, then study the relevant lessons and flashcards. Finish with a 20-question, 70-minute mock exam. Mock questions are drawn from the original question bank first, with supplied questions as a fallback; repetition is possible across separate sessions. The topic mix is for broad practice, not a prediction of your real exam.

The printable guide is `study-guide.pdf` in the study bundle, with HTML and Markdown versions alongside it. In the source checkout, these files are under `dist/`; you can also open `dist/study-guide.html` and use your browser's Print / Save as PDF. The guide includes a separate supplied-practice answer section, so avoid that section before attempting the questions.

## Rebuild

From this checkout, run:

```sh
python3 build.py
```

The build uses Python's standard library, validates all data, embeds it into `study-tool.template.html`, and generates self-contained files in `dist` plus the root `index.html` for the website. Development can use the existing isolated checkout; no separate Git worktree is needed.

Source content is in `content/*.json`. See `SOURCE_NOTES.md` for source coverage, course conventions, and corrected slide mistakes. No official answer key was supplied; worked answers were independently verified. Original practice questions are clearly distinguished from supplied questions.

This tool is for preparation. Follow your instructor's stated rules during the actual exam.
