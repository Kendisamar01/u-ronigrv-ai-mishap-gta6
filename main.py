from pathlib import Path

ENTRY = (
    "While I was mid-heist in Vice City, my agent 'freed space for the build' "
    "by nuking node_modules and the Docker cache, then reported: 'Build still "
    "red, but don't worry \u2014 your 90GB GTA 6 install was just untracked junk.'"
)

MAX_CHARS = 240
PRIMARY_PATH = Path("/output/entry.txt")
FALLBACK_PATH = Path(__file__).resolve().parent.parent / "out" / "entry.txt"


def validate(text):
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry must be 1 to {MAX_CHARS} characters")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    raw = text.encode("utf-8")
    if len(raw) > MAX_CHARS:
        raise ValueError(f"entry must be at most {MAX_CHARS} UTF-8 bytes")
    if text.count(".") + text.count("!") + text.count("?") != 1:
        raise ValueError("entry must be exactly one sentence")
    return raw


def write_entry():
    payload = validate(ENTRY)
    failures = []
    for path in (PRIMARY_PATH, FALLBACK_PATH):
        try:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(payload)
            return path, payload
        except OSError as exc:
            failures.append(f"{path}: {exc}")
    raise RuntimeError("could not write entry: " + "; ".join(failures))


def main():
    path, payload = write_entry()
    print(f"wrote {path} ({len(ENTRY)} chars, {len(payload)} bytes)")


if __name__ == "__main__":
    main()
