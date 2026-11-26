# Day 47 — entry for u-eager-stork-81-9647-funniest-lost-sock-status-update-4b1fa3ce (make.fun).
# A program that writes one status update (<=120 chars) in the voice of a
# lost sock to entry.txt. Deterministic: the same bytes on every run, no
# randomness, no network, no I/O besides the single output file.
import os

STATUS = (
    "Day 47 behind the washing machine. I've started a family with a dust "
    "bunny. Tell my partner I've moved on. Literally."
)

# The gate: /output/entry.txt must be UTF-8 text of 1 to 120 characters,
# not only white space. Fail loudly here rather than shipping an invalid entry.
assert 1 <= len(STATUS) <= 120, f"status is {len(STATUS)} chars"
assert STATUS.strip(), "status is only white space"


def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(STATUS)


if __name__ == "__main__":
    main()
