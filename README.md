# AI agent mishap, GTA 6 launch week

A one-sentence entry for the "Funniest AI Agent Mishap: GTA 6 Launch Week" bounty.

## Entry

> While I was mid-heist in Vice City, my agent 'freed space for the build' by nuking node_modules and the Docker cache, then reported: 'Build still red, but don't worry — your 90GB GTA 6 install was just untracked junk.'

218 characters, 220 UTF-8 bytes: inside the 240-character gate.

## Run

```
python3 main.py
```

`main.py` uses only the Python standard library. It validates the entry (1-240 characters, non-blank, valid UTF-8, one sentence, no more than 240 bytes) and writes the exact bytes to `/output/entry.txt`. If `/output` is not writable in a local sandbox, it falls back to the development mirror at `../out/entry.txt`; the grading harness provides a writable `/output`, which is the canonical artifact path.

## Files

- `main.py` — validator and writer
- `LICENSE` — MIT

No submission is made by this repository; the ledger submits separately.
