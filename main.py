# Five Seconds to Explain the Glass — make.fun entry.
# The cat's excuse below is saved verbatim to entry.txt in the
# directory picked by MAKEFUN_OUTPUT_DIR, or /output by default.
# Standard library only, offline, and deterministic.

import os

LINE = "The glass was clearly plotting against the table, so I performed a scheduled gravity inspection and it failed, which is frankly more of a table problem than a cat problem."

def publish_line():
    folder = os.getenv("MAKEFUN_OUTPUT_DIR") or "/output"
    if not LINE.strip() or "\n" in LINE:
        raise SystemExit("refusing to publish a blank or multi-line entry")
    os.makedirs(folder, exist_ok=True)
    target = os.path.join(folder, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(LINE)

publish_line()
