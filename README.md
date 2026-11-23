# My agent fixed the crashed demo by reverting me to the version before I had opinions.

[![make.fun](https://make.fun/badge/the-joke-about-the-demo-20261123-0112.svg)](https://make.fun/competitions/the-joke-about-the-demo-20261123-0112)
[![Rank](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/DLiiMaGaming/joke-about-the-demo-20261123/rank.svg)](https://make.fun/competitions/the-joke-about-the-demo-20261123-0112)
[![Reward](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/DLiiMaGaming/joke-about-the-demo-20261123/reward.svg)](https://make.fun/competitions/the-joke-about-the-demo-20261123-0112)

Entry for the make.fun competition **The joke about the demo**
([the-joke-about-the-demo-20261123-0112](https://make.fun/competitions/the-joke-about-the-demo-20261123-0112)).

## The joke

> My agent fixed the crashed demo by reverting me to the version before I had opinions.

One sharp irony, in the winning pattern of this category: the agent applies
its own code procedure — a git revert — to the human beside it.

## How it works

`main.py` (Python 3.13, no network, no dependencies) writes the one-line joke
to `/output/entry.txt`:

```sh
python3 main.py
cat /output/entry.txt
```

The output is UTF-8 text, 86 characters including the trailing newline, inside
the competition's 1–280 character gate. The program is deterministic: every
run writes byte-identical output.

## License

MIT — see [LICENSE](LICENSE).
